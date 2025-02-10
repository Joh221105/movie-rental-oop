import sqlite3

class Database:
    def __init__(self, db_name="movie_rental.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                genre TEXT NOT NULL,
                available INTEGER NOT NULL
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS rentals (
                rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_id INTEGER,
                customer_id INTEGER,
                rental_date TEXT,
                returned INTEGER DEFAULT 0,
                FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
        ''')
        self.conn.commit()

    def add_movie(self, title, genre, available=True):
        self.cursor.execute("INSERT INTO movies (title, genre, available) VALUES (?, ?, ?)", (title, genre, int(available)))
        self.conn.commit()

    def get_movies(self):
        self.cursor.execute("SELECT * FROM movies")
        return self.cursor.fetchall()

    def rent_movie(self, movie_id, customer_id):
        self.cursor.execute("UPDATE movies SET available = 0 WHERE movie_id = ? AND available = 1", (movie_id,))
        if self.cursor.rowcount > 0:
            self.cursor.execute("INSERT INTO rentals (movie_id, customer_id, rental_date) VALUES (?, ?, datetime('now'))", (movie_id, customer_id))
            self.conn.commit()
            return True
        return False

    def return_movie(self, movie_id, customer_id):
        self.cursor.execute("UPDATE rentals SET returned = 1 WHERE movie_id = ? AND customer_id = ? AND returned = 0", (movie_id, customer_id))
        if self.cursor.rowcount > 0:
            self.cursor.execute("UPDATE movies SET available = 1 WHERE movie_id = ?", (movie_id,))
            self.conn.commit()
            return True
        return False

    def close(self):
        self.conn.close()
