from sqlalchemy import Column, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.database import Base


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey('routes.id'), nullable=False)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)

    route = relationship('Route', back_populates='invoices')
