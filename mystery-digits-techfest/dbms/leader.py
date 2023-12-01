import sqlite3
import random

LEADERBOARD_DATABASE_NAME = 'leaderboard.db'

def insert_all_leaderboard(data: list) -> None:
    """
    Insert a list of records into the 'leaderboard' table.

    Args:
        data: List of tuples containing records to be inserted.

    Returns:
        None
    """
    conn = sqlite3.connect(LEADERBOARD_DATABASE_NAME)
    c = conn.cursor()
    if len(data)>10:
        data.remove(data[-1])
    c.executemany("INSERT INTO leaderboard (rank, name, email, level, time, pic) VALUES (?, ?, ?, ?, ?, ?)", data)

    conn.commit()
    conn.close()

def reset_leaderboard() -> None:
    """
    Reset the leaderboard database to the initial state.

    This function drops the existing 'leaderboard' table and recreates it.

    Returns:
        None
    """
    conn = sqlite3.connect(LEADERBOARD_DATABASE_NAME)
    c = conn.cursor()

    print("[WARNING!] You need admin privilege to clear and reset the data! Are you sure? (y/n/yes/no)")
    a = "y"
    c.execute("DROP TABLE IF EXISTS leaderboard")
    if a in ("y", "yes"):
        c.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                    (rank INTEGER ,
                     name TEXT DEFAULT NULL,
                     email TEXT PPRIMARY KEY,
                     level INTEGER DEFAULT 1,
                     time INTEGER DEFAULT 0,
                     pic TEXT DEFAULT NULL
                     )''')

    conn.commit()
    conn.close()

def insert_leaderboard(rank: int, name: str, email: str, level: int, time: int, pic: str) -> None:
    """
    Insert a record into the 'leaderboard' table.

    Args:
        rank: Player's rank.
        name: Player's name.
        email: Player's email (unique identifier).
        level: Player's level.
        time: Player's time.
        pic: Player's picture path.

    Returns:
        None
    """
    conn = sqlite3.connect(LEADERBOARD_DATABASE_NAME)
    c = conn.cursor()

    # Convert level to a single element list for compatibility

    c.execute("INSERT INTO leaderboard (rank, name, email, level, time, pic) VALUES (?, ?, ?, ?, ?, ?)",
            (rank, name, email, level, time, pic))


    conn.commit()
    conn.close()

def update_leaderboard(email: str, level=None, time=None, pic=None) -> None:
    """
    Update a record in the 'leaderboard' table based on the provided email.

    Args:
        email: Player's email (unique identifier).
        level: Updated level (if provided).
        time: Updated time (if provided).
        pic: Updated picture path (if provided).

    Returns:
        None
    """
    conn = sqlite3.connect(LEADERBOARD_DATABASE_NAME)
    c = conn.cursor()

    update_query = "UPDATE leaderboard SET "
    update_values = []

    if level is not None:
        update_query += "level=?, "
        update_values.append(level)

    if time is not None:
        update_query += "time=?, "
        update_values.append(time)

    if pic is not None:
        update_query += "pic=?, "
        update_values.append(pic)

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

def get_all_leaders() -> list:
    """
    Get all leaders from the 'leaderboard' table based on a specific criteria.

    Returns:
        list: All leaders as a list of tuples.
    """
    conn = sqlite3.connect(LEADERBOARD_DATABASE_NAME)
    c = conn.cursor()

    # Example: Fetching leaders based on the highest level
    c.execute("SELECT * FROM leaderboard ORDER BY level DESC")
    leaders = c.fetchall()

    conn.close()

    return leaders


def read_user(email: str) -> list:
    """
    Read details of a user from the 'leaderboard' table based on the provided email.

    Args:
        email: Player's email (unique identifier).

    Returns:
        list: Details of the user as a list of tuples, or 0 if the user doesn't exist.
    """
    conn = sqlite3.connect(LEADERBOARD_DATABASE_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM leaderboard WHERE email=?", (email,))
    result = c.fetchall()

    conn.close()

    if not result:
        return False
    else:
        return result


