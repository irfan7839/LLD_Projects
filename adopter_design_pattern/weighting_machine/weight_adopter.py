class WeightAdopter:
    def __init__(self, weight_in_pound):
        self.weight_in_pound = weight_in_pound

    def get_weight(self):
        wt_constant = 0.453592
        adopter_weight = self.weight_in_pound.get_weight() * wt_constant
        print(f'weight is {adopter_weight} kgs!')
        return adopter_weight
