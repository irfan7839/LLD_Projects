from LLD_Projects.book_my_show.movies.movies import Movie
from LLD_Projects.book_my_show.movies.movies_controller import MoviesController


class MovieInitiate:

    @staticmethod
    def create_movies(movie_id, name, duration, genre):
        movie = Movie()
        movie.set_movie_id(movie_id)
        movie.set_movie_name(name)
        movie.set_movie_duration(duration)
        movie.movie_genre(genre)
        return movie

    @staticmethod
    def create_movie_controller():
        movie_controller = MoviesController()
        return movie_controller

    @staticmethod
    def add_movies_in_controller(movie_controller, movie_list):
        for movie in movie_list:
            movie_controller.add_movie_in_list(movie)

    @staticmethod
    def find_movie_in_controller(movie_controller, movie):
        movie_controller.get_movie(movie)

    @staticmethod
    def find_movies_by_city(movie_controller, city):
        movie_controller.get_movie_from_city(city)

    @staticmethod
    def remove_movie_from_controller_of_city(movie_controller, city, movie):
        movie_controller.remove_movie_from_city(city, movie)

    @staticmethod
    def remove_movie_from_controller(movie_controller, movie):
        movie_controller.remove_movie(movie)
