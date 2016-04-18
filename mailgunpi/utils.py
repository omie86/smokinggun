"""Module contains utility functions.
"""


import requests

from mailgunpi import app


def get_events(domain_name):
    """Return results from Mailgun API request"""
    domain = "https://api.mailgun.net/v3/{}/events".format(domain_name)
    return requests.get(
        domain,
        auth=("api", app.config["MAILGUN_API_KEY"]),
        params={"begin"       : "Sun, 3 Apr 2016 09:00:00 -0000",
                "ascending"   : "yes",
                "limit"       :  25,
                "pretty"      : "yes"})
