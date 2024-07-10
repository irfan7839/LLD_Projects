class MoviesController:
    def __init__(self):
        self.city_movie_map = {}
        self.movie_list = []

    def add_movie_in_city(self, city, movie):
        if city not in self.city_movie_map:
            self.city_movie_map[city] = [movie]
        else:
            self.city_movie_map[city].append(movie)
        print('Movie added successfully in city!')

    def add_movie_in_list(self, movie):
        if movie not in self.movie_list:
            self.movie_list.append(movie)
            print('Movie added successfully in city!')
            return
        raise Exception('Movie already exist in movie list!')

    def remove_movie_from_city(self, city, movie):
        if city not in self.city_movie_map:
            raise Exception("This city does not exist in Controller!")
        else:
            if movie not in self.city_movie_map[city]:
                raise Exception("This movie does not exist in particular city!")
            self.city_movie_map[city].remove(movie)
            print('Movie removed successfully in city')
            return

    def remove_movie(self, movie):
        if movie not in self.movie_list:
            raise Exception("This movie does not exist in Controller!")
        else:
            self.movie_list.remove(movie)
            print('Movie removed successfully from Controller!')
            return

    def get_movie_from_city(self, city, movie):
        if city not in self.city_movie_map:
            raise Exception("This city does not exist in Controller!")
        else:
            for mov in self.city_movie_map[city]:
                if mov == movie:
                    return mov
            raise Exception("This movie does not exist in particular city!")

    def get_movie(self, movie):
        for mov in self.movie_list:
            if mov == movie:
                return mov
            raise Exception("This movie does not exist in particular city!")
