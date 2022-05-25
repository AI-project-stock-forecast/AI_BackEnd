from typing import Optional

from pydantic import BaseModel


class EventBase(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None


class EventCreate(EventBase):
    name: str
    code: str


class EventUpdate(EventBase):
    pass


class EventInDBBase(EventBase):
    id: Optional[int]
    name: Optional[str] = None
    code: Optional[str] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Event(EventInDBBase):
    pass
