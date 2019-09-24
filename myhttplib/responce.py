import datetime
import os
import socket

from myhttplib.utils import get_file_size, get_file_extention
from myhttplib.request import Request
from myhttplib.status import HTTPStatusOK, status_resolve, HTTPStatusNotFound
from myhttplib.info import ConnectionHeader, close_field, ServerHeader, ServerName, DateHeader, http_version, NL, \
    contentheader, ContentLengthHeader, ContentTypeHeader, DefaultContentType, HEAD
from myhttplib.status import ClientError
from myhttplib.vars import ROOT_DIR, DEFAULT_FILE, CHUNCK_SIZE


class Responce:
    __slots__ = ['headers', 'path', '_req_method', 'title',
                 'code', 'head', '_raw_head', '_head_done',
                 '_file_done', '_file', '_file_size', '_file_extention']
    def __init__(self):
        self.path: str
        self._req_method: str
        self.title: bytes
        self.code: int
        self.head: list
        self._raw_head: bytes

        self._head_done = False
        self._file_done = False

        self._file = None
        self._file_size = None
        self._file_extention = None

        self.code = None
        self.path = None
        self.title = None
        self.headers: list = [
            (ConnectionHeader, close_field),
            (ServerHeader, ServerName),
            (DateHeader, datetime.datetime.now()),
        ]
        self.head = []
        self._raw_head = b''

    def handle_file(self, path: str) -> None:
        self._file_size = get_file_size(path)
        extention = get_file_extention(path)
        if extention in contentheader:
            self._file_extention = extention

        if self._req_method == HEAD:
            self._file_done = True
            return

        self._file = open(path, 'rb')

    def build(self, request: Request):
        try:
            request.build()

        except ClientError as err:
            self.code = err.code
        else:
            self.path = request.path
            self._req_method = request.method
            self.code = HTTPStatusOK

        if self.code == HTTPStatusOK:
            self.handle_file(self.path)

        title = bytes(f'HTTP/{http_version} {self.code} {status_resolve[self.code]}', encoding='utf8')
        self.head.append(title)
        # TODO mb None
        if self.code == HTTPStatusOK:
            self.headers.append((ContentLengthHeader, self._file_size))
            if self._file_extention is None:
                self.headers.append((ContentTypeHeader, DefaultContentType))
            else:
                self.headers.append((ContentTypeHeader, contentheader[self._file_extention]))

        for row in self.headers:
            header, value = row
            self.head.append(bytes(f'{header}: {value}', encoding='utf8'))

        self.head.append(NL)
        self._raw_head = NL.join(self.head)

    def send(self, conn: socket.socket) -> bool:
        if not self._head_done:
            conn.send(self._raw_head)
            self._head_done = True
            return False

        if not (self._file is None) and not self._file_done:
            piece = self._file.read(CHUNCK_SIZE)
            if not piece:
                self._file.close()
            else:
                conn.send(piece)
                return False

        return True


