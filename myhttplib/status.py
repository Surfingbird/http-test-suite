HTTPStatusOK = 200

HTTPStatusBadRequest = 400
HTTPStatusForbidden = 403
HTTPStatusNotFound = 404
HTTPStatusNotAllowed = 405

status_resolve = {
    HTTPStatusOK: 'OK',
    HTTPStatusBadRequest:  'Bad Request',
    HTTPStatusForbidden:  'Forbidden',
    HTTPStatusNotFound:  'Not Found',
    HTTPStatusNotAllowed:  'Method Not Allowed',
}

class ClientError(ValueError):
    code = None
    discription = 'clients error'

    def __init__(self, dis=discription):
        print(dis)

class BadRequestError(ClientError):
    code = HTTPStatusBadRequest

class ForbiddenError(ClientError):
    code = HTTPStatusForbidden

class NotFoundError(ClientError):
    code = HTTPStatusNotFound

class NotAllowedError(ClientError):
    code = HTTPStatusNotAllowed
