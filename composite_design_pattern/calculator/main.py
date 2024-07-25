from LLD_Projects.composite_design_pattern.calculator.constant import Operation
from LLD_Projects.composite_design_pattern.calculator.expression import Expression
from LLD_Projects.composite_design_pattern.calculator.number import NumberClass


class Main:
    @staticmethod
    def start():
        num_one = NumberClass(1)
        num_two = NumberClass(2)
        num_seven = NumberClass(7)
        exp_one = Expression(num_one, num_seven, Operation.ADD)
        exp_two = Expression(num_two, exp_one, Operation.MULTIPLY)
        print(exp_two.evaluate())


main = Main()
main.start()
