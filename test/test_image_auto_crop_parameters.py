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
from openapi_client.models.image_auto_crop_parameters import ImageAutoCropParameters  # noqa: E501
from openapi_client.rest import ApiException

class TestImageAutoCropParameters(unittest.TestCase):
    """ImageAutoCropParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImageAutoCropParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.image_auto_crop_parameters.ImageAutoCropParameters()  # noqa: E501
        if include_optional :
            return ImageAutoCropParameters(
                file_id = '0', 
                page_range = '0', 
                confidence = 1.337
            )
        else :
            return ImageAutoCropParameters(
                file_id = '0',
                page_range = '0',
        )

    def testImageAutoCropParameters(self):
        """Test ImageAutoCropParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
