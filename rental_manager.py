from database.database import Database

class RentalManager:
    def __init__(self):
        self.db = Database()

    def add_movie(self, title, genre, available=True):
        self.db.add_movie(title, genre, available)

    def view_movies(self):
        movies = self.db.get_movies()
        if not movies:
            print("\nNo movies available.")
            return

        print("\n" + "="*50)  
        print("Available Movies:\n")
        for movie in movies:
            movie_id, title, genre, available = movie
            status = "Available" if available else "Not Available"
            print(f"ID: {movie_id} | {title} ({genre}) - {status}")
        print("="*50)

    def rent_movie(self, movie_id, customer_id):
        success = self.db.rent_movie(movie_id, customer_id)
        if success:
            print("Movie rented successfully.")
        else:
            print("Movie is not available or does not exist.")

    def return_movie(self, movie_id, customer_id):
        success = self.db.return_movie(movie_id, customer_id)
        if success:
            print("Movie returned successfully.")
        else:
            print("Invalid return request.")

