from LLD_Projects.composite_design_pattern.calculator.arithmetic_exp_interface import ArithmeticInterface
from LLD_Projects.composite_design_pattern.calculator.constant import Operation


class Expression(ArithmeticInterface):
    def __init__(self, left, right, operation):
        self.left = left
        self.right = right
        self.opr = operation

    def evaluate(self):
        value = 0
        if self.opr == Operation.ADD:
            value = self.left.evaluate() + self.right.evaluate()

        elif self.opr == Operation.SUBTRACT:
            value = self.left.evaluate() - self.right.evaluate()
        elif self.opr == Operation.MULTIPLY:
            value = self.left.evaluate() * self.right.evaluate()
        elif self.opr == Operation.DIVIDE:
            value = self.left.evaluate() / self.right.evaluate()
        print("Expression value is:" , value)
        return value
