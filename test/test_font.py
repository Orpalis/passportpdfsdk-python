# coding: utf-8

"""
    PassportPDF API

    Another brick in the cloud  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.font import Font  # noqa: E501
from openapi_client.rest import ApiException

class TestFont(unittest.TestCase):
    """Font unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Font
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.font.Font()  # noqa: E501
        if include_optional :
            return Font(
                font_style = 'Regular', 
                family_name = '0'
            )
        else :
            return Font(
        )

    def testFont(self):
        """Test Font"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
