from datetime import date

from pydantic import BaseModel


class RouteBase(BaseModel):
    name: str
    date: date
    client_id: int


class RouteCreate(RouteBase):
    pass


class RouteRead(RouteBase):
    id: int

    class Config:
        from_attributes = True


class RouteUpdate(RouteBase):
    pass
