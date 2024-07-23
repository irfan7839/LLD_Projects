from LLD_Projects.book_my_show.screen.screen import Screen
from LLD_Projects.book_my_show.seat.seat import Seat
from LLD_Projects.book_my_show.seat.seat_enum import SeatType
from LLD_Projects.book_my_show.show.show import Show
from LLD_Projects.book_my_show.theater.theater import Theater
from LLD_Projects.book_my_show.theater.theather_controller import TheatersController


class TheaterInitiate:

    @staticmethod
    def create_seats(no_of_silver_seats, no_of_platinum_seats, no_of_gold_seats):
        seat_id = 1
        row = 1
        list_of_seats = []
        total_seats = no_of_silver_seats + no_of_gold_seats + no_of_platinum_seats
        for i in range(1, total_seats + 1):
            seat = Seat()
            if i <= no_of_silver_seats:
                if seat_id < 10:
                    seat.set_seat_id(seat_id)
                    seat.set_seat_row(row)
                    seat.set_seat_type(SeatType.Silver)
                    seat_id += 1
                elif seat_id == 10:
                    seat.set_seat_id(seat_id)
                    seat.set_seat_row(row)
                    seat.set_seat_type(SeatType.Silver)
                    seat_id = 1
                    row += 1

            elif i <= no_of_gold_seats:
                seat = Seat()
                if seat_id < 10:
                    seat.set_seat_id(seat_id)
                    seat.set_seat_row(row)
                    seat.set_seat_type(SeatType.Gold)
                    seat_id += 1
                elif seat_id == 10:
                    seat.set_seat_id(seat_id)
                    seat.set_seat_row(row)
                    seat.set_seat_type(SeatType.Gold)
                    seat_id = 1
                    row += 1
            elif i <= no_of_platinum_seats:
                seat = Seat()
                if seat_id < 10:
                    seat.set_seat_id(seat_id)
                    seat.set_seat_row(row)
                    seat.set_seat_type(SeatType.Platinum)
                    seat_id += 1
                elif seat_id == 10:
                    seat.set_seat_id(seat_id)
                    seat.set_seat_row(row)
                    seat.set_seat_type(SeatType.Platinum)
                    seat_id = 1
                    row += 1
            list_of_seats.append(seat)
        return list_of_seats

    @staticmethod
    def initiate_screen(screen_id, list_of_seats):
        screen = Screen()
        screen.set_screen_id(screen_id)
        screen.set_seat_list(list_of_seats)
        return screen

    @staticmethod
    def initiate_show(show_id, movie, screen, start_time, booked_seats):
        show = Show()
        show.set_show_id(show_id)
        show.set_movie_in_show(movie)
        show.set_screen(screen)
        show.set_seat_list(start_time)
        show.set_seat_list(booked_seats)
        return show

    @staticmethod
    def initiate_theater(theater_id, city, address, screen, show):
        theater = Theater()
        theater.set_theater_id(theater_id)
        theater.set_theater_address(address)
        theater.set_theater_city(city)
        theater.set_theater_show_list(show)
        theater.set_theater_screen_list(screen)
        return theater

    @staticmethod
    def initiate_theater_controller():
        theater_controller = TheatersController()
        return theater_controller
