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


class DocumentLoadResponse(object):
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
        'error': 'Error',
        'remaining_tokens': 'int',
        'file_id': 'str',
        'document_format': 'DocumentFormat',
        'page_count': 'int',
        'thumbnail_data': 'str'
    }

    attribute_map = {
        'error': 'Error',
        'remaining_tokens': 'RemainingTokens',
        'file_id': 'FileId',
        'document_format': 'DocumentFormat',
        'page_count': 'PageCount',
        'thumbnail_data': 'ThumbnailData'
    }

    def __init__(self, error=None, remaining_tokens=None, file_id=None, document_format=None, page_count=None, thumbnail_data=None, local_vars_configuration=None):  # noqa: E501
        """DocumentLoadResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._remaining_tokens = None
        self._file_id = None
        self._document_format = None
        self._page_count = None
        self._thumbnail_data = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if remaining_tokens is not None:
            self.remaining_tokens = remaining_tokens
        self.file_id = file_id
        if document_format is not None:
            self.document_format = document_format
        if page_count is not None:
            self.page_count = page_count
        self.thumbnail_data = thumbnail_data

    @property
    def error(self):
        """Gets the error of this DocumentLoadResponse.  # noqa: E501


        :return: The error of this DocumentLoadResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DocumentLoadResponse.


        :param error: The error of this DocumentLoadResponse.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def remaining_tokens(self):
        """Gets the remaining_tokens of this DocumentLoadResponse.  # noqa: E501

        Specifies the number of remaining tokens.  # noqa: E501

        :return: The remaining_tokens of this DocumentLoadResponse.  # noqa: E501
        :rtype: int
        """
        return self._remaining_tokens

    @remaining_tokens.setter
    def remaining_tokens(self, remaining_tokens):
        """Sets the remaining_tokens of this DocumentLoadResponse.

        Specifies the number of remaining tokens.  # noqa: E501

        :param remaining_tokens: The remaining_tokens of this DocumentLoadResponse.  # noqa: E501
        :type: int
        """

        self._remaining_tokens = remaining_tokens

    @property
    def file_id(self):
        """Gets the file_id of this DocumentLoadResponse.  # noqa: E501

        Specifies the file identifier of the loaded document.  # noqa: E501

        :return: The file_id of this DocumentLoadResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this DocumentLoadResponse.

        Specifies the file identifier of the loaded document.  # noqa: E501

        :param file_id: The file_id of this DocumentLoadResponse.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def document_format(self):
        """Gets the document_format of this DocumentLoadResponse.  # noqa: E501


        :return: The document_format of this DocumentLoadResponse.  # noqa: E501
        :rtype: DocumentFormat
        """
        return self._document_format

    @document_format.setter
    def document_format(self, document_format):
        """Sets the document_format of this DocumentLoadResponse.


        :param document_format: The document_format of this DocumentLoadResponse.  # noqa: E501
        :type: DocumentFormat
        """

        self._document_format = document_format

    @property
    def page_count(self):
        """Gets the page_count of this DocumentLoadResponse.  # noqa: E501

        Specifies the number of pages into the loaded document.  # noqa: E501

        :return: The page_count of this DocumentLoadResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this DocumentLoadResponse.

        Specifies the number of pages into the loaded document.  # noqa: E501

        :param page_count: The page_count of this DocumentLoadResponse.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def thumbnail_data(self):
        """Gets the thumbnail_data of this DocumentLoadResponse.  # noqa: E501

        Specifies the data of a thumbnail from the first page of the document, in PNG format. Only applicable if the GetPreview field of the request has been set to true.  # noqa: E501

        :return: The thumbnail_data of this DocumentLoadResponse.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_data

    @thumbnail_data.setter
    def thumbnail_data(self, thumbnail_data):
        """Sets the thumbnail_data of this DocumentLoadResponse.

        Specifies the data of a thumbnail from the first page of the document, in PNG format. Only applicable if the GetPreview field of the request has been set to true.  # noqa: E501

        :param thumbnail_data: The thumbnail_data of this DocumentLoadResponse.  # noqa: E501
        :type: str
        """

        self._thumbnail_data = thumbnail_data

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
        if not isinstance(other, DocumentLoadResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentLoadResponse):
            return True

        return self.to_dict() != other.to_dict()
