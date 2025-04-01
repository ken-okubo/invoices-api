from pydantic import BaseModel


class InvoiceBase(BaseModel):
    amount: float
    route_id: int


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceUpdate(InvoiceBase):
    pass


class InvoiceRead(InvoiceBase):
    id: int

    class Config:
        from_attributes = True
