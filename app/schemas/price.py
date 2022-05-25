from typing import Optional

from pydantic import BaseModel


class PriceBase(BaseModel):
    event_code: Optional[str] = None
    date: Optional[str] = None
    average: Optional[str] = None


class PriceCreate(PriceBase):
    event_code: str
    date: str
    average: str


class PriceUpdate(PriceBase):
    pass


class PriceInDBBase(PriceBase):
    id: Optional[int]
    event_code: Optional[str] = None
    date: Optional[str] = None
    average: Optional[str] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Price(PriceInDBBase):
    pass
