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


class PdfDetectPageOrientationParameters(object):
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
        'language': 'str',
        'automatically_apply_rotation': 'bool'
    }

    attribute_map = {
        'file_id': 'FileId',
        'page_range': 'PageRange',
        'language': 'Language',
        'automatically_apply_rotation': 'AutomaticallyApplyRotation'
    }

    def __init__(self, file_id=None, page_range=None, language='eng', automatically_apply_rotation=True, local_vars_configuration=None):  # noqa: E501
        """PdfDetectPageOrientationParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._page_range = None
        self._language = None
        self._automatically_apply_rotation = None
        self.discriminator = None

        self.file_id = file_id
        self.page_range = page_range
        self.language = language
        if automatically_apply_rotation is not None:
            self.automatically_apply_rotation = automatically_apply_rotation

    @property
    def file_id(self):
        """Gets the file_id of this PdfDetectPageOrientationParameters.  # noqa: E501

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :return: The file_id of this PdfDetectPageOrientationParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this PdfDetectPageOrientationParameters.

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :param file_id: The file_id of this PdfDetectPageOrientationParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def page_range(self):
        """Gets the page_range of this PdfDetectPageOrientationParameters.  # noqa: E501

        Specifies the number of the page, or the range of pages to be processed.  # noqa: E501

        :return: The page_range of this PdfDetectPageOrientationParameters.  # noqa: E501
        :rtype: str
        """
        return self._page_range

    @page_range.setter
    def page_range(self, page_range):
        """Sets the page_range of this PdfDetectPageOrientationParameters.

        Specifies the number of the page, or the range of pages to be processed.  # noqa: E501

        :param page_range: The page_range of this PdfDetectPageOrientationParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and page_range is None:  # noqa: E501
            raise ValueError("Invalid value for `page_range`, must not be `None`")  # noqa: E501

        self._page_range = page_range

    @property
    def language(self):
        """Gets the language of this PdfDetectPageOrientationParameters.  # noqa: E501

        Specifies the language to be used for the detection.  # noqa: E501

        :return: The language of this PdfDetectPageOrientationParameters.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PdfDetectPageOrientationParameters.

        Specifies the language to be used for the detection.  # noqa: E501

        :param language: The language of this PdfDetectPageOrientationParameters.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def automatically_apply_rotation(self):
        """Gets the automatically_apply_rotation of this PdfDetectPageOrientationParameters.  # noqa: E501

        Specifies whether a rotation shall be automatically applied in order to correct the page orientation when needed.  # noqa: E501

        :return: The automatically_apply_rotation of this PdfDetectPageOrientationParameters.  # noqa: E501
        :rtype: bool
        """
        return self._automatically_apply_rotation

    @automatically_apply_rotation.setter
    def automatically_apply_rotation(self, automatically_apply_rotation):
        """Sets the automatically_apply_rotation of this PdfDetectPageOrientationParameters.

        Specifies whether a rotation shall be automatically applied in order to correct the page orientation when needed.  # noqa: E501

        :param automatically_apply_rotation: The automatically_apply_rotation of this PdfDetectPageOrientationParameters.  # noqa: E501
        :type: bool
        """

        self._automatically_apply_rotation = automatically_apply_rotation

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
        if not isinstance(other, PdfDetectPageOrientationParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PdfDetectPageOrientationParameters):
            return True

        return self.to_dict() != other.to_dict()
