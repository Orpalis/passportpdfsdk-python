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
from openapi_client.models.image_delete_page_parameters import ImageDeletePageParameters  # noqa: E501
from openapi_client.rest import ApiException

class TestImageDeletePageParameters(unittest.TestCase):
    """ImageDeletePageParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImageDeletePageParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.image_delete_page_parameters.ImageDeletePageParameters()  # noqa: E501
        if include_optional :
            return ImageDeletePageParameters(
                file_id = '0', 
                page_range = '0'
            )
        else :
            return ImageDeletePageParameters(
                file_id = '0',
                page_range = '0',
        )

    def testImageDeletePageParameters(self):
        """Test ImageDeletePageParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
