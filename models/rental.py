from datetime import datetime

class Rental:
    def __init__(self, movie, customer):
        self.movie = movie
        self.customer = customer
        self.rental_date = None
        self.returned = False

    def rent_movie(self):
        if self.movie.is_available:
            self.movie.rent_movie()  
            self.rental_date = datetime.now()
            return f"{self.customer.name} rented '{self.movie.title}' on {self.rental_date.strftime('%Y-%m-%d %H:%M:%S')}."
        return f"'{self.movie.title}' is not available for rent."

    def return_movie(self):
        if not self.returned:
            self.returned = True
            self.movie.return_movie() 
            return f"{self.customer.name} returned '{self.movie.title}'."
        return f"'{self.movie.title}' was already returned."
