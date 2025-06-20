import os
import shutil
from datetime import datetime
from typing import List

from fastapi import UploadFile

# import data.seller
from data import seller as seller_data
from error import InvalidImageFormatException

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
result = {}

def upload_product( #token=Depends(get_current_user),
                   title: str,
                   description: str,
                   images: List[UploadFile]
                   ) :
    for idx, image in enumerate(images):
        if not image.content_type.startswith("image/"):
            raise InvalidImageFormatException()

        name, ext = os.path.splitext(image.filename)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        save_filename = f"{name}_{timestamp}{ext}"

        file_path = os.path.join(UPLOAD_DIR, save_filename)

        with open(file_path, "wb") as f:
            shutil.copyfileobj(image.file, f)

        # 첫번째라면
        if idx == 0:
            # product 테이블에 값 추가 쿼리
            product_id = seller_data.save_product(title, description, file_path)
            # product_id = data.seller.upload_image(title, description, file_path)
            result["product_id"] = product_id
        # 두 번째 부터는
        else:
            seller_data.upload_image(result["product_id"], file_path)
            # product_image 테이블에 값 추가 쿼리