from cache import redis_client

def toggle_like(product_id: int, user_key: str):
    product_key = f"like:{product_id}"
    user_likes_key = f"user_likes:{user_key}"

    if not redis_client.sismember(product_key, user_key):
        redis_client.sadd(product_key, user_key)
        redis_client.sadd(user_likes_key, product_id)
        redis_client.zincrby("like_ranking", 1, product_id)
        return True
    return False

def get_like_score(product_id: int) -> int:
    score = redis_client.zscore("like_ranking", product_id)
    return int(score) if score else 0