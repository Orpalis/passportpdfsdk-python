# coding: utf-8

"""
    PassportPDF API

    Another brick in the cloud  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Barcode1DSymbology(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NONE = "None"
    INDUSTRIAL2OF5 = "Industrial2of5"
    INVERTED2OF5 = "Inverted2of5"
    INTERLEAVED2OF5 = "Interleaved2of5"
    IATA2OF5 = "Iata2of5"
    MATRIX2OF5 = "Matrix2of5"
    CODE39 = "Code39"
    CODEABAR = "Codeabar"
    BCDMATRIX = "BcdMatrix"
    DATALOGIC2OF5 = "DataLogic2of5"
    CODE128 = "Code128"
    CODE93 = "CODE93"
    EAN13 = "EAN13"
    UPCA = "UPCA"
    EAN8 = "EAN8"
    UPCE = "UPCE"
    ADD5 = "ADD5"
    ADD2 = "ADD2"

    allowable_values = [NONE, INDUSTRIAL2OF5, INVERTED2OF5, INTERLEAVED2OF5, IATA2OF5, MATRIX2OF5, CODE39, CODEABAR, BCDMATRIX, DATALOGIC2OF5, CODE128, CODE93, EAN13, UPCA, EAN8, UPCE, ADD5, ADD2]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """Barcode1DSymbology - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Barcode1DSymbology):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Barcode1DSymbology):
            return True

        return self.to_dict() != other.to_dict()
