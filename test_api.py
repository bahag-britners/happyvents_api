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
event1 = Event('Event 1', 'Description 1', 'Location 1', 0, 1)
event2 = Event('Event 2', 'Description 2', 'Location 2', 0, 2)
event3 = Event('Event 3', 'Description 3', 'Location 3', 0, 3)

class ApiTests(TestCase):
    @patch('routes.EventList.get')
    def test_events_get_all(self, test_patch):
        with app.test_client() as client:
            test_patch.return_value = [event1.__dict__, event2.__dict__]

            response = client.get(f'{BASE_URL}/events')

            assert response.status_code == 200
            events = json.loads(response.data)
            assert events[0]['id'] == 1


    @patch('routes.Event.post')
    def test_event_post(self, test_patch):
        with app.test_client() as client:
            req = MagicMock(spec=request)
            data = Event('Event 0', 'Description 0', 'Location 0', 0, 1)
            req.json.return_value = data.__dict__
            test_patch.return_value = req.json.return_value

            response = client.post(f'{BASE_URL}/event')

            assert response.status_code == 200
            events = json.loads(response.data)
            assert events['id'] == 1