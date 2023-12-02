import sqlite3

TIME_DATABASE_NAME = 'time.db'

def create_time_table():
    conn = sqlite3.connect(TIME_DATABASE_NAME)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS time
                 (email TEXT PRIMARY KEY,
                  time_list TEXT DEFAULT NULL)''')

    conn.commit()
    conn.close()

def insert_time(email: str, time_list: list):
    conn = sqlite3.connect(TIME_DATABASE_NAME)
    c = conn.cursor()

    # Convert list to a string representation
    time_list_str = ','.join(map(str, time_list))

    c.execute("INSERT INTO time (email, time_list) VALUES (?, ?) ON CONFLICT(email) DO UPDATE SET time_list=?", (email, time_list_str, time_list_str))

    conn.commit()
    conn.close()

def read_time(email: str):
    conn = sqlite3.connect(TIME_DATABASE_NAME)
    c = conn.cursor()

    c.execute("SELECT time_list FROM time WHERE email=?", (email,))
    result = c.fetchone()

    conn.close()

    if not result:
        return False
    else:
        # Convert the string representation of the list back to a list
        return list(map(float, result[0].split(',')))

def update_time(email: str, time_list: list):
    conn = sqlite3.connect(TIME_DATABASE_NAME)
    c = conn.cursor()

    # Convert list to a string representation
    time_list_str = ','.join(map(str, time_list))

    c.execute("UPDATE time SET time_list=? WHERE email=?", (time_list_str, email))

    conn.commit()
    conn.close()
'''
# Example usage
create_time_table()

# Insert
insert_time('user1@example.com', [10, 15, 20])

# Read
print(read_time('user1@example.com'))

# Update
update_time('user1@example.com', [25, 30, 35])

# Read again
print(read_time('user1@example.com'))'''
