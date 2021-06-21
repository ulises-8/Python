"""
CS3B, Assignment #5, Logic gate simulation (Part 2)
Ulises Marian
"""
from abc import ABC, abstractmethod

class Input:
    """A class representing an input"""

    def __init__(self, owner):
        if not isinstance(owner, LogicGate):
            raise TypeError("Owner should be a type of LogicGate")
        self._owner = owner

    def __str__(self):
        try:
            return str(self.value)
        except AttributeError:
            # It's possible to not have a value at the beginning, so
            # handle the exception properly.
            return "(no value)"

    @property
    def owner(self):
        return self._owner

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        # Normalize the value to bool
        self._value = bool(value)
        # Now that the input value has changed, tell to owner logic gate
        # to re-evaluate
        self.owner.evaluate()


class Output:
    """A class representing an output"""

    def __init__(self):
        self._connections = []

    def __str__(self):
        try:
            return str(self.value)
        except AttributeError:
            # It's possible not to have a value at the beginning
            return "(no value)"

    def connect(self, input_):
        if not isinstance(input_, Input):
            raise TypeError("Output must be connected to an input")
        # If the input is not already in the list, add it; alternative is to
        # use a set.
        if input_ not in self.connections:
            self.connections.append(input_)
        try:
            # Set the input's value to this output's value upon connection
            input_.value = self._value
        except AttributeError:
            # If self.value is not there, skip it
            pass

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        # Normalize the value to bool
        self._value = bool(value)
        # After the output value changes, set all the connected inputs
        # to the same value.
        for connection in self.connections:
            connection.value = self.value

    @property
    def connections(self):
        return self._connections

class CostMixin(ABC):
    COST_MULTIPLIER = 10

    @abstractmethod
    def __init__(self, number_of_components):
        self._number_of_components = number_of_components

    @property
    def number_of_components(self):
        return self._number_of_components

    @property
    def cost(self):
        self._cost = CostMixin.COST_MULTIPLIER * (self.number_of_components
                                                  ** 2)
        return self._cost
        #following prof's solution:should have initialized self._cost in init:
        #self._cost = self.COST_MULTIPLIER * (self.number_of_components ** 2)

class NodeMixin(ABC):

    @abstractmethod
    def __init__(self): # initialize what you think is necessary
        self._next = None    #this next is an attribute

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_): # this next is an argument/parameter (object)
        # verify the new node is the right type,
        # and raise a TypeError if not.
        if (next_ is not None) and (not isinstance(next_, NodeMixin)):
            raise TypeError
        self._next = next_

class LogicGate(CostMixin, NodeMixin):
    """Base class for all logic gates."""
    @abstractmethod
    def __init__(self, name, number_of_components, circuit):
        self._name = name
        CostMixin.__init__(self, number_of_components)
        NodeMixin.__init__(self)
        self._circuit = circuit

    @property
    def name(self):
        return self._name


class UnaryGate(LogicGate):
    """A class representing logic gate with a single input."""

    NUMBER_OF_COMPONENTS = 2

    @abstractmethod
    def __init__(self, name, circuit):
        super().__init__(name, self.NUMBER_OF_COMPONENTS, circuit)
        self._input = Input(self)   # self because it is the gate, the owner
        self._output = Output()

    def __str__(self):
        return (f"LogicGate {self.name}: input={self.input}, "
                f"output={self.output}")

    @property
    def input(self):
        return self._input

    @property
    def output(self):
        return self._output


class BinaryGate(LogicGate):
    """A class representing logic gate with two inputs."""

    NUMBER_OF_COMPONENTS = 3

    @abstractmethod
    def __init__(self, name, circuit):
        super().__init__(name, self.NUMBER_OF_COMPONENTS, circuit)
        self._input0 = Input(self) # self because it is the gate, the owner
        self._input1 = Input(self) # self because it is the gate, the owner
        self._output = Output()

    def __str__(self):
        return (f"LogicGate {self.name}: input0={self.input0}, "
                f"input1={self.input1}, output={self.output}")

    @property
    def input0(self):
        return self._input0

    @property
    def input1(self):
        return self._input1

    @property
    def output(self):
        return self._output


class NotGate(UnaryGate):
    def __init__(self, name, circuit):
        super().__init__(name, circuit)
        if not isinstance(circuit, Circuit):
            raise TypeError
        self._circuit = circuit # circuit should have a default value of None
        if circuit is not None: #add logic gate to circuit
            circuit.add(self)

    def evaluate(self):
        try:
            self.output.value = not self.input.value
        except AttributeError:
            pass


class AndGate(BinaryGate):
    def __init__(self, name, circuit):
        super().__init__(name, circuit)
        if not isinstance(circuit, Circuit):
            raise TypeError
        self.circuit = circuit # circuit should have a default value of None
        if circuit is not None: # add logic gate to circuit
            circuit.add(self)

    def evaluate(self):
        try:
            # This may throw an exception, if one of the input is not yet set,
            # which is possible in the normal course of evaluation, because
            # setting the first input will kick off the evaluation.  So just
            # don't set the output.
            self.output.value = self.input0.value and self.input1.value
        except AttributeError:
            pass


class OrGate(BinaryGate):
    def __init__(self, name, circuit):
        super().__init__(name, circuit)
        if not isinstance(circuit, Circuit):
            raise TypeError
        self.circuit = circuit # circuit should have a default value of None
        if circuit is not None: #add logic gate to circuit
            circuit.add(self)

    def evaluate(self):
        try:
            self.output.value = self.input0.value or self.input1.value
        except AttributeError:
            pass


