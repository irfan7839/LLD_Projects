from LLD_Projects.book_my_show.user.customer_user import Customer


class UserInitiate:
    @staticmethod
    def create_user(user_name, age, gender, city):
        user = Customer()
        user.set_user_name(user_name)
        user.set_user_age(age)
        user.set_user_city(gender)
        user.set_user_city(city)
        return user