from rental_manager import RentalManager
from models.movie import DigitalMovie, PhysicalMovie
from models.customer import Customer

def display_menu():
    print("\nMovie Rental System")
    print("1. View all movies")
    print("2. Rent a movie")
    print("3. Return a movie")
    print("4. Exit")

def get_movie_by_id(movie_id, movie_list):
    for movie in movie_list:
        if movie.movie_id == movie_id:
            return movie
    return None

def main():
    rental_manager = RentalManager()

    # dummy movie data
    movie1 = DigitalMovie(1, "Inception", "Sci-Fi", 2.5, "1080p")
    movie2 = PhysicalMovie(2, "The Matrix", "Action", "Blu-ray")
    rental_manager.add_movie(movie1)
    rental_manager.add_movie(movie2)

    # dummy customer data
    customer = Customer(1, "John")

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            rental_manager.view_movies()
        
        elif choice == "2":
            movie_id = int(input("Enter movie ID for rent: "))
            movie = get_movie_by_id(movie_id, rental_manager.movies)
            if movie:
                rental_manager.rent_movie(movie, customer)
            else:
                print("Movie not found.")
        
        elif choice == "3":
            movie_id = int(input("Enter movie ID for return: "))
            movie = get_movie_by_id(movie_id, rental_manager.movies)
            if movie:
                rental_manager.return_movie(movie, customer)
            else:
                print("Movie not found.")
        
        elif choice == "4":
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
