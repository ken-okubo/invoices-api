from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Client(Base):
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cnpj_cpf = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    
    routes = relationship('Route', back_populates='client', cascade='all, delete-orphan')
