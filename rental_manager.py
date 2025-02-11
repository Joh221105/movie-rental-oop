from database.database import Database

class RentalManager:
    def __init__(self):
        self.db = Database()

    def add_movie(self, title, genre, movie_type, resolution=None, file_size=None, format=None, available=True):
        self.db.add_movie(title, genre, movie_type, resolution, file_size, format, available)

    def view_movies(self):
        movies = self.db.get_movies()
        if not movies:
            print("\nNo movies available.")
            return

        print("\n" + "="*70)  
        print("Available Movies:\n")
        for movie in movies:
            movie_id, title, genre, available, movie_type, resolution, file_size, format = movie
            status = "Available" if available else "Not Available"

            if movie_type == "Digital":
                extra_info = f"(Resolution: {resolution}, Size: {file_size}GB)"
            else:  # PhysicalMovie
                extra_info = f"(Format: {format})"

            print(f"ID: {movie_id} | {title} ({genre}) - {status} - {movie_type} {extra_info}")
        
        print("="*70)
