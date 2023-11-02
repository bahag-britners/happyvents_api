class Event:
    def __init__(self, title, description, address, image, event_data, likes, price, eventid=-1):
        self.title = title
        self.eventid = eventid
        self.description = description
        self.address = address
        self.image = image
        self.event_data = event_data
        self.likes = likes
        self.price = price


class Comment:
    def __init__(self, content, eventid, userid, timestamp, likes, commentid=-1):
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



class User:
    def __init__(self, userid, user_password, email):
        self.userid = userid
        self.user_password = user_password
        self.email = email