
import sqlite3
#Task 1

try:

    with sqlite3.connect("../db/magazines.db") as conn: 
        print("Database Created")
except Exception as e:
    print ("SQL Error",e)

#Task 3
def add_publisher(conn, name):
    try:
        cursor=conn.cursor()

        cursor.execute("SELECT id FROM publishers WHERE name = ?",(name,))

        row = cursor.fetchone()
        if row is not None:
            return row[0]
        
        cursor.execute("INSERT INTO publishers (name) VALUES (?)",(name,))
        return cursor.lastrowid

    except sqlite3.Error as e:
        print("Error adding publisher:", e)

def add_magazine(conn, name, publisher_id):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM magazines WHERE name =?",(name,))

        row = cursor.fetchone()
        if row is not None:
            return row[0]
        
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",(name, publisher_id,))
        return cursor.lastrowid

    except sqlite3.Error as e:
        print("Error adding publisher:", e)


def add_subscriber(conn, name, address):
    try:
        cursor = conn.cursor()

        # Check if subscriber already exists (same name + address)
        cursor.execute("""
            SELECT id FROM subscribers
            WHERE name = ? AND address = ?
        """, (name, address))

        row = cursor.fetchone()
        if row is not None:
            return row[0]

        # Insert new subscriber
        cursor.execute(
            "INSERT INTO subscribers (name, address) VALUES (?, ?)",
            (name, address)
        )
        return cursor.lastrowid

    except sqlite3.Error as e:
        print("Error adding subscriber:", e)
        return None



def add_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try:
        cursor = conn.cursor()

        # Check if subscription already exists
        cursor.execute("""
            SELECT id FROM subscriptions
            WHERE subscriber_id = ? AND magazine_id = ?
        """, (subscriber_id, magazine_id))

        row = cursor.fetchone()
        if row is not None:
            return row[0]

        # Insert new subscription
        cursor.execute("""
            INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
        """, (subscriber_id, magazine_id, expiration_date))

        return cursor.lastrowid

    except sqlite3.Error as e:
        print("Error adding subscription:", e)
        return None

        

#Task 2

def main():
    try:
        with sqlite3.connect("../db/magazines.db") as conn:
            conn.execute("PRAGMA foreign_keys = 1")
            cursor = conn.cursor()

            cursor.executescript("""CREATE TABLE IF NOT EXISTS publishers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                );

                CREATE TABLE IF NOT EXISTS magazines (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    publisher_id INTEGER NOT NULL,
                    FOREIGN KEY (publisher_id) REFERENCES publishers(id)
                );

                CREATE TABLE IF NOT EXISTS subscribers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS subscriptions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subscriber_id INTEGER NOT NULL,
                    magazine_id INTEGER NOT NULL,
                    expiration_date TEXT NOT NULL,
                    FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
                    FOREIGN KEY (magazine_id) REFERENCES magazines(id)
                );
            """)
            print("Database and table created sucessfully.")
    except sqlite3.Error as e:
        print("SQL ERROR: ",e)

#task 3
    try:
        with sqlite3.connect("../db/magazines.db") as conn:
            conn.execute("PRAGMA foreign_keys = 1")

            # Add publishers
            p1 = add_publisher(conn, "Publisher A")
            p2 = add_publisher(conn, "Publisher B")
            p3 = add_publisher(conn, "Publisher C")

            # Add magazines
            m1 = add_magazine(conn, "Magazine One", p1)
            m2 = add_magazine(conn, "Magazine Two", p2)
            m3 = add_magazine(conn, "Magazine Three", p3)

            # Add subscribers
            s1 = add_subscriber(conn, "Alice Smith", "123 Main St")
            s2 = add_subscriber(conn, "Bob Johnson", "456 Oak St")
            s3 = add_subscriber(conn, "Carol Davis", "789 Pine St")

            # Add subscriptions
            add_subscription(conn, s1, m1, "2025-01-01")
            add_subscription(conn, s1, m2, "2025-02-01")
            add_subscription(conn, s2, m1, "2025-03-01")

            conn.commit()
            print("Database populated successfully.")

#Task 4
        cursor.execute("SELECT * FROM subscribers")
        rows = cursor.fetchall()
        print("\n All Subscribers")
        for row in rows:
            print(row)

        cursor.execute("SELECT * FROM magazines ORDER BY name")
        rows = cursor.fetchall()
        print("\nAll Magazines sorted by name")
        for row in rows:
            print(row)

        cursor.execute("""SELECT magazines.* FROM magazines 
                       JOIN publishers ON magazines.publisher_id = publisher_id 
                       WHERE publisher_id =?""",(p1,))
        row = cursor.fetchall()
        print(f"\nMagazines for Publisher ID {p1}:")
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("SQL ERROR: ",e)

if __name__=="__main__":
    main()
