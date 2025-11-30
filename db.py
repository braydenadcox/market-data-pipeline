import psycopg

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    "dbname": "market_data",
    "user": "postgres",
    "password": "Flipper11!"
}

def get_db_connection():
    return psycopg.connect(**DB_CONFIG)