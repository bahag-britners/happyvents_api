from flask_restful import Resource
from repository import Repository
from flask import request

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
        return self.repo.event_add(data).__dict__


    def put(self, req=request):
        data = req.get_json()
        return self.repo.event_update(data).__dict__
    
    
    def delete(self, event_id):
        return self.repo.event_delete(event_id)
    

class EventLike(Resource):
    def __init__(self, repo=repository):
        self.repo = repo


    def put(self, req=request):
        data = req.get_json()
        return self.repo.event_like_and_unlike(data)