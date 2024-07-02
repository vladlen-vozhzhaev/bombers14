import socket
from threading import Thread
import json

HOST = "127.0.0.1"
PORT = 9123
MAX_PLAYERS = 2
serverSocket = socket.socket()
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)
players = []
def handler_client(conn):
    while True:
        try:
            data = conn.recv(1024)
            data = json.loads(data.decode('utf-8'))
            if data["request"] == "get_players":
               conn.sendall(bytes(json.dumps({
                   "response": players
               }), 'utf-8'))
        except:
            pass

while True:
    if len(players) <= MAX_PLAYERS:
        conn, addr = serverSocket.accept()
        print("Подключе клиент с ip", addr)
        Thread(target=handler_client, args=(conn, )).start()

