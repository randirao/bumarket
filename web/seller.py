from typing import List
from fastapi import APIRouter, UploadFile
from fastapi.params import File, Form
from starlette.requests import Request
from service import products as product_service

SESSION_COOKIE_NAME = "session_id"
seller = APIRouter(prefix="/seller")

@seller.post('/products')
def add_product(
        request: Request,
        images: List[UploadFile] = File(..., description="Product images", alias="images"),
    title: str = Form(..., alias="title"),
    description: str = Form(..., alias="description")
):
    access_token = request.cookies.get(SESSION_COOKIE_NAME)
    product_service.add_product(access_token, title, description, images)
    return {'message': 'Product added'}

@seller.get('/products/my')
def get_my_products(request: Request):
    access_token = request.cookies.get(SESSION_COOKIE_NAME)
    return product_service.get_products_by_userid(access_token)

@seller.patch('/products/{product_id}')
def update_product(request: Request, product_id: int, title: str = Form(...), description: str = Form(...), images: List[UploadFile] = File(...)):
    access_token = request.cookies.get(SESSION_COOKIE_NAME)
    product_service.update_products(access_token, product_id, title, description, images)
    return {"message": "Product updated"}

@seller.delete('/products/{product_id}')
def delete_product(request: Request, product_id: int):
    access_token = request.cookies.get(SESSION_COOKIE_NAME)
    product_service.delete_product(access_token, product_id)
    return {"message": "Product deleted"}
