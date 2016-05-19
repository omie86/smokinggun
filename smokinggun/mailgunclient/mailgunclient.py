"""Wrapper class around working with the Mailgun API.
"""


import requests

import exceptions


class MailgunClient(object):
    """Class exposing methods to work with the Mailgun API"""
    def __init__(self, api_key=None, base_url=None):
        if not api_key or not base_url:
            raise exceptions.MissingArguments
        self.api_key = api_key
        self.base_url = base_url

    def get_events(self, domain_name, params=None):
        """Return JSON response from API call to Mailgun"""
        response = self._make_api_request(domain_name, params)
        if response.status_code != 200:
            raise exceptions.InvalidMailgunApiRequest

        return response.json()

    def _make_api_request(self, domain_name, params):
        """Make request to Mailgun events endpoint"""
        if not params:
            params = {}

        domain = "{}{}/events".format(self.base_url, domain_name)

        response = requests.get(domain,
            auth=("api", self.api_key),
            params=params)

        return response
