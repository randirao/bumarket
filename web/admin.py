from fastapi import APIRouter, Body
from starlette.requests import Request
import service.admin as service

SESSION_COOKIE_NAME = "session_id"
admin = APIRouter(prefix='/admin')

@admin.post('/sellers')
def makeSeller(request: Request, seller=Body()):
    access_token = request.cookies.get(SESSION_COOKIE_NAME)
    return service.makeSeller(access_token, seller)

@admin.get('/sellers')
def getSellers(request: Request):
    access_token = request.cookies.get(SESSION_COOKIE_NAME)
    return service.getSellers(access_token)
