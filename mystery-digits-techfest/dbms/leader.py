import sqlite3
import random

LEADERBOARD_DATABASE_NAME = 'leaderboard.db'

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
                    (rank INTEGER PRIMARY KEY,
                     name TEXT DEFAULT NULL,
                     level INTEGER DEFAULT 1,
                     time INTEGER DEFAULT 0,
                     pic TEXT DEFAULT NULL
                     )''')

    conn.commit()
    conn.close()

def insert_leaderboard(rank: int, name: str, level: int, time: int, pic: str) -> None:
    """
    Insert a record into the 'leaderboard' table.

    Args:
        rank: Player's rank.
        name: Player's name.
        level: Player's level.
        time: Player's time.
        pic: Player's picture path.

    Returns:
        None
    """
    conn = sqlite3.connect(LEADERBOARD_DATABASE_NAME)
    c = conn.cursor()

    # Convert level to a single element list for compatibility
    level = [level] if isinstance(level, int) else level

    c.execute("INSERT INTO leaderboard (rank, name, level, time, pic) VALUES (?, ?, ?, ?, ?)",
              (rank, name, str(level), time, pic))  # Convert level to string before insertion

    conn.commit()
    conn.close()

def read_leaderboard() -> list:
    """
    Read all records from the 'leaderboard' table.

    Returns:
        list: Records as a list of tuples.
    """
    conn = sqlite3.connect(LEADERBOARD_DATABASE_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM leaderboard")
    result = c.fetchall()

    conn.close()

    return result

def update_leaderboard(name: str, level=None, time=None, pic=None) -> None:
    """
    Update a record in the 'leaderboard' table based on the provided name.

    Args:
        name: Player's name (unique identifier).
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

    # Add the WHERE clause to update based on the name
    update_query += " WHERE name=?"

    # Add the name value to the update_values list
    update_values.append(name)

    # Execute the update query
    c.execute(update_query, tuple(update_values))

    conn.commit()
    conn.close()

def sortLb(lst: list) -> None:
    """
    Sort the provided list based on the level in descending order,
    update the top 10 records in the leaderboard.

    Args:
        lst: List containing name, level, time, and pic.

    Returns:
        None
    """
    # Extract name, level, time, and pic from the list
    name, level, time, pic = lst

    # Ensure level is a list for consistency
    level = [level] if not isinstance(level, list) else level

    # Check if level has at least one element before sorting
    if len(level) >= 1:
        # Get the current leaderboard records
        current_leaderboard = read_leaderboard()

        # Combine the current records with the new data
        combined_data = current_leaderboard + [(None, name, level, time, pic)]

        try:
            # Sort the combined data based on the level in descending order
            sorted_data = sorted(combined_data, key=lambda x: int(x[2][0]), reverse=True)[:10]

            # Reset leaderboard and insert the top 10 records
            reset_leaderboard()
            for rank, (record_id, name, level, time, pic) in enumerate(sorted_data, start=1):
                insert_leaderboard(rank, name, int(level[0]), time, pic)
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Error: Level should have at least one element.")

# Additional function to generate random time for
