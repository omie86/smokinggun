"""Tests for mailgun endpoints.
"""


import json
from unittest import TestCase, main

import mailgunpi


class MailgunEventsEndpointTestCase(TestCase):
    def setUp(self):
        mailgunpi.app.config['TESTING'] = True
        self.app = mailgunpi.app.test_client()
        self.base_endpoint = '/api/v1/mailgun/events'

    def tearDown(self):
        pass

    def test_mailgun_events_endpoint_returns_response(self):
        """Test that mailgun events endpoint returns 200 status code"""
        response = self.app.get(self.base_endpoint)

        self.assertEqual(response.status_code, 200)

    def test_mailgun_events_endpoint_returns_required_fields(self):
        """Test that mailgun events endpoint returns required fields"""
        required_fields = ['status', 'total', 'items']

        response = self.app.get(self.base_endpoint)

        data = json.loads(response.data)

        for field in required_fields:
            self.assertTrue(field in data)

    def test_mailgun_events_domain_endpoint_returns_response(self):
        """Test that mailgun events domain endpoint returns 200 status code"""
        domain = 'wakefield.myenotice.com'

        domain_endpoint = self.base_endpoint + '/{}'.format(domain)

        response = self.app.get(domain_endpoint)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    main()
