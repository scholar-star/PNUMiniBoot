from dataclasses import dataclass

@dataclass
class User:
    login_id: str
    password: str
    name: str

@dataclass
class AuthLoginReq:
    login_id: str
    password: str

@dataclass
class AuthResponse: # 인증결과
    jwt_token: str | None = None
    err_msg: str | None = None