from fastapi import APIRouter

from app.api.v1.endpoints import auth, clients, invoices, routes

api_router = APIRouter()

api_router.include_router(auth.router, prefix='/auth', tags=['auth'])
api_router.include_router(clients.router, prefix='/clients', tags=['Clients'])
api_router.include_router(routes.router, prefix='/routes', tags=['Routes'])
api_router.include_router(invoices.router, prefix='/invoices', tags=['Invoices'])