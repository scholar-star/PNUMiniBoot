from fastapi import APIRouter # 라우터
from app.models.post import *
import time

router = APIRouter(
    prefix="/v1/posts" # 앞에 /posts가 있다고 상정.
)

@router.get("", status_code=201) # 전체 조회
def get_posts(dir: PageDirection = PageDirection.PREV, 
              post_id: int = 0, 
              limit: int = 20):
    return PostsResp(
        posts = [
            Post(
                id=1,
                title="T1",
                body="B1",
                created_at=int(time.time()),
                published=True
            ),
            Post(
                id=2,
                title="T2",
                body="B2",
                created_at=int(time.time()),
                published=True
            )
        ]
    )
    
    
@router.get("/{post_id}") # 전체 조회
def get_posts(post_id: int):
    return PostsResp(
        posts = [
            Post(
                id=post_id,
                title="T1",
                body="B1",
                created_at=int(time.time()),
                published=True
            )
        ]
    )

@router.post("")
def create_post(params: CreatePostReq) -> PostsResp:
    return PostsResp(
        posts = [
            Post(id = 999, title = params.title, body = params.body,
                 created_at=int(time.time()), published=params.publish)
        ]
    )

@router.put("/{post_id}")
def update_post(post_id: int, params: UpdatePostReq) -> PostsResp: # 수정가능 ID, 수정내용을 반영
    return PostsResp(
        posts = [
            Post(id = post_id, title=params.title, body=params.body, 
                 created_at = int(time.time()), published=params.publish)
        ]
    )

@router.delete("/{post_id}")
def delete_post(post_id: int) -> ResultResp:
    return ResultResp(ok=True)