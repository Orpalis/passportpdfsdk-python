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
from openapi_client.models.pdf_init_view_non_full_screen_page_mode import PdfInitViewNonFullScreenPageMode  # noqa: E501
from openapi_client.rest import ApiException

class TestPdfInitViewNonFullScreenPageMode(unittest.TestCase):
    """PdfInitViewNonFullScreenPageMode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PdfInitViewNonFullScreenPageMode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.pdf_init_view_non_full_screen_page_mode.PdfInitViewNonFullScreenPageMode()  # noqa: E501
        if include_optional :
            return PdfInitViewNonFullScreenPageMode(
            )
        else :
            return PdfInitViewNonFullScreenPageMode(
        )

    def testPdfInitViewNonFullScreenPageMode(self):
        """Test PdfInitViewNonFullScreenPageMode"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
