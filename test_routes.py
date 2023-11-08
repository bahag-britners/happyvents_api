from models import Event, Comment, Like, User
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

review1 = Comment('Review 1', 1, 1)
review2 = Comment('Review 2', 1, 2)
review3 = Comment('Review 3', 2, 3)

user1 = User('User 1', 'Password 1', 'Email 1')
user2 = User('User 2', 'Password 2', 'Email 2')

like1 = Like(1, 'User 1')
like2 = Like(1, 'User 2')

events = [event1, event2, event3]
reviews = [review1, review2, review3]