from LLD_Projects.book_my_show.seat.seat_enum import SeatStatus


class Screen:
    def __init__(self):
        self.screen_id = None
        self.seat_list = []

    def get_screen_id(self):
        return self.screen_id

    def get_seat_list(self):
        return self.seat_list

    def set_screen_id(self, screen_id):
        self.screen_id = screen_id

    def set_seat_list(self, seat_list):
        self.seat_list = seat_list

    def add_seat_in_list(self, seat):
        if seat not in self.seat_list:
            self.seat_list.append(seat)
            print('Seat added successfully!')
            return
        raise Exception('This seat already exist!')

    def remove_seat(self, seat):
        if seat not in self.seat_list:
            raise Exception("This seat does not exist in seat list!")
        else:
            self.seat_list.remove(seat)
            print('Seat removed successfully from Controller!')
            return

    def get_list_of_selected_seat(self, seat_ids):
        selected_seats = []
        for seat in self.seat_list:
            for seat_id in seat_ids:
                if seat.seat_id == seat_id:
                    selected_seats.append(seat)
        return selected_seats

    def get_list_of_booked_seats(self):
        selected_seats = []
        for seat in self.seat_list:
            if seat.status.value == SeatStatus.BOOKED:
                selected_seats.append(seat)
        return selected_seats
