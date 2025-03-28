from sqlalchemy.orm import Session

from app.models.route import Route
from app.schemas.route import RouteCreate, RouteUpdate


def create_route(db: Session, route_in: RouteCreate):
    db_route = Route(**route_in.dict())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route


def get_routes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Route).offset(skip).limit(limit).all()


def update_route(db: Session, route_id: int, route_in: RouteUpdate):
    db_route = db.query(Route).filter(Route.id == route_id).first()
    if db_route:
        for key, value in route_in.dict(exclude_unset=True).items():
            setattr(db_route, key, value)
        db.commit()
        db.refresh(db_route)
    return db_route


def delete_route(db: Session, route_id: int):
    db_route = db.query(Route).filter(Route.id == route_id).first()
    if db_route:
        db.delete(db_route)
        db.commit()
    return db_route
