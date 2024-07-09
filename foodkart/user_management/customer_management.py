from LLD_Projects.foodkart.user_management.user_management_interface import UserManagement


class CustomerManagement(UserManagement):

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

    def check_user_exist_by_phone(self, phone):
        for user in self.user_list:
            if user.phone == phone:
                return True
        return False