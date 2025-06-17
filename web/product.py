import hashlib

from fastapi import APIRouter, Depends
from starlette.requests import Request

import service

router = APIRouter(prefix="/products")

def generate_device_id(request: Request) -> str:
    ip = request.client.host
    user_agent = request.headers.get("User-Agent",
                                     "unknown")
    device_id = f"{ip}${user_agent}"
    return (hashlib.sha256(device_id.encode()).hexdigest())


@router.post("/{product_id}/like")
def get_product_like(product_id: int,
                     device_hash=Depends(generate_device_id)):
    return (
        service.toggle_like(product_id, device_hash))