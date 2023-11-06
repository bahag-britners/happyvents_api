
from datetime import date
from datetime import datetime
from models import Event, Comment, EventLike, CommentLike, User
from flask import current_app, g


class Repository():
    def get_db(self):
        if 'db' not in g:
            g.db = current_app.config['pSQL_pool'].getconn()
        return g.db
    
    def events_get_all(self):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute("select eventid, title, description, address, image, event_date, likes, price from events order by title")
            event_records = ps_cursor.fetchall()
            #print(event_records)
            event_list = []
            for row in event_records:
                event_list.append(Event(row[0], row[1], row[2], row[3], row[4],row[5].isoformat(),row[6],row[7]))
            ps_cursor.close()
            return event_list
    
    
    def event_get_by_id(self, id):
        conn = self.get_db()
        if conn:
            ps_cursor = conn.cursor()
            ps_cursor.execute("select eventid, title, description, address, image, event_date, likes, price FROM events WHERE eventid = %s", (id,))
            event_record = ps_cursor.fetchone()
            ps_cursor.close()
        
        if event_record:
            event = Event(event_record[0], event_record[1], event_record[2], event_record[3], event_record[4], event_record[5].isoformat(), event_record[6], event_record[7])
            return event
        else:
            return None
            
    # need to test after adding the event
    def event_add(self, data):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(
                "INSERT INTO events(title, description, address, image, event_date, likes, price) VALUES (%s, %s, %s,%s, %s, %s, %s) RETURNING eventid",
                (data['title'], data['description'], data['address'], '', datetime.strptime(data['event_date'], "%Y-%m-%d"), 0, data['price']))
            
            conn.commit()
            id = ps_cursor.fetchone()[0]
            ps_cursor.close()
            event = Event(id, data['title'], data['description'], data['address'], '', '', 0, 0)
            return event
                            
    def event_update(self, data):
        conn = self.get_db()
        if conn:
            ps_cursor = conn.cursor()
            event_id = data.get('eventid')
            ps_cursor.execute("UPDATE events SET title= %s, description=%s, address=%s, event_date=%s, price=%s WHERE eventid = %s",
                            (data.get('title'), data.get('description'), data.get('address'), datetime.strptime(data.get('event_date'), "%Y-%m-%d"), data.get('price'), event_id))
            conn.commit()
            ps_cursor.close()
            return Event(event_id, data['title'], data['description'], data['address'], data['image'], data['event_date'], data['likes'], data['price'])

    def event_delete(self, id):
        conn = self.get_db()
        if conn:
            ps_cursor = conn.cursor()
            ps_cursor.execute("SELECT eventid FROM events WHERE eventid = %s", (id,))
            existing_event = ps_cursor.fetchone()

            if existing_event:
                ps_cursor.execute("DELETE FROM events WHERE eventid = %s", (id,))
                conn.commit()
                ps_cursor.close()
                return f"Event with ID {id} deleted successfully"
            else:
                return f"Event with ID {id} does not exist"
