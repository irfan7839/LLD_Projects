from LLD_Projects.adopter_design_pattern.weighting_machine.existing_wt_machine_interface import WeightMachineInterface


class Weight(WeightMachineInterface):
    def __init__(self):
        self.weight = None

    def get_weight(self):
        print(f'weight in pounds {self.weight}')
        return self.weight

    def set_weight(self, weight):
        self.weight = weight
