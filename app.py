from flask import Flask
from flask_restful import Api
from routes import EventList, Event, Health 

BASE_URL = '/api'

app = Flask(__name__)
api = Api(app)

api.add_resource(Health, f'{BASE_URL}')
api.add_resource(Event, f'{BASE_URL}/event', f'{BASE_URL}/events/<event_id>')
api.add_resource(EventList, f'{BASE_URL}/events')

if __name__ == '__main__':
    app.run(debug=True)