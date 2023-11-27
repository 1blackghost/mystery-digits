import sqlite3
import random

DATABASE_NAME = 'users.db'

def reset_back_to_start() -> None:
    """
    Reset the database to the initial state.

    This function drops the existing 'user' table and recreates it.

    Returns:
        None
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    print("[WARNING!] You need admin privilege to clear and reset the data! Are you sure? (y/n/yes/no)")
    a = input()
    c.execute("DROP TABLE IF EXISTS user")
    if a in ("y", "yes"):
        c.execute('''CREATE TABLE IF NOT EXISTS user
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT DEFAULT NULL,
                     phone TEXT DEFAULT NULL,
                     email TEXT,
                     profile_url TEXT DEFAULT NULL,
                     current_level INTEGER DEFAULT 1,
                     tries INTEGER DEFAULT 5
                     )''')

    conn.commit()
    conn.close()

def insert_user(email: str, phone: str = "", username: str = "", profile_url: str = "", current_level: int = 1) -> None:
    """
    Insert a user into the 'user' table.

    Args:
        username: User's username.
        phone: User's phone number (default is an empty string).
        email: User's email (default is an empty string).
        profile_url: URL to the user's profile (default is an empty string).
        current_level: User's current level (default is 1).

    Returns:
        None
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    c.execute("INSERT INTO user (username, phone, email, profile_url, current_level, tries) VALUES (?, ?, ?, ?, ?, ?)",
              (username, phone, email, profile_url, current_level, 5))  # Use the passed current_level, tries default to 5

    conn.commit()
    conn.close()


def read_users() -> list:
    """
    Read all users from the 'user' table.

    Returns:
        list: Users as a list of tuples.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM user")
    result = c.fetchall()

    conn.close()

    return result

def update_user(email: str, username=None, phone=None, profile_url=None, current_level=None, tries=None) -> None:
    """
    Update user information in the 'user' table based on the provided email.

    Args:
        email: User's email (unique identifier).
        username: Updated username (if provided).
        phone: Updated phone number (if provided).
        profile_url: Updated profile URL (if provided).
        current_level: Updated current level (if provided).
        tries: Updated number of tries (if provided).

    Returns:
        None
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    update_query = "UPDATE user SET "
    update_values = []

    if username is not None:
        update_query += "username=?, "
        update_values.append(username)

    if phone is not None:
        update_query += "phone=?, "
        update_values.append(phone)

    if profile_url is not None:
        update_query += "profile_url=?, "
        update_values.append(profile_url)

    if current_level is not None:
        update_query += "current_level=?, "
        update_values.append(current_level)

    if tries is not None:
        update_query += "tries=?, "
        update_values.append(tries)

    # Remove the trailing comma and space
    update_query = update_query.rstrip(", ")

    # Add the WHERE clause to update based on the email
    update_query += " WHERE email=?"

    # Add the email value to the update_values list
    update_values.append(email)

    # Execute the update query
    c.execute(update_query, tuple(update_values))

    conn.commit()
    conn.close()

# Additional function to generate UID
def generate_uid() -> int:
    """
    Generate a random 6-digit UID.

    Returns:
        int: Randomly generated UID.
    """
    return random.randint(100000, 999999)
