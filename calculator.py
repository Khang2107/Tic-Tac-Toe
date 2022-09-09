from abc import *

class Operator(ABC):
    @abstractclassmethod
    def calculate(self, a, b):
        pass

    @abstractclassmethod
    def get_symbol(self):
        pass

# o = Operator()


class Calculator:
    def __init__(self):
        self.operators = []

    def register(self, op):
        self.operators.append(op)

    def calculate(self):
        a = float(input("Value 1: "))
        op = input("Operator: ")
        b = float(input("Value 2: "))

        for x in self.operators:
            if x.get_symbol() == op:
                print(a, x.get_symbol(), b, "=", x.calculate(a, b))


class Addition(Operator):
    def calculate(self, a, b):
        return a + b

    def get_symbol(self):
        return "+"


class Subtraction(Operator):
    def calculate(self, a, b):
        return a - b

    def get_symbol(self):
        return "-"


class Multiplication(Operator):
    def calculate(self, a, b):
        return a * b

    def get_symbol(self):
        return "*"


class Division(Operator):
    def calculate(self, a, b):
        return a / b

    def get_symbol(self):
        return "/"


c = Calculator()
add = Addition()
c.register(add)

c.register(Subtraction())
c.register(Multiplication())
c.register(Division())

c.calculate()
