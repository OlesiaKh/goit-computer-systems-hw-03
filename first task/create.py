import psycopg2

# Configuration for connecting to the database
db_config = {
    "dbname": "myDB",
    "user": "postgres",
    "password": "131313",
    "host": "localhost"
}

# SQL commands for creating the necessary tables
create_tables_commands = [
    """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (status_id) REFERENCES status(id),
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """
]


def create_tables():
    conn = None
    try:
        # Establishing a connection to the database
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Executing the commands to create the tables
        for command in create_tables_commands:
            cur.execute(command)

        # Saving changes to the database
        conn.commit()

        # Closing the cursor and connection
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    # Calling the function to create the tables
    create_tables()
