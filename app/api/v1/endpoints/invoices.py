from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.core.deps import get_db
from app.core.security import get_current_user
from app.schemas.invoice import InvoiceCreate, InvoiceRead, InvoiceUpdate
from app.services.invoice import generate_invoice_from_route

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.post('/', response_model=InvoiceRead)
def create_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return crud.invoice.create_invoice(db=db, invoice_in=invoice)


@router.get('/', response_model=List[InvoiceRead])
def list_invoices(skip: int = 0, limit: int = 100,
                  db: Session = Depends(get_db)):
    return crud.invoice.get_invoices(db=db, skip=skip, limit=limit)


@router.get('/{invoice_id}', response_model=InvoiceRead)
def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = crud.invoice.get_invoice(db=db, invoice_id=invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail='Invoice not found')
    return invoice


@router.put('/{invoice_id}', response_model=InvoiceRead)
def update_invoice(invoice_id: int, invoice: InvoiceUpdate,
                   db: Session = Depends(get_db)):
    return crud.invoice.update_invoice(db=db, invoice_id=invoice_id,
                                       invoice_in=invoice)


@router.delete('/{invoice_id}')
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    return crud.invoice.delete_invoice(db=db, invoice_id=invoice_id)


@router.post('/generate/{route_id}', response_model=InvoiceRead)
def generate_invoice(route_id: int, db: Session = Depends(get_db)):
    invoice = generate_invoice_from_route(
        db=db, route_id=route_id)
    if not invoice:
        raise HTTPException(status_code=404, detail='Route not found')
    return invoice
