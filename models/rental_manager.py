from rental import Rental

class RentalManager:
    def __init__(self):
        self.rentals = []

    def rent_movie(self, movie, customer):
        if movie.is_available:
            rental = Rental(movie, customer)  
            movie.rent_movie() 
            customer.rented_movies.append(movie) 
            self.rentals.append(rental)
            return f"{customer.name} rented '{movie.title}'."
        return f"'{movie.title}' is not available."

    def return_movie(self, movie, customer):
        for rental in self.rentals:
            if rental.movie == movie and rental.customer == customer and not rental.returned:
                rental.mark_returned() 
                movie.return_movie()
                customer.rented_movies.remove(movie) 
                return f"{customer.name} returned '{movie.title}'."
        return f"{customer.name} did not rent '{movie.title}'."
