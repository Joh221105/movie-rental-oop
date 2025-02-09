class Movie:
    def __init__(self, movie_id, title, genre, available=True):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.available = available

    def rent_movie(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_movie(self):
        self.available = True

    def get_details(self):
        return f"{self.title} ({self.genre}) - {'Available' if self.available else 'Not Available'}"


class DigitalMovie(Movie):
    def __init__(self, movie_id, title, genre, file_size, resolution, available=True):
        super().__init__(movie_id, title, genre, available)
        self.file_size = file_size  
        self.resolution = resolution  

    def stream_movie(self):
        return f"Streaming {self.title} in {self.resolution} resolution."

    def get_details(self):
        return f"{super().get_details()} - Digital ({self.resolution}, {self.file_size}GB)"


class PhysicalMovie(Movie):
    def __init__(self, movie_id, title, genre, format, available=True):
        super().__init__(movie_id, title, genre, available)
        self.format = format  

    def get_details(self):
        return f"{super().get_details()} - Physical ({self.format})"
