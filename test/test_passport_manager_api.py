# coding: utf-8

"""
    PassportPDF API

    Another brick in the cloud  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.passport_manager_api import PassportManagerApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPassportManagerApi(unittest.TestCase):
    """PassportManagerApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.passport_manager_api.PassportManagerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_passport_manager_get_passport_info(self):
        """Test case for passport_manager_get_passport_info

        """
        pass


if __name__ == '__main__':
    unittest.main()
