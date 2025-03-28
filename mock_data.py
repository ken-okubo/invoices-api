from datetime import date, timedelta

from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.client import Client
from app.models.invoice import Invoice
from app.models.route import Route

db: Session = SessionLocal()

db.query(Invoice).delete()
db.query(Route).delete()
db.query(Client).delete()
db.commit()

clients = [
    Client(name='Restaurante Sakura', cnpj_cpf='12.345.678/0001-99', email='contato@sakura.com.br'),
    Client(name='Sushi Brasil', cnpj_cpf='98.765.432/0001-11', email='contato@sushibrasil.com'),
    Client(name='Temaki House', cnpj_cpf='11.111.111/0001-22', email='contato@temakihouse.com')
]
db.add_all(clients)
db.commit()

db.refresh(clients[0])
db.refresh(clients[1])
db.refresh(clients[2])

routes = []
for i in range(15):
    client = clients[i % 3]
    route = Route(
        name=f'Route {i+1} - Client {client.name}',
        date=date.today() - timedelta(days=i),
        client_id=client.id
        )
    routes.append(route)

db.add_all(routes)
db.commit()

for r in routes[:5]:
    invoice = Invoice(
        amount=100.0,
        route_id=r.id,
        date=r.date
    )
    db.add(invoice)

db.commit()
db.close()

print('Mock data successfully created')
