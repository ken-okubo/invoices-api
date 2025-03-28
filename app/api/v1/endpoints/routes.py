from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.core.deps import get_db
from app.core.security import get_current_user
from app.schemas.route import RouteCreate, RouteRead, RouteUpdate

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.post('/', response_model=RouteRead)
def create_route(route: RouteCreate, db: Session = Depends(get_db)):
    return crud.route.create_route(db, route)


@router.get('/', response_model=List[RouteRead])
def list_routes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.route.get_routes(db, skip=skip, limit=limit)


@router.put('/{route_id}', response_model=RouteRead)
def update_route(route_id: int, route: RouteUpdate, db: Session = Depends(get_db)):
    return crud.route.update_route(db, route_id, route)


@router.delete('/{route_id}')
def delete_route(route_id: int, db: Session = Depends(get_db)):
    return crud.route.delete_route(db, route_id)
