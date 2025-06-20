from . import cur, con

def save_product(title, description, file_path):
    sql = """
        INSERT INTO products (user_id, title, description, image_url) VALUES (%s, %s, %s, %s)
    """
    cur.execute(sql, (1,title,description,file_path))
    con.commit()
    return cur.lastrowid

def upload_image(product_id, file_path):
    sql = """INSERT INTO product_images (product_id, image_url) VALUES (%s, %s)"""
    cur.execute(sql, (product_id, file_path))
    con.commit()