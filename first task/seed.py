from faker import Faker
import psycopg2
import random

# Initializing the Faker library to create fake data
fake = Faker()

# Database connection settings 
db_config = {
    "dbname": "myDB",
    "user": "postgres",
    "password": "131313",
    "host": "localhost"
}

# Functions to generate random data
def generate_users(n=10):
    """ Creates random records for the users table """
    users = [(fake.name(), fake.unique.email()) for _ in range(n)]
    return users


def generate_statuses():
    """ Creates fixed statuses for the status table """
    statuses = [('new',), ('in progress',), ('completed',)]
    return statuses


def generate_tasks(n=30):
    """ Creates random tasks for the tasks table """
    tasks = []
    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        status_id = random.randint(1, 3)  # Assumes there are 3 records in the status table
        user_id = random.randint(1, 10)  # Assumes there are 10 records in the users table
        tasks.append((title, description, status_id, user_id))
    return tasks


# Function to populate the database with generated data
def populate_database():
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Adding generated users to the users table
        users = generate_users()
        cur.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s)", users)

        # Adding statuses to the status table
        statuses = generate_statuses()
        cur.executemany("INSERT INTO status (name) VALUES (%s)", statuses)

        # Adding tasks to the tasks table
        tasks = generate_tasks()
        cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)

        # Committing the transaction and saving changes
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    # Calling the function to populate the database
    populate_database()

