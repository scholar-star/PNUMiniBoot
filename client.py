import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))
# 서버 연결

strCmd = '''
GET / HTTP/1.1 Host: localhost:8080
'''.encode() # 바이트 배열로 변환

s.send(strCmd) # 요청 전송

while True:
    resp = s.recv(1024) # 응답 수신
    if not resp or len(resp) < 1:
        break # 응답이 오지 않았으면 break
    print(resp.decode()) # 응답 출력
s.close() # 소켓 닫기