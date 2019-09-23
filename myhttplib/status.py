HTTPStatusOK = 200

HTTPStatusBadRequest = 400
HTTPStatusForbidden = 403
HTTPStatusNotFound = 404
HTTPStatusNotAllowed = 405

class ClientError(ValueError):
    code = None

class BadRequestError(ClientError):
    code = HTTPStatusBadRequest

class ForbiddenError(ClientError):
    code = HTTPStatusForbidden

class NotFoundError(ClientError):
    code = HTTPStatusNotFound

class NotAllowedError(ClientError):
    code = HTTPStatusNotAllowed
