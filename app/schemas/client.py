from typing import Optional

from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    name: str
    cnpj_cpf: str
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True


class ClientCreate(ClientBase):
    pass


class ClientRead(ClientBase):
    id: int

    class Config:
        from_attributes = True


class ClientUpdate(ClientBase):
    pass
