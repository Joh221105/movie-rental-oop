import sqlite3

def connect():
    return sqlite3.connect("movie_rental.db")

def create_tables():
    conn = connect()
    cursor = conn.cursor()
    
    # creates movies table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            type TEXT NOT NULL,
            available INTEGER NOT NULL DEFAULT 1,
            file_size REAL,
            resolution TEXT,
            format TEXT
        )
    ''')
    
    # creates customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    
    # creates rentals table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rentals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER,
            customer_id INTEGER,
            rental_date TEXT,
            returned INTEGER DEFAULT 0,
            FOREIGN KEY (movie_id) REFERENCES movies(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )
    ''')
    
    conn.commit()
    conn.close()

# creates tables on app start
create_tables()
