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


class InlineObject2(object):
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
        'file_data': 'file',
        'load_document_parameters': 'PdfLoadDocumentParameters'
    }

    attribute_map = {
        'file_data': 'fileData',
        'load_document_parameters': 'loadDocumentParameters'
    }

    def __init__(self, file_data=None, load_document_parameters=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_data = None
        self._load_document_parameters = None
        self.discriminator = None

        self.file_data = file_data
        if load_document_parameters is not None:
            self.load_document_parameters = load_document_parameters

    @property
    def file_data(self):
        """Gets the file_data of this InlineObject2.  # noqa: E501

        The data of the document.  # noqa: E501

        :return: The file_data of this InlineObject2.  # noqa: E501
        :rtype: file
        """
        return self._file_data

    @file_data.setter
    def file_data(self, file_data):
        """Sets the file_data of this InlineObject2.

        The data of the document.  # noqa: E501

        :param file_data: The file_data of this InlineObject2.  # noqa: E501
        :type: file
        """
        if self.local_vars_configuration.client_side_validation and file_data is None:  # noqa: E501
            raise ValueError("Invalid value for `file_data`, must not be `None`")  # noqa: E501

        self._file_data = file_data

    @property
    def load_document_parameters(self):
        """Gets the load_document_parameters of this InlineObject2.  # noqa: E501


        :return: The load_document_parameters of this InlineObject2.  # noqa: E501
        :rtype: PdfLoadDocumentParameters
        """
        return self._load_document_parameters

    @load_document_parameters.setter
    def load_document_parameters(self, load_document_parameters):
        """Sets the load_document_parameters of this InlineObject2.


        :param load_document_parameters: The load_document_parameters of this InlineObject2.  # noqa: E501
        :type: PdfLoadDocumentParameters
        """

        self._load_document_parameters = load_document_parameters

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
        if not isinstance(other, InlineObject2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject2):
            return True

        return self.to_dict() != other.to_dict()
