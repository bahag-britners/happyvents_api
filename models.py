class EventModel:
    def __init__(self, eventId, title, description, address, image, event_date, likes, price, userId):
        self.title = title
        self.eventId = eventId
        self.description = description
        self.address = address
        self.image = image
        self.event_date = event_date
        self.likes = likes
        self.price = price
        self.userId = userId


class CommentModel:
    def __init__(self, commentId, eventId, content, timestamp, likes, userId):
        self.content = content
        self.eventId = eventId
        self.userId = userId
        self.timestamp = timestamp
        self.commentId = commentId
        self.likes = likes


class EventLikeModel:
    def __init__(self, eventId, userId):
        self.eventId = eventId
        self.userId = userId


class CommentLikeModel:
    def __init__(self, eventId, commentId, userId):
        self.eventId = eventId
        self.userId = userId
        self.commentId = commentId


class UserModel:
    def __init__(self, userId, userEmail, userImage):
        self.userId = userId
        self.userEmail = userEmail
        self.userImage = userImage