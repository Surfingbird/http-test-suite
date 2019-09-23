import socket

from myhttplib import ClientError
from myhttplib.request import Request


class Responce:
    def __init__(self):
        pass

    def build(self, request: Request):
        try:
            request.build()

        except ClientError as err:
            pass


    def send(self, conn: socket.socket) -> bool:
        self._send_chunck(conn)

        return True

    def _send_chunck(self, conn: socket.socket):
        conn.send(b'1234567890')