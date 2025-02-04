from enum import Enum # enum 모듈
from socket import *
import re # regex(정규표현식) 모듈
import json
from dataclasses import dataclass

class HttpContentType(Enum):
    TEXT_HTML = 'text/html'
    APPLICATION_JSON = 'application/json'
    IMAGE_PNG = 'image/png'

class HttpMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'

class HttpStatusCode(Enum):
    OK = (200,'OK')
    NOT_FOUND = (404,'Not Found')
    METHOD_NOT_ALLOWED = (405,'Method Not Allowed')
    MOVED = (301, 'Moved Permanently')
    SERVER_ERROR = (500, 'Internal Server Error')

# repr - 자바로 따지자면 toString, 생성자 등을 미리 만들어준다.
@dataclass
class HttpRequest:
    method: HttpMethod
    url: str

DB = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Charlie'},
]

def makeRespHeader(status: HttpStatusCode, contentType: HttpContentType, extra: dict|None = None) -> str:
    resp = f"HTTP/1.1 {status.value[0]} {status.value[1]}\n"
    resp += f"Content-Type: {contentType.value}\n"
    if extra is not None:
        for k,v in extra.items():
            resp += f"{k}: {v}\n"
    resp += '\n'
    return resp

def get_user_from_db():
    return DB

def parseRequest(requests: str) -> HttpRequest | None: # 요청 파싱
    if len(requests) < 1:
        return None
    
    arRequests = requests.split('\n')
    for line in arRequests:
        match = re.search(r'\b(GET|POST|DELETE|PUT|PATCH)\b\s+(.*?)\s+HTTP/1.1', line)
        if match:
            # strMethod = match.group(1)
            # print(strMethod)
            # strPath = match.group(2)

            # HttpRequest 객체를 생성한 뒤, method와 url을 집어넣음
            req = HttpRequest()
            try:
                req.method = HttpMethod(match.group(1))
                req.url = match.group(2)
            except:
                return None
            # req.url = strPath
            return req
    return None

# def handle_req(req: HttpRequest, cSocket):
#     arPath = ['/','/users', '/google.png', '/google'] # 허용 Path
    
def createServer():
    arPath = ['/','/users', '/google.png', '/google'] # 허용 Path
    serverSocket = socket(AF_INET, SOCK_STREAM) # 소켓 instance 생성
    try:
        serverSocket.bind(('localhost', 8080)) # 소켓에 주소&포트 할당
        serverSocket.listen() # 요청 대기
        while True:
            # 요청 정보 얻기
            (cSocket, addr) = serverSocket.accept() # 블로킹 후 요청이 오면 연결 소켓과 주소 반환
            # addr - 클라이언트 포트
            print(addr)

            # 요청 처리
            req = cSocket.recv(1024).decode('utf-8')
            print(req)
            # 1024바이트 버퍼로 수신 ->  utf-8로 디코딩
            # strPath = parseRequest(req) # 요청한 Path
            # print(strPath)
            httpReq = parseRequest(req)
            if httpReq is None:
                # 요청 시 반환된 객체가 없을 경우
                # 405 error(Method Not Allowed) 반환
                resp = 'HTTP/1.1 405 Method Not Allowed\n'
                resp += '\n'
                resp += '<html><body>405 Method Not Allowed</body></html>'
                cSocket.sendall(resp.encode('utf-8'))
                cSocket.shutdown(SHUT_WR)
                continue
            print(f'Path = {httpReq.url}')
            strPath = httpReq.url

            resp = ''
            if strPath not in arPath:
                # resp = 'HTTP/1.1 404 Not Found\n' # 404 에러를 헤더에 작성
                # resp += '\n' # 바디 없음
                resp = makeRespHeader(HttpStatusCode.NOT_FOUND, HttpContentType.TEXT_HTML)
                resp += '<html><body>404 Not Found</body></html>'
            elif strPath == '/users':
                # resp = 'HTTP/1.1 200 OK\n'
                # resp += 'Content-Type: application/json\n'
                # resp +='\n'
                resp = makeRespHeader(HttpStatusCode.OK, HttpContentType.APPLICATION_JSON)
                # 응답 헤더
                resp += json.dumps(get_user_from_db())
                # json으로 변환하여 추가
            elif strPath == '/google.png':
                # resp = 'HTTP/1.1 200 OK\n'
                # resp += 'Content-Type: image/png\n'
                # resp += '\n'
                resp = makeRespHeader(HttpStatusCode.OK, HttpContentType.IMAGE_PNG)
                cSocket.sendall(resp.encode('utf-8'))
                with open('google.png', 'rb') as f: # 바이너리로 읽어들임
                    while chunk := f.read(1024): # 1024 바이트로 쪼갬
                        cSocket.sendall(chunk)
                cSocket.shutdown(SHUT_WR) # 연결 닫기
                continue
            elif strPath == '/google':
                # resp = 'HTTP/1.1 301 Moved Permanently\n'
                # resp += 'Location: http://www.google.com\n'
                # resp += '\n'
                resp = makeRespHeader(HttpStatusCode.MOVED, HttpContentType.TEXT_HTML, {'Location': 'http://www.google.com'})
            else:
                # 응답 전송
                # resp = 'HTTP/1.1 200 OK\n'
                # resp += 'Content-Type: text/html\n'
                # resp += '\n'
                # 응답 헤더
                resp = makeRespHeader(HttpStatusCode.OK, HttpContentType.TEXT_HTML)
                resp += '<html><body>Hello</body></html>'
                # 응답 바디

            cSocket.sendall(resp.encode('utf-8'))
            # 소켓에 응답을 담아 utf-8로 인코딩해서 전송
            # 연결 종료
            cSocket.shutdown(SHUT_WR)
    except KeyboardInterrupt: # 강제 종료 시 서버 닫기
        serverSocket.close()

if __name__ == '__main__': # 메인 함수일때 createServer 실행
    createServer()

# 브라우저 갱신

