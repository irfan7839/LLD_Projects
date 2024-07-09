class RestaurantManagement:
    def __init__(self):
        self.restaurant_list = []

    def get_restaurants_by_area(self, pincode):
        rest_list = []
        for rest in self.restaurant_list:
            for pin in rest.pin_list:
                if pin == pincode:
                    rest_list.append(rest)
        if not rest_list:
            print('No restaurant available in this area ')
            return
        return rest_list

    def add_restaurant(self, restaurant):
        for rest in self.restaurant_list:
            if rest == restaurant:
                print("restaurant already exist")
                return
        self.restaurant_list.append(restaurant)
        print("restaurant added successfully")
        return

    def remove_restaurant(self, restaurant):
        for rest in self.restaurant_list:
            if rest == restaurant:
                self.restaurant_list.remove(restaurant)
                print("restaurant removed successfully")
                return
        print("Restaurant does not exist! ")
        return

    @staticmethod
    def display_restaurants(rest_list):
        if rest_list:
            print('restaurant name \t\t specialized food \t price')
        else:
            print("No restaurant available in this area")
        for rest in rest_list:
            print(f'{rest.name}\t\t {rest.specialized_food}\t {rest.price}')
