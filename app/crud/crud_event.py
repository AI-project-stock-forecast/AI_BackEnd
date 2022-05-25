from app.db.mysql_connect import engineconn
from app.models.event import Event
from app.schemas import event

engine = engineconn()
session = engine.sessionmaker()

class CRUDEvent:
    def get_evnet(self, event_name):
        return session.query(Event).filter_by(event_name=event_name).first()

    def create(self, create_event: event.EventCreate):
        created_event = Event(**create_event.dict())
        session.add(created_event)
        session.commit()
        session.refresh(created_event)

        return created_event