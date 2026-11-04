import socket
import threading

lock = threading.Lock()
def read_from_server(connection):
    while True:
        data = connection.recv(1000)
        if data:
            with lock:
                print("Сообщение типа: ",data.decode("utf-8"))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",6969))
print("Подключился")

threading.Thread(target=read_from_server,args=(s,)).start()

try:
    while True:
        ass = input()
        s.sendall(ass.encode('utf-8'))
finally:
    s.close()