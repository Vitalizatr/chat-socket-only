import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost", 6969))

s.listen(5)
connection = None
connections = []
lock = threading.Lock()
def handler_user(connection,):
    while True:
        data = connection.recv(1000)
        if data:
            with lock:
                send_all(connection,data)

def send_all(exception,message):
    for con in connections:
        if con == exception:
            continue
        con.sendall(message)
try:
    i = 0
    while True:
        connection,cl_addres = s.accept()
        if(connection):
            print(f"Появился новый пользователь: {cl_addres}")
            connections.append(connection)
            threading.Thread(target=handler_user,args=(connection,)).start()
            i+=1

finally:
    if connections:
        for connection in connections:
            connection.close()
    s.close()