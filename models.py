class Event:
    def __init__(self, title, description, location, likes, id=-1):
        self.title = title
        self.id = id
        self.description = description
        self.location = location
        self.likes = likes


class Comment:
    def __init__(self, content, event_id, id=-1):
        self.content = content
        self.eventId = event_id
        self.id = id


class Like:
    def __init__(self, event_id, user_id):
        self.eventId = event_id
        self.userId = user_id


class User:
    def __init__(self, user_id, password, email):
        self.userId = user_id
        # self.username = username
        self.password = password
        self.email = email