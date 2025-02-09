class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = []

    def rent_movie(self, movie):
        self.rented_movies.append(movie)

    def return_movie(self, movie):
        self.rented_movies.remove(movie)
