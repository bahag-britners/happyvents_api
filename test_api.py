import datetime
from flask import request
import routes
from models import Event
from unittest.mock import patch
from unittest import TestCase
import unittest
from app import app
import json
from unittest.mock import MagicMock

BASE_URL = '/api'
event1 = Event(
    eventId=1, 
    title='Event 1', 
    description='Description 1', 
    address='Address 1', 
    image='', 
    event_date='2023-12-23',
    likes=0, 
    price=5
)
event2 = Event(
    eventId=2, 
    title='Event 2', 
    description='Description 2', 
    address='Address 2', 
    image='', 
    event_date='2023-11-25',
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
events = [event1, event2, event3]

class ApiTests(TestCase):
    @patch('routes.EventList.get')
    def test_events_get_all(self, test_patch):
        with app.test_client() as client:
            test_patch.return_value = [event1.__dict__, event2.__dict__]

            response = client.get(f'{BASE_URL}/events')

            assert response.status_code == 200
            events = json.loads(response.data)
            assert events[0]['eventId'] == 1


    @patch('routes.Event.get')
    def test_event_get_by_id(self, test_patch):
        with app.test_client() as client:
            test_patch.return_value = event1.__dict__

            response = client.get(f'{BASE_URL}/events/<event_id>')

            assert response.status_code == 200
            event = json.loads(response.data)
            assert event['eventId'] == 1


    @patch('routes.Event.put')
    def test_event_update(self, test_patch):
        with app.test_client() as client:
            test_patch.return_value = event1.__dict__

            response = client.put(f'{BASE_URL}/event')

            assert response.status_code == 200
            event = json.loads(response.data)
            assert event['eventId'] == 1


    @patch('routes.Event.delete')
    def test_event_update(self, test_patch):
        with app.test_client() as client:
            test_patch.return_value = f"Event with ID {event1.eventId} deleted successfully"

            response = client.delete(f'{BASE_URL}/event')

            assert response.status_code == 200
            res = json.loads(response.data)
            assert res == f"Event with ID {event1.eventId} deleted successfully"


    @patch('routes.Event.post')
    def test_event_post(self, test_patch):
        with app.test_client() as client:
            test_patch.return_value = event1.__dict__

            response = client.post(f'{BASE_URL}/event')

            assert response.status_code == 200
            event = json.loads(response.data)
            assert event['eventId'] == 1