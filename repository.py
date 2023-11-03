
from models import Event, Comment, EventLike, CommentLike, User
import psycopg2

HOST = "104.155.14.105",
DATABASE = "happyvents",
DB_PORT = 5432,
USER = "postgres",
PASSWORD ='happyvent_01'

#event1 = Event('Event 1', 'Description 1', 'Location 1', 0, 1)
#event2 = Event('Event 2', 'Description 2', 'Location 2', 0, 2)
#event3 = Event('Event 3', 'Description 3', 'Location 3', 0, 3)

#review1 = Comment('Review 1', 1, 1)
#review2 = Comment('Review 2', 1, 2)
#review3 = Comment('Review 3', 2, 3)

#user1 = User('User 1', 'Password 1', 'Email 1')
##user2 = User('User 2', 'Password 2', 'Email 2')

#like1 = Like(1, 'User 1')
#like2 = Like(1, 'User 2')

#events = [event1, event2, event3]
#reviews = [review1, review2, review3]


class Repository():
    def get_db(self):
        return psycopg2.connect(
            host= "104.155.14.105",
            database= "happyvents",
            port= 5432,
            user= "postgres",
            password= "happyvent_01")
    
    def events_get_all(self):
        conn = None
        try:
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
        
        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    
    
    def event_get_by_id(self, id):
        conn = None
        try:
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

        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
            
    # need to test after adding the event
    def event_add(self, data):
        conn = None
        try:
            conn = self.get_db()
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute(
                    "INSERT INTO event(title, description, address, image, event_date, likes, price) VALUES (%s, %s, %s,%s, %s, %s, %s) RETURNING eventid",
                    (data['title'], data['description'], data['address'], '', '', 0, 0))
               
                conn.commit()
                id = ps_cursor.fetchone()[0]
                ps_cursor.close()
                event = Event(id, data['title'], data['description'], data['address'], '', '', 0, 0)
                return event

        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                
                
        def event_update(self, data):
            conn = None
            try:
                conn = self.get_db()
                if conn:
                    ps_cursor = conn.cursor()
                    event_id = data.get('eventid')
                    if event_id is not None:
                        ps_cursor.execute("SELECT eventid FROM events WHERE eventid = %s", (id,))
                        existing_event = ps_cursor.fetchone()

                    if existing_event:
                        ps_cursor.execute("UPDATE events SET title= %s, description=%s, address=%s WHERE eventid = %s",
                                      (data.get('title'), data.get('description'), data.get('address'), id))
                        conn.commit()
                        ps_cursor.close()
                        return f"Event with ID {id} updated successfully"
                    else:
                        return f"Event with ID {id} does not exist"

            except Exception as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

        def event_delete(self, id):
            conn = None
            try:
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

            except Exception as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()


    #def reviews_get_by_id(self, id):
       # return next((r for r in reviews if r.id == id), None)
    
    # def review_add(self, data):
    #     return Comment(data['content'], data['eventId'], len(reviews) + 1)
