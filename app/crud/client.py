from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate


def create_client(db: Session, client_in: ClientCreate) -> Client:
    db_client = Client(**client_in.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Client).offset(skip).limit(limit).all()


def update_client(db: Session, client_id: int, client_in: ClientUpdate):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail='Client not found')
    
    for field, value in client_in.dict(exclude_unset=True).items():
        setattr(client, field, value)
    
    db.commit()
    db.refresh(client)
    return client


def delete_client(db: Session, client_id: int):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, details='Client not found')
    
    db.delete(client)
    db.commit()
    return client
