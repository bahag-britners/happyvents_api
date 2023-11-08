from models import Event
from flask import Flask
import psycopg2
from psycopg2 import pool
from repository import Repository
from unittest.mock import MagicMock
import datetime

event1 = Event(
    eventId=1, 
    title='Event 1', 
    description='Description 1', 
    address='Address 1', 
    image='', 
    event_date=datetime.datetime(2023, 12, 25), 
    likes=0, 
    price=5
)
event2 = Event(
    eventId=2, 
    title='Event 2', 
    description='Description 2', 
    address='Address 2', 
    image='', 
    event_date=datetime.datetime(2023, 11, 25), 
    likes=0, 
    price=13.50
)

event3 = Event(
    eventId=3, 
    title='Event 3', 
    description='Description 3', 
    address='Address 3', 
    image='', 
    event_date='2023-11-24', 
    likes=0, 
    price=9.99
)
event3_json = {
    'eventId': event3.eventId,
    'title': event3.title,
    'description': event3.description,
    'address': event3.address,
    'image': event3.image,
    'event_date': event3.event_date,
    'likes': event3.likes,
    'price': event3.price
}

events = [event1, event2]

event_row = [
    (event1.eventId, event1.title, event1.description, event1.address, event1.image, event1.event_date, event1.likes, event1.price),
    (event2.eventId, event2.title, event2.description, event2.address, event2.image, event2.event_date, event2.likes, event2.price),
]


def test_events_get_all():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchall.return_value = event_row
        repo = Repository()
        events = repo.events_get_all()
        assert events[0].title == event1.title
        assert events[1].eventId == event2.eventId


def test_event_get_by_id():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchone.return_value = event_row[0]
        repo = Repository()
        event = repo.event_get_by_id(event1.eventId)
        assert event.title == event1.title
        assert event.eventId == event1.eventId


def test_event_add():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchone.return_value = [event3]
        repo = Repository()
        event = repo.event_add(event3_json)
        assert event.title == event3.title


def test_event_update():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchone.return_value = [event3_json]
        repo = Repository()
        event = repo.event_update(event3_json)
        assert event.eventId == event3.eventId
        assert event.title == event3.title


def test_event_delete():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchone.return_value = f"Event with ID {event3.eventId} deleted successfully"
        repo = Repository()
        res = repo.event_delete(event3.eventId)
        assert res == f"Event with ID {event3.eventId} deleted successfully"