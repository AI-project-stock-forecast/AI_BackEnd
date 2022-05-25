from app.db.mysql_connect import engineconn
from app.models.price import Price
from app.schemas import price

engine = engineconn()
session = engine.sessionmaker()


class CRUDPrice:
    def get_price(self, event_code: str):
        return session.query(Price).filter_by(event_code=event_code).all()

    def create(self, create_price: price.PriceCreate) -> Price:
        created_price = Price(**create_price.dict())
        session.add(created_price)
        session.commit()
        session.refresh(created_price)

        return created_price

    def delete(self, price_id: int):
        found_price = session.query(Price).filter_by(id=price_id).first()
        session.delete(found_price)
        result = session.commit()

        return "deleted"
