from dataclasses import dataclass

@dataclass # dataclass로 만든다.
# 생성지, 초기화, 출력을 자동으로 해준다.
class User:
    loginId: str
    name: str
    age: int
    email: str

def create_user(user: User): # User 클래스 매개변수로 사용
    pass


db = ['Linux', 'Windows', 'MacOS','Android','Redhat']

def get_product(page: int=1, per_page:int=2) -> list:
    startIndex = (page-1)*per_page
    endIndex = startIndex + per_page
    return db[startIndex:endIndex]
    # int형 2개를 받고 list를 반환형으로 내보낸다.


