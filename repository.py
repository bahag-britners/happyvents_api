from models import Event, Review, Like, User

event1 = Event('Event 1', 'Description 1', 'Location 1', 0, 1)
event2 = Event('Event 2', 'Description 2', 'Location 2', 0, 2)
event3 = Event('Event 3', 'Description 3', 'Location 3', 0, 3)

review1 = Review('Review 1', 1, 1)
review2 = Review('Review 2', 1, 2)
review3 = Review('Review 3', 2, 3)

user1 = User('User 1', 'Password 1', 'Email 1')
user2 = User('User 2', 'Password 2', 'Email 2')

like1 = Like(1, 'User 1')
like2 = Like(1, 'User 2')

events = [event1, event2, event3]
reviews = [review1, review2, review3]


class Repository():
    def events_get_all(self):
        return events
    
    def event_get_by_id(self, id):
        return next((event for event in events if event.id == id), None)
    
    def event_add(self, data):
        new_event = Event(data['title'], data['description'], data['location'], 0, len(events) + 1)
        events.append(new_event)
        return new_event
    
    def event_update(self, data):
        event_to_update = next((event for event in events if event.id == id), None)
        if event_to_update is not None:
            return Event(data['title'], data['description'], data['location'], 0, len(events) + 1)

    def event_delete(self, id):
        event_to_delete = next((event for event in events if event.id == id), None)
        if event_to_delete is not None:
            events.remove(event_to_delete)

    def reviews_get_by_id(self, id):
        return next((r for r in reviews if r.id == id), None)
    
    def review_add(self, data):
        return Review(data['content'], data['eventId'], len(reviews) + 1)
