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


class PdfAutoDeskewParameters(object):
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
        'max_angle_of_research': 'float',
        'optimistic': 'bool'
    }

    attribute_map = {
        'file_id': 'FileId',
        'page_range': 'PageRange',
        'max_angle_of_research': 'MaxAngleOfResearch',
        'optimistic': 'Optimistic'
    }

    def __init__(self, file_id=None, page_range=None, max_angle_of_research=15, optimistic=False, local_vars_configuration=None):  # noqa: E501
        """PdfAutoDeskewParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._page_range = None
        self._max_angle_of_research = None
        self._optimistic = None
        self.discriminator = None

        self.file_id = file_id
        self.page_range = page_range
        if max_angle_of_research is not None:
            self.max_angle_of_research = max_angle_of_research
        if optimistic is not None:
            self.optimistic = optimistic

    @property
    def file_id(self):
        """Gets the file_id of this PdfAutoDeskewParameters.  # noqa: E501

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :return: The file_id of this PdfAutoDeskewParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this PdfAutoDeskewParameters.

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :param file_id: The file_id of this PdfAutoDeskewParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def page_range(self):
        """Gets the page_range of this PdfAutoDeskewParameters.  # noqa: E501

        Specifies the page or the page range to be auto-deskewed.  # noqa: E501

        :return: The page_range of this PdfAutoDeskewParameters.  # noqa: E501
        :rtype: str
        """
        return self._page_range

    @page_range.setter
    def page_range(self, page_range):
        """Sets the page_range of this PdfAutoDeskewParameters.

        Specifies the page or the page range to be auto-deskewed.  # noqa: E501

        :param page_range: The page_range of this PdfAutoDeskewParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and page_range is None:  # noqa: E501
            raise ValueError("Invalid value for `page_range`, must not be `None`")  # noqa: E501

        self._page_range = page_range

    @property
    def max_angle_of_research(self):
        """Gets the max_angle_of_research of this PdfAutoDeskewParameters.  # noqa: E501

        Specifies the maximum skew angle to be detected. A value of below 15 is suggested.  # noqa: E501

        :return: The max_angle_of_research of this PdfAutoDeskewParameters.  # noqa: E501
        :rtype: float
        """
        return self._max_angle_of_research

    @max_angle_of_research.setter
    def max_angle_of_research(self, max_angle_of_research):
        """Sets the max_angle_of_research of this PdfAutoDeskewParameters.

        Specifies the maximum skew angle to be detected. A value of below 15 is suggested.  # noqa: E501

        :param max_angle_of_research: The max_angle_of_research of this PdfAutoDeskewParameters.  # noqa: E501
        :type: float
        """

        self._max_angle_of_research = max_angle_of_research

    @property
    def optimistic(self):
        """Gets the optimistic of this PdfAutoDeskewParameters.  # noqa: E501

        Specifies whether the skew detection engine must be optimistic when detecting angles.  If you know the image is skewed, you should set this to true.  # noqa: E501

        :return: The optimistic of this PdfAutoDeskewParameters.  # noqa: E501
        :rtype: bool
        """
        return self._optimistic

    @optimistic.setter
    def optimistic(self, optimistic):
        """Sets the optimistic of this PdfAutoDeskewParameters.

        Specifies whether the skew detection engine must be optimistic when detecting angles.  If you know the image is skewed, you should set this to true.  # noqa: E501

        :param optimistic: The optimistic of this PdfAutoDeskewParameters.  # noqa: E501
        :type: bool
        """

        self._optimistic = optimistic

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
        if not isinstance(other, PdfAutoDeskewParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PdfAutoDeskewParameters):
            return True

        return self.to_dict() != other.to_dict()
