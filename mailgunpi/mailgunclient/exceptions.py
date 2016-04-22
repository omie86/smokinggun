"""Module contains custom exceptions for package.
"""


class Error(Exception):
    """Base-class for all exceptions raised by this package"""


class MissingArguments(Error):
    """Missing arguments. Please review documentation."""


class InvalidMailgunApiRequest(Error):
    """Invalid Mailgun API request. Inspect domain name provided."""
