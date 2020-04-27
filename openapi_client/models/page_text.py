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


class PageText(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'page_number': 'int',
        'extracted_text': 'str'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'extracted_text': 'ExtractedText'
    }

    def __init__(self, page_number=None, extracted_text=None, local_vars_configuration=None):  # noqa: E501
        """PageText - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._page_number = None
        self._extracted_text = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        self.extracted_text = extracted_text

    @property
    def page_number(self):
        """Gets the page_number of this PageText.  # noqa: E501

        Specifies the number of the page.  # noqa: E501

        :return: The page_number of this PageText.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this PageText.

        Specifies the number of the page.  # noqa: E501

        :param page_number: The page_number of this PageText.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def extracted_text(self):
        """Gets the extracted_text of this PageText.  # noqa: E501

        The text extraction result.  # noqa: E501

        :return: The extracted_text of this PageText.  # noqa: E501
        :rtype: str
        """
        return self._extracted_text

    @extracted_text.setter
    def extracted_text(self, extracted_text):
        """Sets the extracted_text of this PageText.

        The text extraction result.  # noqa: E501

        :param extracted_text: The extracted_text of this PageText.  # noqa: E501
        :type: str
        """

        self._extracted_text = extracted_text

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
        if not isinstance(other, PageText):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PageText):
            return True

        return self.to_dict() != other.to_dict()
