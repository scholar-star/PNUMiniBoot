from fastapi import FastAPI
from app.handlers import auth_handler
from app.handlers import posts_handler # 디렉토리 안 import python module
# auth_handler.py, posts_handler.py를 가져온다.

app = FastAPI()

app.include_router(auth_handler.router)
app.include_router(posts_handler.router)