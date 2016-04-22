"""Unit tests for the MailgunClient class.
"""


from unittest import TestCase, main

from mailgunpi import mailgunclient
from mailgunpi.mailgunclient import exceptions

import config


class MailgunClientTestCase(TestCase):
    def setUp(self):
        self.api_key = config.MAILGUN_API_KEY
        self.base_url = config.MAILGUN_API_BASE_URL
        self.test_domain = config.MAILGUN_TEST_DOMAIN
        self.mg = mailgunclient.MailgunClient(self.api_key, self.base_url)

    def tearDown(self):
        pass

    def test_mailgun_client_throws_on_init(self):
        """Test exception thrown if missing init arguments"""
        with self.assertRaises(exceptions.MissingArguments):
            mg = mailgunclient.MailgunClient()

    def test_get_events_returns_response(self):
        """Test that get_events method returns JSON response"""
        response = self.mg.get_events(self.test_domain)

        self.assertIsInstance(response, dict)

    def test_get_events_throws_error_if_invalid_request(self):
        """Test that get_events throws exception if invalid API request"""
        invalid_domain = 'fakedomain.myenotice.com'

        with self.assertRaises(exceptions.InvalidMailgunApiRequest):
            self.mg.get_events(invalid_domain)

    def test_make_api_request_returns(self):
        """Test that make_api_request returns response"""
        params = None

        response = self.mg._make_api_request(self.test_domain, params)

        self.assertIsNotNone(response)


if __name__ == '__main__':
    main()
