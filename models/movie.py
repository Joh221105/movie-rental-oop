class Movie:
    def __init__(self, movie_id, title, genre, available=True):
        self.__movie_id = movie_id
        self.__title = title
        self.__genre = genre
        self.__available = available

    def get_movie_id(self):
        return self.__movie_id

    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    def is_available(self):
        return self.__available

    def rent_movie(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_movie(self):
        self.__available = True

    def get_details(self):
        return f"{self.__title} ({self.__genre}) - {'Available' if self.__available else 'Not Available'}"


class DigitalMovie(Movie):
    def __init__(self, movie_id, title, genre, file_size, resolution, available=True):
        super().__init__(movie_id, title, genre, available)
        self.__file_size = file_size
        self.__resolution = resolution

    def get_file_size(self):
        return self.__file_size

    def get_resolution(self):
        return self.__resolution

    def stream_movie(self):
        return f"Streaming {self.get_title()} in {self.__resolution} resolution."

    def get_details(self):
        return f"{super().get_details()} - Digital ({self.__resolution}, {self.__file_size}GB)"


class PhysicalMovie(Movie):
    def __init__(self, movie_id, title, genre, format, available=True):
        super().__init__(movie_id, title, genre, available)
        self.__format = format

    def get_format(self):
        return self.__format

    def get_details(self):
        return f"{super().get_details()} - Physical ({self.__format})"