class XorGate(BinaryGate):
    def __init__(self, name, circuit):
        super().__init__(name, circuit)
        if not isinstance(circuit, Circuit):
            raise TypeError
        self.circuit = circuit # circuit should have a default value of None
        if circuit is not None: #add logic gate to circuit
            circuit.add(self)

    def evaluate(self):
        try:
            # Assume the value is bool, != is same as xor
            self.output.value = (self.input0.value != self.input1.value)
        except AttributeError:
            pass


class Circuit:
    # implement your own linked list-like data structure in this class

    def __init__(self):
        self._head = None
        self._cost = None

    def add(self, gate):
        if not isinstance(gate, LogicGate):
            raise TypeError
        gate.next = self._head  # node becomes new top, with its next pointing
                                # to the 'old' top
        self._head = gate       # adds a gate to the circuit in any order

    @property
    def cost(self):
        total_cost = 0
        gate = self._head    #start at the head
        # This is the total of the costs of all the gates in the circuit
        # traverse the linked list of gates and add up the cost of each gate.
        while gate is not None:
            total_cost += gate.cost
            gate = gate.next
        return total_cost


def full_adder(a, b, ci):
    circuit5 = Circuit()
    x1 = XorGate("x1", circuit5)
    x2 = XorGate("x2", circuit5)
    a1 = AndGate("a1", circuit5)
    a2 = AndGate("a2", circuit5)
    or1 = OrGate("or1", circuit5)

    x1.input0.value = a
    x1.input1.value = b
    x2.input0.value = x1.output.value
    #print(x1.output.value)

    x2.input1.value = ci
    #print(x2.output.value)

    a1.input0.value = a
    a1.input1.value = b
    #print(a1.output.value)

    a2.input0.value = ci
    a2.input1.value = x1.output.value
    #print(a2.output.value)

    or1.input1.value = a1.output.value
    or1.input0.value = a2.output.value
    #print(or1.output.value)

    return x2.output.value, or1.output.value, circuit5.cost

possible_combinations = [full_adder(a=True, b=False, ci=True),
                         full_adder(a=True, b=True, ci=False),
                         full_adder(a=True, b=True, ci=True),
                         full_adder(a=False, b=True, ci=True),
                         full_adder(a=False, b=False, ci=True),
                         full_adder(a=False, b=False, ci=False),
                         full_adder(a=True, b=False, ci=False),
                         full_adder(a=False, b=True, ci=False)]

print("1-bit full adder test:")

for combination in possible_combinations:
    print(combination)


def test():
    """Umbrella test function"""
    tests = [
        test_not_not,
        test_and_not,
        test_input,
        test_output,
        test_not,
        test_and,
        test_or,
        test_xor,
    ]
    for t in tests:
        print("Running " + t.__name__ + " " + "-" * 20)
        t()

circuit0 = Circuit()

# test NOT-NOT circuit
def test_not_not():
    not_gate1 = NotGate("not1", circuit0)
    not_gate2 = NotGate("not2", circuit0)
    not_gate1.output.connect(not_gate2.input)
    print("Cost of NOT-NOT circuit is " + str(circuit0.cost))

circuit1 = Circuit()

# test AND-NOT circuit
def test_and_not():
    and_gate1 = AndGate("and1", circuit1)
    not_gate1 = NotGate("not1", circuit1)
    and_gate1.output.connect(not_gate1.input)
    print("Cost of AND-NOT circuit is " + str(circuit1.cost))


def test_input():
    input_ = Input(NotGate("test", circuit0))
    print("Initially, input_ is:", input_)
    try:
        print(input_.value)
        print("Failed: input_.value exists before it's set, which should not happen!")
    except AttributeError:
        print("Succeeded: input_.value doesn't exist before it's set.")
    input_.value = True
    print("After set to True, input_ is:", input_)


def test_output():
    output = Output()
    print("Initially, output is:", output)
    try:
        print(output.value)
        print("Failed: output.value exists before it's set, which should not happen!")
    except AttributeError:
        print("Succeeded: output.value doesn't exist before it's set.")
    output.value = True
    print("After set to True, output is:", output)

def test_not():
    not_gate = NotGate("not", circuit0)
    not_gate.input.value = True
    print(not_gate)
    not_gate.input.value = False
    print(not_gate)


def test_and():
    and_gate = AndGate("and", circuit0)
    print("AND gate initial state:", and_gate)
    and_gate.input0.value = True
    print("AND gate with 1 input set", and_gate)
    and_gate.input1.value = False
    print("AND gate with 2 inputs set:", and_gate)
    and_gate.input1.value = True
    print("AND gate with 2 inputs set:", and_gate)


def test_or():
    or_gate = OrGate("or", circuit0)
    or_gate.input0.value = False
    or_gate.input1.value = False
    print(or_gate)
    or_gate.input1.value = True
    print(or_gate)


def test_xor():
    xor_gate = XorGate("xor", circuit0)
    xor_gate.input0.value = False
    xor_gate.input1.value = False
    print(xor_gate)
    xor_gate.input1.value = True
    print(xor_gate)

# old test
#def test_not_not():
    #not_gate1 = NotGate("not1", circuit)
    #not_gate2 = NotGate("not2", circuit)
    #not_gate1.output.connect(not_gate2.input)
    #print(not_gate1)
    #print(not_gate2)
    #print("Setting not-gate input to False...")
    #not_gate1.input.value = False
    #print(not_gate1)
    #print(not_gate2)

# old test
#def test_and_not():
    #and_gate = AndGate("and", circuit)
    #not_gate = NotGate("not", circuit)
    #and_gate.output.connect(not_gate.input)
    #and_gate.input0.value = True
    #and_gate.input1.value = False
    #print(and_gate)
    #print(not_gate)
    #and_gate.input1.value = True
    #print(and_gate)
    #print(not_gate)


if __name__ == '__main__':
    test()
