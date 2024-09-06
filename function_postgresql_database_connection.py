from psycopg2 import connect, OperationalError

def get_connection():
    conn_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'qweqweqwe',
        'host': 'localhost',
        'port': '5432'
    }

    try:
        conn = connect(**conn_params)
        return conn
    except OperationalError as error:
        print(f"Error connecting to the database: {error}")
        return None
