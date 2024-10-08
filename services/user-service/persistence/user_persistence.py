import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    connection = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'localhost'),
        database=os.getenv('POSTGRES_DB', 'user_db'),
        user=os.getenv('POSTGRES_USER', 'user'),
        password=os.getenv('POSTGRES_PASSWORD', 'password')
    )
    return connection

def init_db():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL
            );
        ''')
    conn.commit()
    conn.close()

def add_user(username):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO users (username) VALUES (%s)', (username,))
    conn.commit()
    conn.close()

def find_user(username):
    conn = get_db_connection()
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
    conn.close()
    return user
