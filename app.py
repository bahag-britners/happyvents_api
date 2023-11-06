from flask import Flask, g
from flask_restful import Api
from routes import EventList, Event, Health
from flask_cors import CORS
import os
from psycopg2 import pool

BASE_URL = os.environ.get("BASE_URL")
HOST = os.environ.get("HOST")#
DATABASE = os.environ.get("DATABASE") #os.environ.get("DATABASE")
DB_PORT = os.environ.get("DB_PORT")# os.environ.get("DB_PORT")
USER = os.environ.get("USER") #os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD") #os.environ.get("PASSWORD")
# env_var = dict(os.environ)
MIN = os.environ.get("MIN")
MAX = os.environ.get("MAX")
DEBUG = os.environ.get("DEBUG")

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['pSQL_pool'] = pool.SimpleConnectionPool(minconn=MIN,
    maxconn=MAX,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=DB_PORT,
    database=DATABASE)

api.add_resource(Health, f'{BASE_URL}')
api.add_resource(Event, f'{BASE_URL}/event', f'{BASE_URL}/events/<event_id>')
api.add_resource(EventList, f'{BASE_URL}/events')

@app.teardown_appcontext
def close_conn(e):
    db = g.pop('db', None)
    if db is not None:
        app.config['pSQL_pool'].putconn(db)
        print('released connection back to pool')

if __name__ == '__main__':
    app.run(debug=DEBUG)