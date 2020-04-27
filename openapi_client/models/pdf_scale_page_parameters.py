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


class PdfScalePageParameters(object):
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
        'scale_x': 'float',
        'scale_y': 'float'
    }

    attribute_map = {
        'file_id': 'FileId',
        'page_range': 'PageRange',
        'scale_x': 'ScaleX',
        'scale_y': 'ScaleY'
    }

    def __init__(self, file_id=None, page_range=None, scale_x=None, scale_y=None, local_vars_configuration=None):  # noqa: E501
        """PdfScalePageParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._page_range = None
        self._scale_x = None
        self._scale_y = None
        self.discriminator = None

        self.file_id = file_id
        self.page_range = page_range
        self.scale_x = scale_x
        self.scale_y = scale_y

    @property
    def file_id(self):
        """Gets the file_id of this PdfScalePageParameters.  # noqa: E501

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :return: The file_id of this PdfScalePageParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this PdfScalePageParameters.

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :param file_id: The file_id of this PdfScalePageParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def page_range(self):
        """Gets the page_range of this PdfScalePageParameters.  # noqa: E501

        Specifies the number of the page, or the range of pages which shall be scaled.  # noqa: E501

        :return: The page_range of this PdfScalePageParameters.  # noqa: E501
        :rtype: str
        """
        return self._page_range

    @page_range.setter
    def page_range(self, page_range):
        """Sets the page_range of this PdfScalePageParameters.

        Specifies the number of the page, or the range of pages which shall be scaled.  # noqa: E501

        :param page_range: The page_range of this PdfScalePageParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and page_range is None:  # noqa: E501
            raise ValueError("Invalid value for `page_range`, must not be `None`")  # noqa: E501

        self._page_range = page_range

    @property
    def scale_x(self):
        """Gets the scale_x of this PdfScalePageParameters.  # noqa: E501

        Specifies the horizontal scale factor, by which the width of the page shall be multiplied.  # noqa: E501

        :return: The scale_x of this PdfScalePageParameters.  # noqa: E501
        :rtype: float
        """
        return self._scale_x

    @scale_x.setter
    def scale_x(self, scale_x):
        """Sets the scale_x of this PdfScalePageParameters.

        Specifies the horizontal scale factor, by which the width of the page shall be multiplied.  # noqa: E501

        :param scale_x: The scale_x of this PdfScalePageParameters.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and scale_x is None:  # noqa: E501
            raise ValueError("Invalid value for `scale_x`, must not be `None`")  # noqa: E501

        self._scale_x = scale_x

    @property
    def scale_y(self):
        """Gets the scale_y of this PdfScalePageParameters.  # noqa: E501

        Specifies the horizontal scale factor, by which the height of the page shall be multiplied.  # noqa: E501

        :return: The scale_y of this PdfScalePageParameters.  # noqa: E501
        :rtype: float
        """
        return self._scale_y

    @scale_y.setter
    def scale_y(self, scale_y):
        """Sets the scale_y of this PdfScalePageParameters.

        Specifies the horizontal scale factor, by which the height of the page shall be multiplied.  # noqa: E501

        :param scale_y: The scale_y of this PdfScalePageParameters.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and scale_y is None:  # noqa: E501
            raise ValueError("Invalid value for `scale_y`, must not be `None`")  # noqa: E501

        self._scale_y = scale_y

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
        if not isinstance(other, PdfScalePageParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PdfScalePageParameters):
            return True

        return self.to_dict() != other.to_dict()
