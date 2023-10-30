from flask_restful import Resource


class Health(Resource):
    def get(self):
        return {'hello': 'from hell'}
    

class EventList(Resource):
    def get(self):
        return {'hello': 'from eventlist'}


class Event(Resource):
    def get(self, event_id):
        return {'hello': f'from event {event_id}'}
    
    def post(self):
        return {'hello': 'from event (post)'}
    
    def put(self):
        return {'hello': 'from event (put)'}
    
    def delete(self, event_id):
        return {'hello': f'from event {event_id}'}