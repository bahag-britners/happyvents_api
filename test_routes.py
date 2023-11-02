from models import Event, Comment, Like, User

event1 = Event('Event 1', 'Description 1', 'Location 1', 0, 1)
event2 = Event('Event 2', 'Description 2', 'Location 2', 0, 2)
event3 = Event('Event 3', 'Description 3', 'Location 3', 0, 3)

review1 = Comment('Review 1', 1, 1)
review2 = Comment('Review 2', 1, 2)
review3 = Comment('Review 3', 2, 3)

user1 = User('User 1', 'Password 1', 'Email 1')
user2 = User('User 2', 'Password 2', 'Email 2')

like1 = Like(1, 'User 1')
like2 = Like(1, 'User 2')

events = [event1, event2, event3]
reviews = [review1, review2, review3]