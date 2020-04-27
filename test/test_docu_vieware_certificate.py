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
from openapi_client.models.docu_vieware_certificate import DocuViewareCertificate  # noqa: E501
from openapi_client.rest import ApiException

class TestDocuViewareCertificate(unittest.TestCase):
    """DocuViewareCertificate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DocuViewareCertificate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.docu_vieware_certificate.DocuViewareCertificate()  # noqa: E501
        if include_optional :
            return DocuViewareCertificate(
                display_name = '0', 
                data = 'YQ==', 
                password = '0', 
                timestamp_server_uri = '0', 
                timestamp_server_user_name = '0', 
                timestamp_server_user_password = '0'
            )
        else :
            return DocuViewareCertificate(
        )

    def testDocuViewareCertificate(self):
        """Test DocuViewareCertificate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
