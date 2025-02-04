from fastapi import APIRouter # 라우터
from app.models.user import *

router = APIRouter(
    prefix="/v1/auth" # 앞에 /auth가 있다고 상정.
)


@router.post("/signup", status_code=201) # 회원 가입
def signup(user: User) -> AuthResponse:
    return AuthResponse(
        jwt_token="asdfjk;l"
    )

@router.post("/signin") # 로그인
def signin(user: AuthLoginReq):
    return AuthResponse(
        jwt_token="aaaa"
    )