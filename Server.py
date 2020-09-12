import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

clientsocket, address = s.accept()
print(address,"와 연결에 성공했습니다.")

while True:
    msg = input()
    clientsocket.send(bytes(msg, "utf-8"))