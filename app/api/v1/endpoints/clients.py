from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.core.deps import get_db
from app.core.security import get_current_user
from app.schemas.client import ClientCreate, ClientRead, ClientUpdate

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.post('/', response_model=ClientRead)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return crud.client.create_client(db=db, client_in=client)


@router.get('/', response_model=List[ClientRead])
def list_clients(skip: int = 0, limit: int = 100,
                 db: Session = Depends(get_db)):
    return crud.client.get_clients(db=db, skip=skip, limit=limit)


@router.get('/{client_id}', response_model=ClientRead)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = crud.client.get_client(db=db, client_id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail='Client not found')
    return client


@router.put('/{client_id}', response_model=ClientRead)
def update_client(client_id: int, client_in: ClientUpdate,
                  db: Session = Depends(get_db),):
    return crud.client.update_client(db=db, client_id=client_id,
                                     client_in=client_in)


@router.delete('/{client_id}', response_model=ClientRead)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    return crud.client.delete_client(db=db, client_id=client_id)
