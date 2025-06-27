import os
import shutil

import cache.like as like_cache
from service.users import getUserData
from data import products as data


def toggle_like(product_id:int, device_hash:str):
    like_cache.toggle_like(product_id, device_hash)
    score = like_cache.get_like_score(product_id)
    return {
        "product_id": product_id,
        "like_count" : score,
    }


def upload_image(image):
    name, ext= os.path.splitext(image.filename)
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    save_name = f"{name}{timestamp}{ext}"

    image_path = os.path.join("uploads", save_name)

    with open(image_path, "wb") as f:
        shutil.copyfileobj(image.file, f)

    return image_path

def add_product(access_token, title, description, images):
    user = getUserData(access_token)

    product_id = data.add_product(user['user_id'], title, description, upload_image(images[0]))

    for image in images[1:]:
        image_path = upload_image(image)
        data.upload_image(product_id, image_path)

def get_products_by_userid(access_token):
    user = getUserData(access_token)

    products = data.get_products_by_userid(user['user_id'])
    return products

def update_products(access_token, product_id, title, description, images):
    user = getUserData(access_token)
    data.update_products(product_id, user['user_id'], title, description, upload_image(images[0]))

    for image in images[1:]:
        image_path = upload_image(image)
        data.upload_image(product_id, image_path)

def delete_product(access_token, product_id):
    user = getUserData(access_token)
    data.delete_product(product_id, user['user_id'])

def get_products_all():
    return data.get_products_all()


def get_product_by_id(product_id, device_hash):
    product = data.get_product_by_id(product_id)
    is_liked = data.get_is_liked(product_id, device_hash)
    images = data.get_images(product_id)

    return {
        "product_id": product_id,
        "title": product['title'],
        "description": product['description'],
        "images": [
            product['image_url'],
            *[img['image_url'] for img in images]
        ],
        "created_at": product['created_at'],
        "like_count": product['like_count'],
        "is_liked": bool(is_liked['is_liked']),
    }