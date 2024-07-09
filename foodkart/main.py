from LLD_Projects.foodkart.orders.order import Order
from LLD_Projects.foodkart.restaurant.restaurant import Restaurant
from LLD_Projects.foodkart.restaurant.restaurant_management import RestaurantManagement
from LLD_Projects.foodkart.user.customer import Customer
from LLD_Projects.foodkart.user.restaurant_owner import RestaurantOwner
from LLD_Projects.foodkart.user_management.customer_management import CustomerManagement
from LLD_Projects.foodkart.user_management.owner_management import OwnerManagement


class Main:
    @staticmethod
    def start():
        restaurant = Restaurant()
        restaurant.set_restaurant_id(123)
        restaurant.set_restaurant_name('FoodHub')
        restaurant.set_restaurant_food("Chicken 65")
        restaurant.set_food_price(250)
        restaurant.set_initial_quantity(20)
        restaurant.add_pin_code_list('843302')
        restaurant_owner_list = OwnerManagement()
        owner = RestaurantOwner()
        customer_list = CustomerManagement()
        owner.set_user_name("ABC")
        owner.set_user_age(20)
        owner.set_user_phone('123456789', restaurant_owner_list)
        owner.set_user_gender('M')
        owner.set_restaurant(restaurant)
        customer = Customer()
        customer.set_user_name('Ayan')
        customer.set_user_age(20)
        customer.set_user_phone('8757235380', customer_list)
        customer.set_user_pincode('843302')
        rest_management = RestaurantManagement()
        rest_management.add_restaurant(restaurant)
        rest_order = rest_management.get_restaurants_by_area('843302')
        order = Order()
        order.set_restaurant_details(rest_order[0])
        order.set_total_quantity(18)
        order.set_total_price()
        order.print_receipt()

main = Main()
main.start()

