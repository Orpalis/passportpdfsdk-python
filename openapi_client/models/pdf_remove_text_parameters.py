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


class PdfRemoveTextParameters(object):
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
        'file_id': 'str',
        'page_range': 'str',
        'remove_only_hidden_text': 'bool'
    }

    attribute_map = {
        'file_id': 'FileId',
        'page_range': 'PageRange',
        'remove_only_hidden_text': 'RemoveOnlyHiddenText'
    }

    def __init__(self, file_id=None, page_range=None, remove_only_hidden_text=False, local_vars_configuration=None):  # noqa: E501
        """PdfRemoveTextParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._page_range = None
        self._remove_only_hidden_text = None
        self.discriminator = None

        self.file_id = file_id
        self.page_range = page_range
        if remove_only_hidden_text is not None:
            self.remove_only_hidden_text = remove_only_hidden_text

    @property
    def file_id(self):
        """Gets the file_id of this PdfRemoveTextParameters.  # noqa: E501

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :return: The file_id of this PdfRemoveTextParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this PdfRemoveTextParameters.

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :param file_id: The file_id of this PdfRemoveTextParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def page_range(self):
        """Gets the page_range of this PdfRemoveTextParameters.  # noqa: E501

        Specifies the page or the page range whose text shall be removed.  # noqa: E501

        :return: The page_range of this PdfRemoveTextParameters.  # noqa: E501
        :rtype: str
        """
        return self._page_range

    @page_range.setter
    def page_range(self, page_range):
        """Sets the page_range of this PdfRemoveTextParameters.

        Specifies the page or the page range whose text shall be removed.  # noqa: E501

        :param page_range: The page_range of this PdfRemoveTextParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and page_range is None:  # noqa: E501
            raise ValueError("Invalid value for `page_range`, must not be `None`")  # noqa: E501

        self._page_range = page_range

    @property
    def remove_only_hidden_text(self):
        """Gets the remove_only_hidden_text of this PdfRemoveTextParameters.  # noqa: E501

        Specifies whether only hidden text shall be removed.  # noqa: E501

        :return: The remove_only_hidden_text of this PdfRemoveTextParameters.  # noqa: E501
        :rtype: bool
        """
        return self._remove_only_hidden_text

    @remove_only_hidden_text.setter
    def remove_only_hidden_text(self, remove_only_hidden_text):
        """Sets the remove_only_hidden_text of this PdfRemoveTextParameters.

        Specifies whether only hidden text shall be removed.  # noqa: E501

        :param remove_only_hidden_text: The remove_only_hidden_text of this PdfRemoveTextParameters.  # noqa: E501
        :type: bool
        """

        self._remove_only_hidden_text = remove_only_hidden_text

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
        if not isinstance(other, PdfRemoveTextParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PdfRemoveTextParameters):
            return True

        return self.to_dict() != other.to_dict()
