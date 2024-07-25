from LLD_Projects.composite_design_pattern.calculator.arithmetic_exp_interface import ArithmeticInterface


class NumberClass(ArithmeticInterface):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        print('Number is:' , self.value)
        return self.value
