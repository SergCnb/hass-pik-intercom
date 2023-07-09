class PikIntercomException(Exception):
    """Base class for exceptions"""


class PikAccessDeniedIntercomException(PikIntercomException):
    """Received access denied (HTTP 403)"""


class MalformedDataError(PikIntercomException, ValueError):
    """Received data is malformed"""


class ServerResponseError(PikIntercomException):
    """Error embedded into server response"""
