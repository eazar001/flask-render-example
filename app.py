from flask import Flask
import psycopg2


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World from Ebrahim in 3308'


@app.route('/db_test')
def db_test():
    connection_url = 'postgresql://eazar001_render_db_user:F6rRZMJ8EfDvOo5nSXP5aEW8PYVZ6LNh@dpg-d47u8rhr0fns73fmtb10-a/eazar001_render_db'
    with psycopg2.connect(connection_url) as conn:
        return 'Database Connection Successful'
