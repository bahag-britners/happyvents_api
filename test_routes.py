import datetime
from models import EventModel, CommentModel, EventLikeModel, UserModel
from unittest.mock import MagicMock
from routes import Health, EventList, Event
from repository import Repository
from flask import request
from app import app

event1 = EventModel(1000, 'Event 1', 'Description 1', 'Address 1', '', '2023-11-24', 0, 50)
event2 = EventModel(1002, 'Event 2', 'Description 2', 'Address 2', '', '2023-11-24', 0, 13)
event3 = EventModel(1003, 'Event 3', 'Description 3', 'Address 3', '', '2023-11-24', 0, 10)

comment1 = CommentModel('Comment 1', 'Event 1', 'User 1','Hello 1', '2023-11-12', 0)
comment2 = CommentModel('Comment 2', 'Event 2', 'User 1','Hello 2', '2023-11-12', 0)
user1 = UserModel('User 1', 'Email 1', 'Password 1')
like1 = EventLikeModel(1, 'User 1')

events = [event1, event2, event3]
comments = [comment1, comment2]


def test_health():
    response = Health().get()
    assert response['hello'] == 'from hell'


def test_get_all_events():
    repo = MagicMock(spec=Repository)
    repo.events_get_all.return_value = events

    response_events = EventList(repo).get()
    
    assert response_events[0]['eventId'] == 1000
    assert response_events[0]['title'] == 'Event 1'


def test_add_new_event():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        req = MagicMock(spec=request)
        event_to_add = EventModel(eventId=4, title='Event 4', description='Description 4', address='Address 4', image='', 
                            event_date='2023-11-25', likes=0, price=11)
        req.json.return_value = event_to_add.__dict__
        repo.event_add.return_value = EventModel(eventId=4, title='Event 4', description='Description 4', address='Address 4', image='', 
                            event_date='2023-11-25', likes=0, price=11)
        
        response_event_added = Event(repo).post(req)

        assert response_event_added['eventId'] == 4
        assert response_event_added['title'] == 'Event 4'
        assert response_event_added['event_date'] == '2023-11-25'


def test_get_event_by_id():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        repo.event_get_by_id.return_value = event1

        response_event = Event(repo).get('1000')
    
        assert response_event['eventId'] == 1000
        assert response_event['title'] == 'Event 1'



def test_update_event():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        req = MagicMock(spec=request)
        event_req_json = EventModel(eventId=1000, title='New Event Name', description='Description 4', address='New Address', image='', 
                            event_date='2023-11-25', likes=0, price=11)
        req.json.return_value = event_req_json.__dict__
        event_updated = EventModel(eventId=1000, title='New Event Name', description='Description 4', address='New Address', image='', 
                            event_date='2023-11-25', likes=0, price=11)
        repo.event_update.return_value = event_updated

        response_updated_event = Event(repo).put(req)
    
        assert response_updated_event['eventId'] == 1000
        assert response_updated_event['title'] == 'New Event Name'
        assert response_updated_event['address'] == 'New Address'
   

def test_delete_event():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        repo.event_delete.return_value = "Event with ID 1002 deleted successfully"

        response = Event(repo).delete("1002")
    
        assert response == "Event with ID 1002 deleted successfully"