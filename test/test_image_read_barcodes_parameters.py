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
from openapi_client.models.image_read_barcodes_parameters import ImageReadBarcodesParameters  # noqa: E501
from openapi_client.rest import ApiException

class TestImageReadBarcodesParameters(unittest.TestCase):
    """ImageReadBarcodesParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImageReadBarcodesParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.image_read_barcodes_parameters.ImageReadBarcodesParameters()  # noqa: E501
        if include_optional :
            return ImageReadBarcodesParameters(
                file_id = '0', 
                page_range = '0', 
                roi_left = 56, 
                roi_top = 56, 
                roi_width = 56, 
                roi_height = 56, 
                scan_mode = 'FavorSpeed', 
                scan_barcode1_d = True, 
                scan_barcode_qr = True, 
                scan_barcode_micro_qr = True, 
                scan_barcode_pdf417 = True, 
                scan_barcode_data_matrix = True, 
                scan_barcode_aztec = True
            )
        else :
            return ImageReadBarcodesParameters(
                file_id = '0',
                page_range = '0',
        )

    def testImageReadBarcodesParameters(self):
        """Test ImageReadBarcodesParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
