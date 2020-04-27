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
from openapi_client.models.pdf_insert_image_parameters import PdfInsertImageParameters  # noqa: E501
from openapi_client.rest import ApiException

class TestPdfInsertImageParameters(unittest.TestCase):
    """PdfInsertImageParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PdfInsertImageParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.pdf_insert_image_parameters.PdfInsertImageParameters()  # noqa: E501
        if include_optional :
            return PdfInsertImageParameters(
                file_id = '0', 
                page_range = '0', 
                image_data = 'YQ==', 
                image_file_id = '0', 
                quality = 56, 
                color_image_compression = 'None', 
                bitonal_compression = 'None'
            )
        else :
            return PdfInsertImageParameters(
                file_id = '0',
                page_range = '0',
        )

    def testPdfInsertImageParameters(self):
        """Test PdfInsertImageParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
