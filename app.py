from rental_manager import RentalManager

def display_menu():
    print("\nMovie Rental System")
    print("1. View all movies")
    print("2. Add a movie")
    print("3. Rent a movie")
    print("4. Return a movie")
    print("5. Exit")

def main():
    rental_manager = RentalManager()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            rental_manager.view_movies()

        elif choice == "2":
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            movie_type = input("Enter movie type (Digital/Physical): ").strip().capitalize()

            if movie_type == "Digital":
                resolution = input("Enter resolution (e.g., 1080p, 4K): ")
                file_size = float(input("Enter file size (GB): "))
                rental_manager.add_movie(title, genre, movie_type, resolution=resolution, file_size=file_size)

            elif movie_type == "Physical":
                format = input("Enter format (DVD/Blu-ray/VHS): ")
                rental_manager.add_movie(title, genre, movie_type, format=format)

            else:
                print("Invalid movie type. Please enter either 'Digital' or 'Physical'.")

        elif choice == "3":
            movie_id = int(input("Enter movie ID to rent: "))
            customer_id = int(input("Enter customer ID: "))
            rental_manager.rent_movie(movie_id, customer_id)

        elif choice == "4":
            movie_id = int(input("Enter movie ID to return: "))
            customer_id = int(input("Enter customer ID: "))
            rental_manager.return_movie(movie_id, customer_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
