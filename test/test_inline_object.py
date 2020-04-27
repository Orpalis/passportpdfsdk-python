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
from openapi_client.models.inline_object import InlineObject  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineObject(unittest.TestCase):
    """InlineObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_object.InlineObject()  # noqa: E501
        if include_optional :
            return InlineObject(
                file_data = bytes(b'blah'), 
                load_document_parameters = openapi_client.models.load_document_parameters.LoadDocumentParameters(
                    file_name = '0', 
                    content_encoding = 'Identity', 
                    get_preview = True, 
                    thumbnail_width = 56, 
                    thumbnail_height = 56, 
                    thumbnail_background_color = 'rgba(0,0,0,0)', 
                    thumbnail_fit_to_page_size = True, )
            )
        else :
            return InlineObject(
                file_data = bytes(b'blah'),
        )

    def testInlineObject(self):
        """Test InlineObject"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
