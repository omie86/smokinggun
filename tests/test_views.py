"""Unit tests for Flask application views module.
"""


from unittest import TestCase, main

import mailgunpi


class ViewsTestCase(TestCase):
    def setUp(self):
        mailgunpi.app.config['TESTING'] = True
        self.app = mailgunpi.app.test_client()

    def tearDown(self):
        pass

    def test_root_view(self):
        """Test that root '/' returns page"""
        response = self.app.get('/')
        assert 'Mailgun P.I.' in response.data

    def test_root_view_has_query_form(self):
        """Test that root '/' contains query form"""
        response = self.app.get('/')

        assert 'form-mailgun-query' in response.data


if __name__ == '__main__':
    main()
