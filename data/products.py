from data import con, cur

def add_product(user_id, title, description, image_url):
    query = f"INSERT INTO products (user_id, title, description, image_url) VALUES ('{user_id}', '{title}', '{description}', '{image_url}')"
    cur.execute(query)
    con.commit()

    product_id = cur.lastrowid

    print(product_id)
    return product_id

def upload_image(product_id, image_url):
    query = f"INSERT INTO product_images (product_id, image_url) VALUES ('{product_id}', '{image_url}')"
    cur.execute(query)
    con.commit()

def get_products_by_userid(user_id):
    query = f"SELECT product_id, title, COUNT(like_id) as likes_count FROM products NATURAL LEFT JOIN likes WHERE user_id={user_id} GROUP BY product_id, title"
    cur.execute(query)
    products = cur.fetchall()
    return products

def update_products(product_id, user_id, title, description, image_url):
    query = f"UPDATE products SET title='{title}', description='{description}', image_url='{image_url}' WHERE product_id='{product_id}' and user_id={user_id}"
    cur.execute(query)
    con.commit()

def delete_product(product_id, user_id):
    check_query = f"SELECT COUNT(*) as count FROM products WHERE product_id = {product_id} AND user_id = {user_id}"
    cur.execute(check_query)
    result = cur.fetchone()

    if result['count'] == 0:
        raise ValueError("상품을 찾을 수 없거나 삭제 권한이 없습니다.")
    query = f"DELETE FROM products WHERE product_id='{product_id}' and user_id='{user_id}'"
    cur.execute(query)
    con.commit()

def get_products_all():
    query = "SELECT product_id, title, COUNT(like_id) as likes_count FROM products NATURAL LEFT JOIN likes GROUP BY product_id, title"
    cur.execute(query)
    products = cur.fetchall()
    return products

def get_product_by_id(product_id):
    query = f"SELECT product_id, title, description, image_url, created_at, COUNT(like_id) as like_count FROM products NATURAL LEFT JOIN likes WHERE product_id='{product_id}' GROUP BY  product_id, title, description, image_url, created_at"
    cur.execute(query)
    products = cur.fetchone()
    return products

def get_is_liked(product_id, device_hash):
    query = f"SELECT COUNT(*) as is_liked FROM likes WHERE product_id='{product_id}' AND device_hash='{device_hash}'"
    cur.execute(query)
    is_liked = cur.fetchone()
    return is_liked

def get_images(product_id):
    query = f"SELECT image_url FROM product_images WHERE product_id='{product_id}'"
    cur.execute(query)
    images = cur.fetchall()
    return images
