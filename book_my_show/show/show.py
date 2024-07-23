class Show:
    def __init__(self):
        self.show_id = None
        self.movie = None
        self.screen = None
        self.start_time = None
        self.booked_seat_list = []

    def get_show_id(self):
        return self.show_id

    def get_movie_in_show(self):
        return self.movie

    def get_screen(self):
        return self.screen

    def get_start_time(self):
        return self.start_time

    def get_seat_list(self):
        return self.booked_seat_list

    def set_show_id(self, show_id):
        self.show_id = show_id

    def set_movie_in_show(self, movie):
        self.movie = movie

    def set_screen(self, screen):
        self.screen = screen

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_seat_list(self, booked_seat_list):
        self.booked_seat_list = booked_seat_list

    def add_booked_seat_list(self, seat_list):
        for seat in seat_list:
            if seat not in self.booked_seat_list:
                self.booked_seat_list.append(seat)

        print('Seats added successfully')

    def remove_booked_seat_list(self, seat_list):
        for seat in seat_list:
            if seat in self.booked_seat_list:
                self.booked_seat_list.remove(seat)

        print('Seats removed successfully')
