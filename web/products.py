import hashlib

import service.products as service

from fastapi import APIRouter
from fastapi.params import Depends
from starlette.requests import Request
from fastapi import HTTPException

products = APIRouter(prefix="/products")

def generate_device_id(request:Request) -> str:
    ip = request.client.host
    user_agent = request.headers.get("User-Agent", "unknown")

    device_id = f"{ip}${user_agent}"
    return hashlib.sha256(device_id.encode()).hexdigest()

@products.post("/{product_id}/like")
def get_product_like(product_id: int, device_hash=Depends(generate_device_id)):
    try:
        return service.toggle_like(product_id, device_hash)
    except Exception as e:
        print(f"[ERROR] toggle_like 실패: {e}")
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

@products.get('')
def get_products_all():
    return service.get_products_all()

@products.get('/{product_id}')
def get_product_by_id(product_id: int, device_hash=Depends(generate_device_id)):
    return service.get_product_by_id(product_id, device_hash)