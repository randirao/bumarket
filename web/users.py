from fastapi import APIRouter, Body, HTTPException
from starlette import status
from starlette.requests import Request
from starlette.responses import Response
from service.users import getAccessToken
from service import users as service

users = APIRouter()
SESSION_COOKIE_NAME = "session_id"

@users.post("/login", status_code=status.HTTP_200_OK)
def login(response: Response, user = Body()):
    access_token = getAccessToken(user)
    response.set_cookie(
        key=SESSION_COOKIE_NAME,
        value=access_token,
        httponly=True,
        samesite="strict",
        secure=False,
        path="/"
    )

    response.status_code = status.HTTP_200_OK

    return {"message": "success"}

@users.post("/logout")
def logout(response: Response):
    response.delete_cookie(key=SESSION_COOKIE_NAME)
    response.status_code = status.HTTP_200_OK
    return {"message": "success"}

@users.get("/me")
def get_me(request: Request):
    access_token = request.cookies.get(SESSION_COOKIE_NAME)
    return service.token_to_user(access_token)

