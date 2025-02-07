class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = []

    def rent_movie(self, movie):
        if movie.rent_movie():
            self.rented_movies.append(movie)
            return f"{self.name} rented {movie.title}"
        return f"{movie.title} is currently not available."

    def return_movie(self, movie):
        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
            return f"{self.name} returned {movie.title}"
        return f"{self.name} doesn't have {movie.title}"