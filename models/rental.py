class Rental:
    def __init__(self, movie, customer):
        self.__movie = movie
        self.__customer = customer
        self.__rental_date = None
        self.__returned = False

    def get_movie(self):
        return self.__movie

    def get_customer(self):
        return self.__customer

    def get_rental_date(self):
        return self.__rental_date

    def is_returned(self):
        return self.__returned

    def rent_movie(self):
        if self.__movie.is_available():
            self.__movie.rent_movie()
            self.__rental_date = datetime.now()
            return f"{self.__customer.get_name()} rented '{self.__movie.get_title()}' on {self.__rental_date.strftime('%Y-%m-%d %H:%M:%S')}."
        return f"'{self.__movie.get_title()}' is not available for rent."

    def return_movie(self):
        if not self.__returned:
            self.__returned = True
            self.__movie.return_movie()
            return f"{self.__customer.get_name()} returned '{self.__movie.get_title()}'."
        return f"'{self.__movie.get_title()}' was already returned."
