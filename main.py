from fastapi import FastAPI

from web.admin import admin
from web.products import products
from web.users import users
from web.seller import seller

SESSION_COOKIE_NAME = "session_id"
app = FastAPI()
app.include_router(users)
app.include_router(admin)
app.include_router(products)
app.include_router(seller)