class TheatersController:
    def __init__(self):
        self.city_theater_map = {}
        self.theater_list = []

    def add_movie_in_city(self, city, theater):
        if city not in self.city_theater_map:
            self.city_theater_map[city] = [theater]
        else:
            self.city_theater_map[city].append(theater)
        print('theater added successfully in city!')

    def add_theater_in_list(self, theater):
        if theater not in self.theater_list:
            self.theater_list.append(theater)
            print('Movie added successfully in city!')
            return
        raise Exception('Movie already exist in movie list!')

    def remove_theater_from_city(self, city, theater):
        if city not in self.city_theater_map:
            raise Exception("This city does not exist in Controller!")
        else:
            if theater not in self.city_theater_map[city]:
                raise Exception("This theater does not exist in particular city!")
            self.city_theater_map[city].remove(theater)
            print('theater removed successfully in city')
            return

    def remove_theater(self, theater):
        if theater not in self.theater_list:
            raise Exception("This theater does not exist in Controller!")
        else:
            self.theater_list.remove(theater)
            print('theater removed successfully from Controller!')
            return

    def get_theater_from_city(self, city, theater):
        if city not in self.city_theater_map:
            raise Exception("This city does not exist in Controller!")
        else:
            for theat in self.city_theater_map[city]:
                if theat == theater:
                    return theat
            raise Exception("This theater does not exist in particular city!")

    def get_theater(self, theater):
        for theat in self.theater_list:
            if theat == theater:
                return theat
            raise Exception("This theater does not exist in particular city!")
