import os
import re
from urllib.parse import urlparse
from typing import Union

from myhttplib.status import ForbiddenError, NotFoundError
from myhttplib.vars import config, DEFAULT_FILE


def get_file_length():
    pass

def get_file_size(path) -> int:
    st = os.stat(path)
    return st.st_size

extention_field = 'extention'
pattern = '(?P<extention>\.\w+)$'
extentions_regex = re.compile(pattern)
def get_file_extention(path) -> Union[str, None]:
    m = extentions_regex.search(path)
    if m:
        extention = m.group(extention_field)
        return extention

    return None


def clear_path(raw_path: str) -> str:
    obj = urlparse(raw_path)
    res = obj.path
    is_dir = False

    is_index = False

    if res.find('../') >= 0:
        raise ForbiddenError('You can not look into upper foldiers')

    if res[0] != '/':
        res = '/' + res

    if res[-1] == '/':
        if os.path.isfile(config.ROOT_DIR + res):
            is_dir = False
            raise NotFoundError('file with / simbol')
        else:
            is_dir = True
            is_index = True
            res = res + DEFAULT_FILE

    res = config.ROOT_DIR + res

    if not os.path.exists(res) and not is_dir:
        raise NotFoundError('--')

    if not os.path.exists(res) and is_index:
        raise ForbiddenError('You have not access to this file, no index')

    if not os.access(res, os.R_OK):
        raise ForbiddenError('You have not access to this file')

    return res

