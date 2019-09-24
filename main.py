import os

from myhttplib import Server, config
import socket

if __name__ == '__main__':
    port = 80

    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    _socket.bind(('0.0.0.0', port))
    _socket.listen(1)
    _socket.setblocking(0)

    print('socket ok')
    # CPU_LIMIT
    for _ in range(1, int(config.CPU_LIMIT)):
        pid = os.fork()
        if pid == 0:
            break

    server = Server(port, _socket)
    print('server created')
    server.run()