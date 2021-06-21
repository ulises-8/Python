"""
CS3B, Assignment #2, RPN Calculator
Ulises Marian
"""
import numpy
#pip install numpy

class MyStack:
    # Constants
    MAX_CAPACITY = 100000
    DEFAULT_CAPACITY = 10

    # Initializer method
    def __init__(self, default_item, capacity=DEFAULT_CAPACITY, dtype=int):
        # If the capacity is bad, fail right away
        if not self.validate_capacity(capacity):
            raise ValueError("Capacity " + str(capacity) + " is invalid")
        self.capacity = capacity
        self.default_item = default_item

        # Make room in the stack and make sure it's empty to begin with
        self.clear()

    def clear(self):
        # Allocate the storage and initialize top of stack
        self.stack = numpy.array([self.default_item for _ in range(
           self.capacity)])
        self.top_of_stack = 0

    @classmethod
    def validate_capacity(cls, capacity):
        return 0 <= capacity <= cls.MAX_CAPACITY

    def push(self, item_to_push):
        if self.is_full():
            raise OverflowError("Push failed - capacity reached")

        self.stack[self.top_of_stack] = item_to_push
        self.top_of_stack += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop failed - stack is empty")

        self.top_of_stack -= 1
        return self.stack[self.top_of_stack]

    def is_empty(self):
        return self.top_of_stack == 0

    def is_full(self):
        return self.top_of_stack == self.capacity

    def get_capacity(self):
        return self.capacity

    def __str__(self):
        string_descr = "in stack is {} and in top_of_stack is {}."
        string_descr = string_descr.format(self.stack, self.top_of_stack)
        return string_descr


def mystack_test():
    # Instantiate two empty stacks, one of 50 ints, another of 15 strings
    s1 = MyStack(-1, 50)
    s2 = MyStack("undefined")
    # and one more with bad argument
    try:
        s3 = MyStack(None, -100)
        print("Failed test: expected __init()__ to reject negative capcity but it didn't")
    except Exception as e:
        print("Successful test: handled negative capacity: " + str(e))

    # Confirm the stack capacities
    print("------ Stack Sizes -------\n  s1: {}   s2: {}\n".
          format(s1.get_capacity(), s2.get_capacity()))

    # Pop empty stack
    print("------ Test stack ------\n")
    try:
        s1.pop()
        print("Failed test: expected pop() to raise empty-stack exception but it didn't")
    except Exception as e:
        print("Successful test: handled popping empty s1: " + str(e))

    # Push some items
    s1.push(44)
    s1.push(123)
    s1.push(99)
    s1.push(10)
    s1.push(1000)
    # try to put a square peg into a round hole
    try:
        s1.push("should not be allowed into an int stack")
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    try:
        s2.push(444)
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    try:
        s1.push(44.4)
        s2.push("bank")
        s2.push("-34")
        s2.push("should be okay")
        s2.push("a penny earned")
        s2.push("item #9277")
        s2.push("where am i?")
        s2.push("4")
        s2.push("4")
        s2.push("4")
        s2.push("4")
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))

    try:
        s2.push("This is when stack is full")
        print("Failed test: expected push() to throw exception but it didn't")
    except Exception as e:
        print("Successful test: handled pushing when stack is full: " + str(e))
    print("\n--------- First Stack ---------\n")

    # Pop and inspect the items
    for k in range(0, 10):
        try:
            print("[" + str(s1.pop()) + "]")
        except Exception as e:
            print("Successful test: handled popping empty stack s1: " + str(e))
    print("\n--------- Second Stack ---------\n")
    for k in range(0, 10):
        print("[" + str(s2.pop()) + "]")


if __name__ == "__main__":
    mystack_test()


class RpnCalculator:
    # class constants
    ADDITION = "+"
    SUBTRACTION = "-"
    FLOOR_DIVISION = "//"
    MULTIPLICATION = "*"
    OPERATORS = [ADDITION, SUBTRACTION, FLOOR_DIVISION, MULTIPLICATION]

    @staticmethod
    def eval(rpn_expression):
        save_list = RpnCalculator.parse(rpn_expression)
        save_result = RpnCalculator.eval_tokens(save_list)
        return save_result

    @staticmethod
    def parse(rpn_expression):
        individual_tok = rpn_expression.split()
        return individual_tok

    @staticmethod
    def eval_tokens(tokens):
        new_stack = MyStack(len(tokens))
        for token in tokens:
            if token.isdigit():
               new_stack.push(token)
            elif token == RpnCalculator.ADDITION:
              operand_1 = new_stack.pop()
              operand_2 = new_stack.pop()
              operation_result = operand_1 + operand_2
              new_stack.push(operation_result)
            elif token == RpnCalculator.SUBTRACTION:
              operand_1 = new_stack.pop()
              operand_2 = new_stack.pop()
              operation_result = operand_1 - operand_2
              new_stack.push(operation_result)
            elif token == RpnCalculator.FLOOR_DIVISION:
              operand_1 = new_stack.pop()
              operand_2 = new_stack.pop()
              operation_result = operand_1 // operand_2
              new_stack.push(operation_result)
            elif token == RpnCalculator.MULTIPLICATION:
              operand_1 = new_stack.pop()
              operand_2 = new_stack.pop()
              operation_result = RpnCalculator.multiply_it(operand_1, operand_2)
              new_stack.push(operation_result)
            elif not token.isdigit() or token not in RpnCalculator.OPERATORS:
                raise ValueError ("ILLEGAL value/operator")
        if new_stack.top_of_stack > 1:
            raise ValueError ("Too many operands!!")
        return new_stack

    @staticmethod
    def multiply_it(multiplicand, multiplier):
        if multiplier == 0:
            return 0
        elif multiplier < 0:
            return -RpnCalculator.multiply_it(multiplicand, - multiplier)
        else:
            return multiplicand + RpnCalculator.multiply_it(multiplicand,
                                                            multiplier - 1)


