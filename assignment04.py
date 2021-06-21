class Input:
    def __init__(self, owner):
        if isinstance(owner, LogicGate):
            self._owner = owner
        else:
            raise TypeError

    def __str__(self):
       #if isinstance(owner, LogicGate):
            #if hasattr(self.owner.input0, '_value') and hasattr(
              # self.owner.input1, '_value') :
       if hasattr(self, '_value'):
          return f"{self._value}"
       else:
          return "(no value)"
    """"        #try:
            #    return f"{self._value}"
            #except:
             #   return "(no value)"
        #elif self.owner == AndGate or OrGate or XorGate:
           # if hasattr(self.owner.input0, '_value') and hasattr(
           # self.owner.input1, '_value'):
           #    return f"{self.owner.input0._value} {self.owner.input1._value}"
           # else:
           #     return "(no value)"
    """

    @property
    def owner(self):
        return self._owner

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = bool(value)
        self.owner.evaluate()


class Output:
    def __init__(self):
        pass  # takes NO parameters
       # should not give an initial value to the value attribute

    def __str__(self):
        if hasattr(self, '_value'):
            return f"{self._value}"
        else:
            return "(no value)"
      # if value is not set, in which case the string should be "(no value)"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
   # this is saving the value from evaluate, that is coming from input...

class LogicGate:
    def __init__(self, name):
        self._name = name
        self._output = Output()  # an instance of the output class

    @property
    def name(self):
        return self._name

    @property
    def output(self):
        return self._output


# def evaluate(self):
# self.output.value = True

# work on this
# raise Exception ("not implemented")
# in this base class, in case I forget to define evaluate() in one of
# the gates
# it is just a reminder. Not necessary


class NotGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)  # input0 is an instance of the Input class

    def __str__(self):
        return f"Gate '{self.name}': input={self.input0}, output={self.output}"

    @property
    def input0(self):
        return self._input0

    def evaluate(self):
        self.output.value = not self.input0.value
        return self.output.value


class AndGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)  # input0 is an instance of the Input class
        self._input1 = Input(self)

    def __str__(self):
        return f"Gate '{self.name}': input0={self.input0}, input1=" \
               f"{self.input1}, output={self.output}"

    @property
    def input0(self):
        return self._input0

    @property
    def input1(self):
        return self._input1

    def evaluate(self):
        if hasattr(self, '_input0') and hasattr(self, '_input1'):
            self.output.value = (self.input0.value and self.input1.value)
            return self.output.value
        else:
            return "output not set"


class OrGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)  # input0 is an instance of the Input class
        self._input1 = Input(self)

    def __str__(self):
        return f"Gate '{self.name}': input0={self.input0}, input1=" \
               f"{self.input1}, output={self.output}"

    @property
    def input0(self):
       return self._input0

    @property
    def input1(self):
        return self._input1

    def evaluate(self):
       if hasattr(self, '_input0') and hasattr(self, '_input1'):
           self.output.value = (self.input0.value or self.input1.value)
           return self.output.value
       else:
           return "value not set"


class XorGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)  # input0 is an instance of the Input class
        self._input1 = Input(self)

    def __str__(self):
        return f"Gate '{self.name}':, input0={self.input0}, input1=" \
             f"{self._input1}, output={self.output}"

    @property
    def input0(self):
        return self._input0

    @property
    def input1(self):
        return self._input1

    def evaluate(self):
        if self.input0.value != self.input1.value:
            self.output.value = True
        else:
            self.output.value = False
        return self.output.value


# ---------- Testing ------------------

# test class Input
def test_input():
    input_ = Input(NotGate("TESTING NOT GATE"))
    print("Initially, input_ is:", input_)
    try:
        print(input_.value)
        print(
           "Failed: input_.value exists before it's set, which should not "
           "happen!")
    except AttributeError:
        print("Succeeded: input_.value doesn't exist before it's set.")

test_input()

print()

# test class Output
def test_output():
    output_ = Output()
    print("Initially, output_ is:", output_)
    try:
        print(output_.value)
        print(
           "Failed: output_.value exists before it's set, which should not "
           "happen!")
    except AttributeError:
        print("Succeeded: output_.value doesn't exist before it's set.")
    output_.value = True
    print("After set to True, input_ is:", output_)

test_output()

print()

# test class NotGate
def test_notgate():
    not_gate = NotGate("not")
    print(not_gate)
    not_gate.input0.value = True  # Note: we are setting not_gate.input.value,
    print(not_gate.output.value)  # should print False
    print(not_gate)
    not_gate.input0.value = False
    print(not_gate)

test_notgate()

print()

# test class AndGate
def test_andgate():
    and_gate = AndGate("and")
    print(and_gate)
    and_gate.input0.value = False
    and_gate.input1.value = True
    print(and_gate.output.value)  # should be False
    print(and_gate)               # output=False
    and_gate.input0.value = True
    and_gate.input1.value = True
    print(and_gate)
    and_gate.input0.value = False
    and_gate.input1.value = False
    print(and_gate)

test_andgate()

print()

# test class OrGate
def test_orgate():
    or_gate = OrGate("or")
    print(or_gate)
    or_gate.input0.value = True
    print(or_gate.output.value)  # should print NOT SET
    print(or_gate)
    or_gate.input1.value = False
    print(or_gate.output.value)
    print(or_gate)

test_orgate()

print()

# test class XorGate
def test_xorgate():
    xor_gate = XorGate("xor")
    print(xor_gate)
    xor_gate.input0.value = False
    print(xor_gate.output.value)  # should print NOT SET
    print(xor_gate)
    xor_gate.input1.value = True
    print(xor_gate.output.value)  # should be False
    print(xor_gate)  # output=False

test_xorgate()