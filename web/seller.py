from typing import List

from fastapi import APIRouter, Form, File, UploadFile
# from fastapi.params import Depends
from service import seller as product_service

router = APIRouter(prefix="/seller/products")

@router.post("")
def upload_product( #token=Depends(get_current_user),
                   title: str = Form(...),
                   description: str = Form(...),
                   images: List[UploadFile] = File(...)
                   ) :
    product_service.upload_product(title, description, images)
    return {"success": True}