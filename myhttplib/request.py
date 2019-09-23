import re
import socket

from myhttplib import NotAllowedError, BadRequestError, validate_path
from myhttplib.info import valid_methods, valid_http_versions

CHUNCK_SIZE = 1024
END = b'\r\n\r\n'
NL = b'\r\n'

method_field = 'method'
path_field = 'path'
version_field = 'version'

title_pattern = b'^(?P<method>[A-Z]+) (?P<path>[/\w]+) HTTP/(?P<version>\d(.\d)?)'

class Request:
    __slots__ = ['_raw_request', 'method', 'path', 'title_regex',
                 'version']
    def __init__(self):
        self._raw_request: bytes
        self.method: str
        self.path : str
        self.version: str

        self._raw_request = b''
        self.method = None
        self.path = None
        self.version = None

        self.title_regex = re.compile(title_pattern)

    def recieve(self, conn: socket.socket) -> bool:
        chunck = self._recv_chunck(conn)
        self._raw_request += chunck

        if not chunck:
            return True
        if self._raw_request.find(END) >= 0:
            return True

        return False

    def _recv_chunck(self, conn: socket.socket) -> bytes:
        return conn.recv(CHUNCK_SIZE)

    def build(self) -> None:
        raw = self._raw_request
        if len(raw.rstrip()) == 0:
            raise BadRequestError()

        head, _ = raw.split(END)
        title, *headers = head.split(NL)
        self._parse_title(title)

    def _parse_title(self, title: bytes) -> None:
        m = self.title_regex.search(title)
        print(title)
        if m:
            method = m.group(method_field)
            if not method in valid_methods:
                raise NotAllowedError()

            # TODO validate path
            path = m.group(path_field)
            if not validate_path(path):
                raise BadRequestError()

            version = m.group(version_field)
            if not version in valid_http_versions:
                raise BadRequestError()

            self.method = method
            self.path = path
            self.version = version

        raise BadRequestError()

