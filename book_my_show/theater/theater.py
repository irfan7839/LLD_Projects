class Theater:
    def __init__(self):
        self.theater_id = None
        self.theater_address = None
        self.theater_city = None
        self.screen_list = []
        self.show_list = []

    def get_theater_id(self):
        return self.theater_id

    def get_theater_address(self):
        return self.theater_address

    def get_theater_city(self):
        return self.theater_city

    def get_theater_screen_list(self):
        return self.screen_list

    def get_theater_show_list(self):
        return self.show_list

    def set_theater_id(self, theater_id):
        self.theater_id = theater_id

    def set_theater_address(self, theater_address):
        self.theater_address = theater_address

    def set_theater_city(self, theater_city):
        self.theater_city = theater_city

    def set_theater_screen_list(self, screen_list):
        self.screen_list = screen_list

    def set_theater_show_list(self, show_list):
        self.show_list = show_list

    def add_show_in_theater(self, show):
        if show not in self.show_list:
            self.show_list.append(show)
            print('Show added successfully in theater!')
            return
        raise Exception('Show already exist in theater!')

    def remove_show_from_theater(self, show):
        if show not in self.show_list:
            raise Exception('Show does not exist in theater!')

        self.show_list.remove(show)

    def add_screen_in_theater(self, screen):
        if screen not in self.screen_list:
            self.screen_list.append(screen)
            print('Screen added successfully in theater!')
            return
        raise Exception('Screen already exist in theater!')

    def remove_screen_from_theater(self, screen):
        if screen not in self.screen_list:
            raise Exception('Screen does not exist in theater!')

        self.screen_list.remove(screen)

    def display_shows(self):
        if self.show_list:
            print('movie name\t\t start time\t\t end time')
        else:
            raise Exception('No Movie available')
        for show in self.show_list:
            print(f'{show.movie.movie_name}\t\t {show.start_time}\t\t {show.end_time}')

    def filter_shows_by_movie(self, movie):
        if self.show_list:
            print('show id\t\t movie name\t\t start time\t\t end time')
        else:
            raise Exception('No Movie available')
        for show in self.show_list:
            if show.movie.movie_name == movie:
                print(f'{show.show_id}\t\t {show.movie.movie_name}\t\t {show.start_time}\t\t {show.end_time}')

    def get_shows_by_id(self, show_id):
        for show in self.show_list:
            if show.show_id == show_id:
                return show
        raise Exception('No show with this id exist')
