from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Route(Base):
    __tablename__ = 'routes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)

    client = relationship('Client', back_populates='routes')
    invoices = relationship(
        'Invoice', back_populates='route', cascade='all, delete-orphan')
