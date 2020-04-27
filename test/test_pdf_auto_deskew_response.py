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
from openapi_client.models.pdf_auto_deskew_response import PdfAutoDeskewResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestPdfAutoDeskewResponse(unittest.TestCase):
    """PdfAutoDeskewResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PdfAutoDeskewResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.pdf_auto_deskew_response.PdfAutoDeskewResponse()  # noqa: E501
        if include_optional :
            return PdfAutoDeskewResponse(
                error = openapi_client.models.error.Error(
                    result_code = 'OK', 
                    ext_result_status = '0', 
                    ext_result_message = '0', 
                    internal_error_id = '0', ), 
                remaining_tokens = 56
            )
        else :
            return PdfAutoDeskewResponse(
        )

    def testPdfAutoDeskewResponse(self):
        """Test PdfAutoDeskewResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
