from car_rental_system.location.location import Location
from car_rental_system.stores.stores import Stores
from car_rental_system.users.user import User
from car_rental_system.vehicles.vehicles import Vehicles


def create_user():
    user = User()
    user_id = input('please provide user id')
    user_name = input('please provide user name')
    user.create_user(user_id, user_name)
    d_license = input('please provide driving license')
    user.add_driving_license(d_license)
    return user


def create_location():
    state = input('please provide state')
    city = input('please provide city')
    address = input('please provide address')
    pincode = int(input('please provide pincode'))

    location = Location(state, city, address, pincode)
    return location


def create_vehicle():
    vehicle = Vehicles()
    v_number = input('please provide vehicle number')
    v_type = input('please provide vehicle type')
    milage = input('please provide milage')
    manufacturer = input('please provide manufacturer')
    vehicle.add_vehicle(v_number, v_type, milage, manufacturer)
    return vehicle


def create_store():
    location = create_location()
    store = Stores(123, location)
    vehicle = create_vehicle()
    store.set_vehicles([vehicle])
    return store


if __name__ == '__main__':
    pass
