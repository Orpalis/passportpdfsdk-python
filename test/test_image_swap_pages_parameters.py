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
from openapi_client.models.image_swap_pages_parameters import ImageSwapPagesParameters  # noqa: E501
from openapi_client.rest import ApiException

class TestImageSwapPagesParameters(unittest.TestCase):
    """ImageSwapPagesParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImageSwapPagesParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.image_swap_pages_parameters.ImageSwapPagesParameters()  # noqa: E501
        if include_optional :
            return ImageSwapPagesParameters(
                file_id = '0', 
                page1 = 56, 
                page2 = 56
            )
        else :
            return ImageSwapPagesParameters(
                file_id = '0',
                page1 = 56,
                page2 = 56,
        )

    def testImageSwapPagesParameters(self):
        """Test ImageSwapPagesParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