def test_my_stack():
    # The following lines of code would've worked with the original MyStack
    # because it would've used lists, rather than stacks. Lists allow for
    # heterogeneous data (hence, floats, ints, strings), plus such lists are
    # allowed to increase and decrease in size without constraint, as opposed to
    # the size restriction of stacks.
    s1.append(15.0)
    new_element = s1.pop(3)   # pop item at index 3
    s2.append(new_element)
    s2.append("pizza")
    s1.append(s2)   # append list to list


def test_rpn():
    print("\n----------- Test RPN -----------\n")
    r1 = RpnCalculator()
    try:
        save_result = r1.eval("2")
        print("single number 2 = ", save_result.stack[0])
    except Exception as e:
        print("single number 2 =" + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("3 4 +")
        print("3 4 + = ", save_result.stack[0])
    except Exception as e:
        print("3 4 + " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("3 4 -")
        print("3 4 - = ", save_result.stack[0])
    except Exception as e:
        print("3 4 - " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("3 4 *")
        print("3 4 * = ", save_result.stack[0])
    except Exception as e:
        print("3 4 * " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("3 4 //")
        print("3 4 // = ", save_result.stack[0])
    except Exception as e:
        print("3 4 // " + "EXCEPTION HANDLED: " + str(e))

    #multiple-operation expressions
    try:
        save_result = r1.eval("4 6 * 5 +")
        print("4 6 * 5 + = ", save_result.stack[0])
    except Exception as e:
        print("4 6 * 5 + " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("20 10 + 2 * 80 - 80 //")
        print("20 10 + 2 * 80 - 80 // = ", save_result.stack[0])
    except Exception as e:
        print("20 10 + 2 * 80 - 80 // " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("5 6 8 9 * // - 4 +")
        print("5 6 8 9 * // - 4 + = ", save_result.stack[0])
    except Exception as e:
        print("5 6 8 9 * // - 4 + " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("10 10 // 10 * 20 + 10 - 3333 +")
        print("10 10 // 10 * 20 + 10 - 3333 + = ", save_result.stack[0])
    except Exception as e:
        print("10 10 // 10 * 20 + 10 - 3333 + " + "EXCEPTION HANDLED: " + str(e))

    # handle exceptions
    try:
        save_result = r1.eval("1 2 hello")
        print("1 2 hello = ", save_result.stack[0])
    except Exception as e:
        print("1 2 hello = " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("7 3 * 2 ?")
        print("7 3 * 2 ? = ", save_result.stack[0])
    except Exception as e:
        print("7 3 * 2 ? = " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("3 py 5 + #")
        print("3 py 5 + # = ", save_result.stack[0])
    except Exception as e:
        print("3 py 5 + # = " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("1 2 3 4 -")
        print("1 2 3 - = ", save_result.stack[0])
    except Exception as e:
        print("1 2 3 4 + - = " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("7 6 * 9")
        print("7 6 * 9 = ", save_result.stack[0])
    except Exception as e:
        print("7 6 * 9 = " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("8 0 4 + 9 7 - 3 // 6")
        print("8 0 4 + 9 7 - 3 // 6 = ", save_result.stack[0])
    except Exception as e:
        print("8 0 4 + 9 7 - 3 // 6 = " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("1 2 - - -")
        print("1 2 - - - = ", save_result.stack[0])
    except Exception as e:
        print("1 2  - - - = " + "EXCEPTION HANDLED: " + str(e))
    try:
        save_result = r1.eval("3 6 * 7 - +")
        print("3 6 * 7 - + = ", save_result.stack[0])
    except Exception as e:
        print("3 6 * 7 - + = " + "EXCEPTION HANDLED: " + str(e))


if __name__ == "__main__":
    test_rpn()
