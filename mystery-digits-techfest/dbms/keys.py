import sqlite3
import random

DATABASE_NAME = 'keys.db'

def reset_back_to_start() -> None:
    """
    Reset the database to the initial state.

    This function drops the existing 'keys' table and recreates it.

    Returns:
        None
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    print("[WARNING!] You need admin privilege to clear and reset the data! Are you sure? (y/n/yes/no)")
    a = input()
    c.execute("DROP TABLE IF EXISTS keys")
    if a in ("y", "yes"):
        c.execute('''CREATE TABLE IF NOT EXISTS keys
                    (id INTEGER PRIMARY KEY,
                     value TEXT NOT NULL
                     )''')

    conn.commit()
    conn.close()

def insert_keys(keys: list) -> None:
    """
    Insert a list of keys into the 'keys' table.

    Args:
        keys: List of keys to insert.

    Returns:
        None
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    for key in keys:
        c.execute("INSERT INTO keys (value) VALUES (?)", (key,))

    conn.commit()
    conn.close()

def read_keys() -> list:
    """
    Read all keys from the 'keys' table.

    Returns:
        list: Keys as a list of strings.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM keys")
    result = c.fetchall()

    keys_list = [row[1] for row in result]

    conn.close()

    return keys_list

# Additional function to generate UID
def generate_uid() -> int:
    """
    Generate a random 6-digit UID.

    Returns:
        int: Randomly generated UID.
    """
    return random.randint(100000, 999999)

# Additional function to insert a single key
def insert_key(value: str) -> None:
    """
    Insert a single key into the 'keys' table.

    Args:
        value: Key value.

    Returns:
        None
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    c.execute("INSERT INTO keys (value) VALUES (?)", (value,))

    conn.commit()
    conn.close()

