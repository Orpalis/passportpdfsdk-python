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
from openapi_client.models.pdf_aligned_text_parameters import PdfAlignedTextParameters  # noqa: E501
from openapi_client.rest import ApiException

class TestPdfAlignedTextParameters(unittest.TestCase):
    """PdfAlignedTextParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PdfAlignedTextParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.pdf_aligned_text_parameters.PdfAlignedTextParameters()  # noqa: E501
        if include_optional :
            return PdfAlignedTextParameters(
                text_vertical_alignment = 'Near', 
                text_horizontal_alignment = 'Near', 
                text = '0', 
                text_color = 'black', 
                font_name = '0', 
                standard_font_name = 'Courier', 
                font_style = 'Regular', 
                font_size = 56
            )
        else :
            return PdfAlignedTextParameters(
        )

    def testPdfAlignedTextParameters(self):
        """Test PdfAlignedTextParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
