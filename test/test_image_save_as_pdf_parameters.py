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
from openapi_client.models.image_save_as_pdf_parameters import ImageSaveAsPDFParameters  # noqa: E501
from openapi_client.rest import ApiException

class TestImageSaveAsPDFParameters(unittest.TestCase):
    """ImageSaveAsPDFParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImageSaveAsPDFParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.image_save_as_pdf_parameters.ImageSaveAsPDFParameters()  # noqa: E501
        if include_optional :
            return ImageSaveAsPDFParameters(
                file_id = '0', 
                page_range = '*', 
                conformance = 'Unknown', 
                color_image_compression = 'None', 
                bitonal_image_compression = 'None', 
                enable_color_detection = True, 
                image_quality = 56, 
                downscale_resolution = 56, 
                fast_web_view = True
            )
        else :
            return ImageSaveAsPDFParameters(
                file_id = '0',
        )

    def testImageSaveAsPDFParameters(self):
        """Test ImageSaveAsPDFParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
