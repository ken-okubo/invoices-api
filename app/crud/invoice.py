from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate, InvoiceUpdate


def create_invoice(db: Session, invoice_in: InvoiceCreate) -> Invoice:
    db_invoice = Invoice(**invoice_in.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


def get_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Invoice).offset(skip).limit(limit).all()


def get_invoice(db: Session, invoice_id: int):
    return db.query(Invoice).filter(Invoice.id == invoice_id).first()


def update_invoice(db: Session, invoice_id: int, invoice_in: InvoiceUpdate):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if invoice:
        for field, value in invoice_in.dict().items():
            setattr(invoice, field, value)
        db.commit()
        db.refresh(invoice)
    return invoice


def delete_invoice(db: Session, invoice_id: int):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if invoice:
        db.delete(invoice)
        db.commit()
    return invoice
