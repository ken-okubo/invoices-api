from sqlalchemy.orm import Session
from app.models.invoice import Invoice
from app.models.route import Route
from datetime import date


def generate_invoice_from_route(db: Session, route_id: int) -> Invoice:
    route = db.query(Route).filter(Route.id == route_id).first()
    if not route:
        return None

    new_invoice = Invoice(
        amount=100.0,
        date=date.today(),
        route_id=route_id
    )
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    return new_invoice
