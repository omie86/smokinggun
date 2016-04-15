"""Tests for mailgun endpoints.
"""


import json
from unittest import TestCase, main

import mailgunpi


class MailgunEventsEndpointTestCase(TestCase):
    def setUp(self):
        mailgunpi.app.config['TESTING'] = True
        self.app = mailgunpi.app.test_client()
        self.endpoint = '/api/v1/mailgun/events'

    def tearDown(self):
        pass

    def test_mailgun_events_endpoint_returns_response(self):
        """Test that mailgun events endpoint returns 200 status code"""
        response = self.app.get(self.endpoint)

        self.assertEqual(response.status_code, 200)

    def test_mailgun_events_endpoint_returns_required_fields(self):
        """Test that mailgun events endpoint returns required fields"""
        required_fields = ['status', 'total', 'items']

        response = self.app.get(self.endpoint)

        data = json.loads(response.data)

        for field in required_fields:
            self.assertTrue(field in data)
