from models.rental import Rental

class RentalManager:
    def __init__(self):
        self.rentals = []
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def rent_movie(self, movie, customer):
        if movie.available:
            rental = Rental(movie, customer)
            movie.rent_movie()
            customer.rent_movie(movie)
            self.rentals.append(rental)
            return f"{customer.name} rented '{movie.title}'."
        return f"'{movie.title}' is not available."

    def return_movie(self, movie, customer):
        for rental in self.rentals:
            if rental.movie == movie and rental.customer == customer and not rental.returned:
                rental.return_movie()
                movie.return_movie()
                customer.return_movie(movie)
                return f"{customer.name} returned '{movie.title}'."
        return f"{customer.name} did not rent '{movie.title}'."

    def view_movies(self):
        if not self.movies:
            print("\nNo movies available.")
            return

        print("\n" + "="*50)  
        print("Available Movies:\n")

        for movie in self.movies:
            print(f"ID: {movie.movie_id} | {movie.get_details()}")

        print("="*50)


