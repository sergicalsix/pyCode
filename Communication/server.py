import selectors
import socket

from datetime import datetime

def _accept(server_socket, mask):
    client_socket, addr = server_socket.accept()
    client_socket.setblocking(False)
    selector.register(client_socket, selectors.EVENT_READ, _handle)

    print('[{}] handle connection, start - {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), client_socket.getpeername()))

def _handle(client_socket, mask):
    data = client_socket.recv(recv_size)
    if data:
        #バイナリー形式でClientに送信
        client_socket.send(b'Reply: ' + data)
    else:
        selector.unregister(client_socket)
        print('[{}] handle connection, end - {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), client_socket.getpeername()))
        client_socket.close()


#グローバルに情報を定義
host = 'localhost'
port = 8080
bind_address = (host, port)
backlog_size = 10
recv_size = 1024
selector = selectors.DefaultSelector()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(bind_address)
    server_socket.listen(backlog_size)
    server_socket.setblocking(False)
    #selectorに登録
    selector.register(server_socket, selectors.EVENT_READ, _accept)

    print('[{}] Server startup'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    #server受信待ち
    try:
        while True:
            events = selector.select()
            for key, mask in events:
                callback = key.data  # callback is accept or handle
                callback(key.fileobj, mask)  # callback function call
    except KeyboardInterrupt:
        print('[{}] Server stop'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

