from psycopg2 import connect

def get_connection():
    conn_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'qweqweqwe',
        'host': 'localhost',
        'port': '5432'
    }
    
    try:
        with connect(**conn_params) as conn:
            return conn
            # Connection is automatically closed when exiting this block
    except Exception as error:
        print(f"Error connecting to the database: {error}")

# Example usage:
get_connection()
