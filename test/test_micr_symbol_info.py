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
from openapi_client.models.micr_symbol_info import MICRSymbolInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestMICRSymbolInfo(unittest.TestCase):
    """MICRSymbolInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MICRSymbolInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.micr_symbol_info.MICRSymbolInfo()  # noqa: E501
        if include_optional :
            return MICRSymbolInfo(
                symbol_value = '0', 
                symbol_value2 = '0', 
                top = 56, 
                left = 56, 
                bottom = 56, 
                right = 56, 
                line = 56, 
                confidence = 1.337, 
                confidence2 = 1.337
            )
        else :
            return MICRSymbolInfo(
        )

    def testMICRSymbolInfo(self):
        """Test MICRSymbolInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
