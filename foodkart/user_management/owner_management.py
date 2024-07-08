from foodkart.user_management.user_management_interface import UserManagement


class OwnerManagement(UserManagement):

    def get_user_list(self):
        return self.user_list

    def update_user_list(self, user):
        for user_data in self.user_list:
            if user.phone == user_data.phone:
                print("user already exist")
                return
        self.user_list.append(user)

    def get_user_by_phone(self, phone):
        for user in self.user_list:
            if user.phone == phone:
                return user
        print("No user exist with this phone nummber! ")

    def get_user_by_restaurant(self, restaurant_name):
        for user in self.user_list:
            if user.restaurant.name == restaurant_name:
                return user
        print("No user exist for this restaurant! ")
