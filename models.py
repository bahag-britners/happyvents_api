class Event:
    def __init__(self, eventid, title, description, address, image, event_data, likes, price):
        self.title = title
        self.eventid = eventid
        self.description = description
        self.address = address
        self.image = image
        self.event_data = event_data
        self.likes = likes
        self.price = price


class Comment:
    def __init__(self, commentid, eventid, userid, content, timestamp, likes):
        self.content = content
        self.eventid = eventid
        self.userid = userid
        self.timestamp = timestamp
        self.commentid = commentid
        self.likes = likes


class EventLike:
    def __init__(self, eventid, userid):
        self.eventId = eventid
        self.userId = userid


class CommentLike:
    def __init__(self, eventid, userid, commentid):
        self.eventId = eventid
        self.userId = userid
        self.commentId = commentid


class User:
    def __init__(self, userid, email, user_password):
        self.userid = userid
        self.user_password = user_password
        self.email = email