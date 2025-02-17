class Customer:
    def __init__(self, customer_id, name):
        self.__customer_id = customer_id
        self.__name = name
        self.__rented_movies = []

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_rented_movies(self):
        return self.__rented_movies

    def rent_movie(self, movie):
        self.__rented_movies.append(movie)

    def return_movie(self, movie):
        self.__rented_movies.remove(movie)
