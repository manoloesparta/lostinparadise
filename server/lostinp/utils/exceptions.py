# Mongo Handler
class DocumentNotFound(Exception):
    pass


class DuplicateDocumentId(Exception):
    pass


class CollectionNotSpecified(Exception):
    pass


# Configuration


class InvalidEnvironment(Exception):
    pass


class EnvironmentValueNotFound(Exception):
    pass


# JWT


class InvalidToken(Exception):
    pass


class ClaimNotFound(Exception):
    pass


# Controllers HTTP


class ControllerException(Exception):
    status_code = 100


class BadRequest(ControllerException):
    status_code = 400


class Unauthorized(ControllerException):
    status_code = 401
