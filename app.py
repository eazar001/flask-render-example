from flask import Flask
import psycopg2


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World from Ebrahim in 3308'


@app.route('/db_test')
def db_test():
    with connect_db_service() as conn:
        return 'Database Connection Successful'


@app.route('/db_create')
def db_create():
    with connect_db_service() as conn:
        cur = conn.cursor()
        cur.execute(
        '''
            CREATE TABLE IF NOT EXISTS Basketball(
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
                );
        ''')
        conn.commit()
        return 'Basketball Table Successfully Created'


def connect_db_service():
    connection_url = 'postgresql://eazar001_render_db_user:F6rRZMJ8EfDvOo5nSXP5aEW8PYVZ6LNh@dpg-d47u8rhr0fns73fmtb10-a/eazar001_render_db'
    conn = psycopg2.connect(connection_url)
    return conn
