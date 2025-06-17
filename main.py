import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from error import BumarketException
from web import admin


app = FastAPI()
app.include_router(admin.router)

@app.exception_handler(BumarketException)
def bumarket_exception_handeler(request: Request, exc: BumarketException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.msg
        }
    )


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000)