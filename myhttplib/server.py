import socket, select
from typing import Dict

from myhttplib.request import Request
from myhttplib.responce import Responce

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'

# TODO check file discriptor for reading
class Server:
    __slots__ = ['port', '_socket', '_epoll',
                 '_connections', '_requests', '_responses']
    def __init__(self, port: int, _socket):
        self.port = port
        self._socket = _socket

        self._epoll = select.epoll()
        self._epoll.register(self._socket.fileno(), select.EPOLLIN)

        self._connections = {}
        self._requests = {}
        self._responses = {}

    def run(self):
        try:
            while True:
                events = self._epoll.poll(1)
                for fileno, event in events:
                    if fileno == self._socket.fileno():
                        try:
                            connection, address = self._socket.accept()
                            connection.setblocking(0)

                            handler = connection.fileno()
                            self._epoll.register(handler, select.EPOLLIN)
                            self._connections[handler] = connection

                            self._requests[handler] = Request()
                            self._responses[handler] = Responce()
                        except socket.error:
                            pass

                    elif event & select.EPOLLIN:
                        try:
                            conn = self._connections[fileno]
                            done = self._requests[fileno].recieve(conn)
                            if done:
                                self._epoll.modify(fileno, select.EPOLLOUT)
                                request = self._requests[fileno]
                                self._responses[fileno].build(request)
                        except socket.error:
                            pass

                    elif event & select.EPOLLOUT:
                        try:
                            conn = self._connections[fileno]
                            done = self._responses[fileno].send(conn)
                            if done:
                                self._epoll.modify(fileno, 0)
                                self._connections[fileno].shutdown(socket.SHUT_RDWR)
                        except socket.error:
                            pass

                    elif event & select.EPOLLHUP:
                        self._epoll.unregister(fileno)
                        self._connections[fileno].close()
                        del self._connections[fileno]

        finally:
            self._epoll.unregister(self._socket.fileno())
            self._epoll.close()
            self._socket.close()
