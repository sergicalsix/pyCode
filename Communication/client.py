import selectors
import socket
import sys

def _write(client_socket, mask):
    #serverに送信
    client_socket.send(message.encode('utf-8'))
    #serverからのReplyを受信
    selector.modify(client_socket, selectors.EVENT_READ, _read)

def _read(client_socket, mask):
    #serverからのReplyを受信
    data = client_socket.recv(recv_size)
    selector.unregister(client_socket)
    #ここがReplyの内容
    print(data.decode('utf-8'))
    client_socket.close()
    received = True

#グローバルに情報を定義
host = 'localhost'
port = 8080
server_address = (host, port)

if len(sys.argv) == 1:
    message = "\n  usage: $python client.py 'Hello World!' "
else:
    message = sys.argv[1]
    if len(sys.argv) > 2:
        for s in sys.argv[2:]:
            message += ' ' + s

recv_size = 1024
selector = selectors.DefaultSelector()
received = False


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(server_address)
    client_socket.setblocking(False)
    selector.register(client_socket, selectors.EVENT_WRITE, _write)

    while not received:
        events = selector.select(0.1)

        if not events:
            break
        
        for key, mask in events:
            callback = key.data 
            callback(key.fileobj, mask) 