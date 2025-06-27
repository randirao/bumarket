from fastapi import HTTPException

from service.jwt_util import decode_access_token
import data.users as data


def makeSeller(access_token, seller):
    if not access_token or not decode_access_token(access_token)['is_admin']:
        raise HTTPException(status_code=401, detail="Invalid access token")

    return data.make_seller(seller)


def getSellers(access_token):
    if not access_token or not decode_access_token(access_token)['is_admin']:
        raise HTTPException(status_code=401, detail="Invalid access token")

    return data.get_all_sellers()