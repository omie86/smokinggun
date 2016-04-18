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

    def test_events_endpoint_returns_response(self):
        """Test that mailgun events endpoint returns 200 status code"""
        response = self.app.get(self.base_endpoint)

        self.assertEqual(response.status_code, 200)

    def test_events_endpoint_returns_json_response_for_domain(self):
        """Test that mailgun events endpoint returns for domain"""
        domain = 'wakefield.myenotice.com'

        domain_endpoint = self.base_endpoint + '?domain={}'.format(domain)

        response = self.app.get(domain_endpoint)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.data)
        self.assertEqual(json_response['domain'], domain)


if __name__ == '__main__':
    main()
