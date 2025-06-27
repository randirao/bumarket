from fastapi import HTTPException

from data.users import get_user_by_credentials
from service.jwt_util import create_access_token, decode_access_token
from data import users as data


def getAccessToken(user):
    user_data = get_user_by_credentials(user)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_data['created_at'] = str(user_data['created_at'])
    return create_access_token(user_data)

def getUserData(access_token):
    user_data = decode_access_token(access_token)
    return {
        "user_id": user_data['user_id'],
        "username": user_data['username'],
        "is_admin": user_data['is_admin'],
    }

def token_to_user(token: str):
    payload = decode_access_token(token)

    user = data.find_by_username(payload['username'])
    user['password'] = None
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {key: value for key, value in user.items() if key != 'password'}