from typing import Optional # Optional : None 가능 값
from enum import Enum
from dataclasses import dataclass
from app.models.shared import ResultResp

class PageDirection(Enum):
    NEXT='next'
    PREV='prev'

@dataclass
class Post:
    id: int
    title: str
    body: str
    created_at: int
    published: bool

@dataclass
class PostsResp:
    posts: list[Post]
    err_msg: str | None = None

@dataclass
class CreatePostReq: # Post 생성
    title: str
    body: str
    publish: bool = False

@dataclass
class UpdatePostReq:
    title: Optional[str] = None
    body: Optional[str] = None
    publish: Optional[bool] = None