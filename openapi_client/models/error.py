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


class Error(object):
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
        'result_code': 'PassportPDFStatus',
        'ext_result_status': 'str',
        'ext_result_message': 'str',
        'internal_error_id': 'str'
    }

    attribute_map = {
        'result_code': 'ResultCode',
        'ext_result_status': 'ExtResultStatus',
        'ext_result_message': 'ExtResultMessage',
        'internal_error_id': 'InternalErrorId'
    }

    def __init__(self, result_code=None, ext_result_status=None, ext_result_message=None, internal_error_id=None, local_vars_configuration=None):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result_code = None
        self._ext_result_status = None
        self._ext_result_message = None
        self._internal_error_id = None
        self.discriminator = None

        if result_code is not None:
            self.result_code = result_code
        self.ext_result_status = ext_result_status
        self.ext_result_message = ext_result_message
        self.internal_error_id = internal_error_id

    @property
    def result_code(self):
        """Gets the result_code of this Error.  # noqa: E501


        :return: The result_code of this Error.  # noqa: E501
        :rtype: PassportPDFStatus
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this Error.


        :param result_code: The result_code of this Error.  # noqa: E501
        :type: PassportPDFStatus
        """

        self._result_code = result_code

    @property
    def ext_result_status(self):
        """Gets the ext_result_status of this Error.  # noqa: E501

        Specifies a result code related to an error which occured in an external component.  # noqa: E501

        :return: The ext_result_status of this Error.  # noqa: E501
        :rtype: str
        """
        return self._ext_result_status

    @ext_result_status.setter
    def ext_result_status(self, ext_result_status):
        """Sets the ext_result_status of this Error.

        Specifies a result code related to an error which occured in an external component.  # noqa: E501

        :param ext_result_status: The ext_result_status of this Error.  # noqa: E501
        :type: str
        """

        self._ext_result_status = ext_result_status

    @property
    def ext_result_message(self):
        """Gets the ext_result_message of this Error.  # noqa: E501

        Specifies a message which further describes the error.  # noqa: E501

        :return: The ext_result_message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._ext_result_message

    @ext_result_message.setter
    def ext_result_message(self, ext_result_message):
        """Sets the ext_result_message of this Error.

        Specifies a message which further describes the error.  # noqa: E501

        :param ext_result_message: The ext_result_message of this Error.  # noqa: E501
        :type: str
        """

        self._ext_result_message = ext_result_message

    @property
    def internal_error_id(self):
        """Gets the internal_error_id of this Error.  # noqa: E501

        Specifies a unique identifier, allowing to easily assess the error.  # noqa: E501

        :return: The internal_error_id of this Error.  # noqa: E501
        :rtype: str
        """
        return self._internal_error_id

    @internal_error_id.setter
    def internal_error_id(self, internal_error_id):
        """Sets the internal_error_id of this Error.

        Specifies a unique identifier, allowing to easily assess the error.  # noqa: E501

        :param internal_error_id: The internal_error_id of this Error.  # noqa: E501
        :type: str
        """

        self._internal_error_id = internal_error_id

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
        if not isinstance(other, Error):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Error):
            return True

        return self.to_dict() != other.to_dict()
