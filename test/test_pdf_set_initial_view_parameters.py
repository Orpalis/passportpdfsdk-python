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
from openapi_client.models.pdf_set_initial_view_parameters import PdfSetInitialViewParameters  # noqa: E501
from openapi_client.rest import ApiException

class TestPdfSetInitialViewParameters(unittest.TestCase):
    """PdfSetInitialViewParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PdfSetInitialViewParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.pdf_set_initial_view_parameters.PdfSetInitialViewParameters()  # noqa: E501
        if include_optional :
            return PdfSetInitialViewParameters(
                file_id = '0', 
                page_mode = 'None', 
                layout_mode = 'SinglePage', 
                non_full_screen_page_mode = 'None', 
                open_page = 56, 
                open_zoom = 1.337, 
                hide_toolbar = True, 
                hide_menubar = True, 
                hide_window_ui = True, 
                fit_window = True, 
                center_window = True, 
                display_doc_title = True
            )
        else :
            return PdfSetInitialViewParameters(
                file_id = '0',
        )

    def testPdfSetInitialViewParameters(self):
        """Test PdfSetInitialViewParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
