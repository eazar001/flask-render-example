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


@app.route('/db_insert')
def db_insert():
    with connect_db_service() as conn:
        cur = conn.cursor()
        cur.execute(
        '''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            Values
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
        conn.commit()
        return 'Basketball Table Successfully Populated'


@app.route('/db_select')
def db_select():
    with connect_db_service() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Basketball")
        records = cur.fetchall()
    
    response_string = "<table>"
    
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += f"<td>{info}</td>"
        response_string += "</tr>"
    
    response_string += "</table>"
    return response_string


@app.route('/db_drop')
def db_drop():
    with connect_db_service() as conn:
        cur = conn.cursor()
        cur.execute("DROP TABLE Basketball")
        cur.commit()
    
    return 'Basketball Table Successfully Dropped'


def connect_db_service():
    connection_url = 'postgresql://eazar001_render_db_user:F6rRZMJ8EfDvOo5nSXP5aEW8PYVZ6LNh@dpg-d47u8rhr0fns73fmtb10-a/eazar001_render_db'
    conn = psycopg2.connect(connection_url)
    return conn
