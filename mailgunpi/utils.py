"""Module contains utility functions.
"""


import requests

from mailgunpi import app


def get_events(domain_name, params=None):
    """Return results from Mailgun API request"""
    if not params:
        params = {}

    domain = "https://api.mailgun.net/v3/{}/events".format(domain_name)
    return requests.get(
        domain,
        auth=("api", app.config["MAILGUN_API_KEY"]),
        params=params)
