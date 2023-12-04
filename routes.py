from flask_restful import Resource
from models import EventModel
from repository import Repository
from flask import request

from verify_token import retrieve_user

repository = Repository()
class Health(Resource):
    def get(self):
        return {'hello': 'from hell'}
    
class EventListByTitle(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def get(self, title):
        return [event.__dict__ for event 
                in self.repo.events_get_by_title(title)]


class EventList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def get(self):
        return [e.__dict__ for e in self.repo.events_get_all()]
    

class CreatedEventList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def get(self, req=request):
        user = retrieve_user(req)
        if user is None:
            return {'error': 'Unauthorized'}, 401
        else:
            return [e.__dict__ for e in self.repo.events_get_created(user.userId)]
    

class LikedEventList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def get(self, req=request):
        user = retrieve_user(req)
        if user is None:
            return {'error': 'Unauthorized'}, 401
        else:
            return [e.__dict__ for e in self.repo.events_get_liked(user.userId)]


class Event(Resource):
    def __init__(self, repo=repository):
        self.repo = repo


    def get(self, event_id):
        event = self.repo.event_get_by_id(event_id)
        if event is None:
            return {'error': 'Event not found'}, 404
        return event.__dict__
    

    def post(self, req=request):
        data = req.get_json()
        user = retrieve_user(req)
        if user is None:
            return {'error': 'Unauthorized'}, 401
        else:
            return self.repo.event_add(data, user.userId).__dict__


    def put(self, req=request):
        data = req.get_json()
        user = retrieve_user(req)
        if user is None:
            return {'error': 'Unauthorized'}, 401
        else:
            val = self.repo.event_update(data, user.userId)
            if isinstance(val, EventModel):
                return val.__dict__
            else:
                return val
    
    
    def delete(self, event_id, req=request):
        user = retrieve_user(req)
        if user is None:
            return {'error': 'Unauthorized'}, 401
        else:
            return self.repo.event_delete(event_id, user.userId)
    

class EventLike(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def put(self, req=request):
        data = req.get_json()
        user = retrieve_user(req)
        if user is None:
            return {'error': 'Unauthorized'}, 401
        else:
            return self.repo.event_like_and_unlike(data, user.userId)

class Users(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def post(self, req=request):
        user = retrieve_user(req)
        if user is None:
            return {'error': 'Unauthorized'}, 401
        else:
            return self.repo.user_add(user)

class Comment(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
    
    def get(self, event_id):
        return [c.__dict__ for c in self.repo.comments_get_all(event_id)]

    def post(self, event_id, req=request):
        data = req.get_json()
        user = retrieve_user(req)
        if user is None:
            return {'error': 'Unauthorized'}, 401
        else:
            return self.repo.comment_add(event_id, data, user.userId).__dict__

    def delete(self, comment_id, req=request):
        user = retrieve_user(req)
        if user is None:
            return {'error': 'Unauthorized'}, 401
        else:
            return self.repo.comment_delete(comment_id, user.userId)

class CommentLike(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def put(self, event_id, req=request):
        data = req.get_json()
        user = retrieve_user(req)
        if user is None:
            return {'error': 'Unauthorized'}, 401
        else:
            return self.repo.comment_like_and_unlike(event_id, data, user.userId)
        