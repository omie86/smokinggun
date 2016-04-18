"""Unit test for models module.
"""


from unittest import TestCase, main

from mailgunpi import models


class ModelTestCase(TestCase):
    def setUp(self):
        self.response_model = models.RESPONSE_MODEL

    def tearDown(self):
        pass


    def test_response_model_contains_required_fields(self):
        """Test that response model contains required fields"""
        required_fields = ['status', 'total', 'items', 'domain']

        for field in required_fields:
            self.assertTrue(field in self.response_model)


if __name__ == '__main__':
    main()
