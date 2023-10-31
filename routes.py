from flask_restful import Resource
from repository import Repository
from flask import request

repo = Repository()
class Health(Resource):
    def get(self):
        return {'hello': 'from hell'}
    

class EventList(Resource):
    def get(self):
        return [e.__dict__ for e in repo.events_get_all()]
    
    def post(self):
        data = request.get_json()
        return repo.event_add(data).__dict__


class Event(Resource):
    def get(self, event_id):
        event = repo.event_get_by_id(event_id)
        if event is None:
            return {'error': 'Event not found'}, 404
        return event.__dict__
    

    def post(self):
        data = request.get_json()
        return repo.event_add(data).__dict__


    def put(self):
        data = request.get_json()
        return repo.event_update(data).__dict__
    
    def delete(self, event_id):
        return repo.event_delete(event_id)