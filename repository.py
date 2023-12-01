
from datetime import date
from datetime import datetime
from models import EventModel, CommentModel, EventLikeModel, CommentLikeModel, UserModel
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
            ps_cursor.execute("select * from events order by title")
            event_records = ps_cursor.fetchall()
            #print(event_records)
            event_list = []
            for row in event_records:
                event_list.append(EventModel(row[0], row[1], row[2], row[3], row[4],row[5].isoformat(),row[6],row[7], row[8]))
            ps_cursor.close()
            return event_list
        
    def events_get_created(self, userId):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute("SELECT * FROM events WHERE userid = %s ORDER BY title", (userId,))
            event_records = ps_cursor.fetchall()
            event_list = []
            for row in event_records:
                event_list.append(EventModel(row[0], row[1], row[2], row[3], row[4],row[5].isoformat(),row[6],row[7], row[8]))
            ps_cursor.close()
            return event_list
        
    def events_get_liked(self, userId):
        print(userId)
        print(type(userId))
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute("SELECT eventid FROM event_like WHERE userid = %s", (userId,))
            liked_event_records = ps_cursor.fetchall()
            liked_events = []   
            for row in liked_event_records:
                liked_events.append(row[0])
            ps_cursor.execute("SELECT * FROM events WHERE eventid = ANY(%s) ORDER BY title", [liked_events])
            liked_event_records = ps_cursor.fetchall()
            liked_events = [] 
            for row in liked_event_records:
                liked_events.append(EventModel(row[0], row[1], row[2], row[3], row[4],row[5].isoformat(),row[6],row[7], row[8]))
            conn.commit()
            ps_cursor.close()
            return liked_events
    
    def event_get_by_id(self, id):
        conn = self.get_db()
        if conn:
            ps_cursor = conn.cursor()
            ps_cursor.execute("select * FROM events WHERE eventid = %s", (id,))
            event_record = ps_cursor.fetchone()
            ps_cursor.close()
        
        if event_record:
            event = EventModel(event_record[0], event_record[1], event_record[2], event_record[3], event_record[4], event_record[5].isoformat(), event_record[6], event_record[7], event_record[8])
            return event
        else:
            return None
    
    def events_get_by_title(self, title):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute("SELECT * FROM events WHERE title ILIKE %s ORDER BY title", ('%' + title + '%',))
            event_records = ps_cursor.fetchall()
            #print(event_records)
            event_list = []
            for row in event_records:
                event_list.append(EventModel(row[0], row[1], row[2], row[3], row[4],row[5].isoformat(),row[6],row[7], row[8]))
            ps_cursor.close()
            return event_list
            
    # need to test after adding the event
    def event_add(self, data, userId):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(
                "INSERT INTO events(title, description, address, image, event_date, likes, price, userid) VALUES (%s, %s, %s,%s, %s, %s, %s, %s) RETURNING eventid",
                (data['title'], data['description'], data['address'], '', datetime.strptime(data['event_date'], "%Y-%m-%d"), 0, data['price'], userId))
            
            conn.commit()
            id = ps_cursor.fetchone()[0]
            ps_cursor.close()
            event = EventModel(id, data['title'], data['description'], data['address'], '', data['event_date'], 0, data['price'])
            return event
                            
    def event_update(self, data, userId):
        conn = self.get_db()
        if conn:
            ps_cursor = conn.cursor()
            event_id = data.get('eventId')
            ps_cursor.execute("SELECT userid FROM events WHERE eventid = %s", (event_id,))
            event_creator_id = ps_cursor.fetchone()[0]
            print("event creator id: " + event_creator_id)
            print("userId: " + userId)
            if event_creator_id != userId:
                ps_cursor.close()
                return {'error': 'You are not allowed to do this!'}, 401
            else:
                ps_cursor.execute("UPDATE events SET title= %s, description=%s, address=%s, event_date=%s, price=%s WHERE eventid = %s",
                            (data.get('title'), data.get('description'), data.get('address'), datetime.strptime(data.get('event_date'), "%Y-%m-%d"), data.get('price'), event_id))
                conn.commit()
                ps_cursor.close()
                return EventModel(event_id, data['title'], data['description'], data['address'], data['image'], data['event_date'], data['likes'], data['price'])

    def event_delete(self, eventId, userId):
        conn = self.get_db()
        if conn:
            ps_cursor = conn.cursor()
            ps_cursor.execute("SELECT userid FROM events WHERE eventid = %s", (eventId,))
            event_creator_id = ps_cursor.fetchone()

            if event_creator_id is not None and event_creator_id[0] == userId:
                ps_cursor.execute("DELETE FROM events WHERE eventid = %s", (eventId,))
                conn.commit()
                ps_cursor.close()
                return f"Event with ID {eventId} deleted successfully"
            else:
                return f"Event with ID {eventId} cannot be deleted because you are not the creator"
    
    def event_like_and_unlike(self, data, userId):
        conn = self.get_db()
        if conn:
            ps_cursor = conn.cursor()
            ps_cursor.execute("SELECT eventid FROM event_like WHERE eventid = %s AND userid = %s", (data['eventId'], userId))
            liked_event = ps_cursor.fetchone()
            if liked_event is None:
                # like the event
                ps_cursor.execute("INSERT INTO event_like(eventid, userid) VALUES (%s, %s)", (data['eventId'], userId))
                ps_cursor.execute("UPDATE events SET likes = likes + 1 WHERE eventid = %s", (data['eventId'],))
                conn.commit()
                ps_cursor.close()
                return f"Event is liked successfully"
            else:
                # unlike the event
                ps_cursor.execute("DELETE FROM event_like WHERE eventid = %s AND userid = %s", (data['eventId'], userId))
                ps_cursor.execute("UPDATE events SET likes = likes - 1 WHERE eventid = %s", (data['eventId'],))
                conn.commit()
                ps_cursor.close()
                return f"Event is unliked successfully"
    
    def user_add(self, user):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute("SELECT * FROM users WHERE userid = %s", (user.userId,))
            user_exists = ps_cursor.fetchone()
            if user_exists:
                return "User already exists"
            else:
                ps_cursor.execute(
                    "INSERT INTO users(userid, user_email, user_image, user_name) VALUES (%s, %s, %s, %s)",
                    (user.userId, user.userEmail, user.userImage, user.userName))
            conn.commit()
            ps_cursor.close()
            return "User added successfully"

    def comments_get_all(self, eventId):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute("SELECT * FROM comments WHERE eventid = %s ORDER BY timestamp", (eventId,))
            comment_records = ps_cursor.fetchall()
            comment_list = []
            for row in comment_records:
                comment_list.append(CommentModel(row[0], row[1], row[2], row[3].isoformat(), row[4], row[5]))
            ps_cursor.close()
            return comment_list

    def comment_add(self, eventId, data, userId):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            timestamp = datetime.now()
            ps_cursor.execute(
                "INSERT INTO comments(eventid, content, timestamp, userid) VALUES (%s, %s, %s, %s) RETURNING commentid",
                (eventId, data['content'], timestamp, userId))
            conn.commit()
            comment_id = ps_cursor.fetchone()[0]
            ps_cursor.execute("SELECT user_name FROM users WHERE userid = %s", (userId,))
            user_name = ps_cursor.fetchone()[0]
            ps_cursor.close()
            comment = CommentModel(comment_id, eventId, data['content'], timestamp, user_name)
            return comment

    def comment_delete(self, commentId, userId):
        conn = self.get_db()
        if conn:
            ps_cursor = conn.cursor()
            ps_cursor.execute("SELECT userid FROM comments WHERE commentid = %s", (commentId,))
            comment_creator_id = ps_cursor.fetchone()

            if comment_creator_id is not None and comment_creator_id[0] == userId:
                ps_cursor.execute("DELETE FROM comments WHERE commentid = %s", (commentId,))
                conn.commit()
                ps_cursor.close()
                return f"Comment with ID {commentId} deleted successfully"
            else:
                return f"Comment with ID {commentId} cannot be deleted because you are not the creator"

    def comment_like_and_unlike(self, eventId, data, userId):
        conn = self.get_db()
        if conn:
            ps_cursor = conn.cursor()
            ps_cursor.execute("SELECT commentid FROM comment_like WHERE commentid = %s AND userid = %s",
                                (data['commentId'], userId))
            liked_comment = ps_cursor.fetchone()
            if liked_comment is None:
                # like the comment
                ps_cursor.execute("INSERT INTO comment_like(eventid, commentid, userid) VALUES (%s, %s, %s)",
                                    (eventId, data['commentId'], userId))
                ps_cursor.execute("UPDATE comments SET likes = likes + 1 WHERE commentid = %s", (data['commentId'],))
                conn.commit()
                ps_cursor.close()
                return f"Comment is liked successfully"
            else:
                # unlike the comment
                ps_cursor.execute("DELETE FROM comment_like WHERE commentid = %s AND userid = %s",
                                    (data['commentId'], userId))
                ps_cursor.execute("UPDATE comments SET likes = likes - 1 WHERE commentid = %s", (data['commentId'],))
                conn.commit()
                ps_cursor.close()
                return f"Comment is unliked successfully"