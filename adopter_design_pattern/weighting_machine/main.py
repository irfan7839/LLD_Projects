from LLD_Projects.adopter_design_pattern.weighting_machine.existing_weight_machine import Weight
from LLD_Projects.adopter_design_pattern.weighting_machine.weight_adopter import WeightAdopter


class Main:
    @staticmethod
    def start():
        wt_in_pound = Weight()
        wt_in_pound.set_weight(55)
        wt_in_kg = WeightAdopter(wt_in_pound)
        wt_in_kg.get_weight()


main = Main()
main.start()
