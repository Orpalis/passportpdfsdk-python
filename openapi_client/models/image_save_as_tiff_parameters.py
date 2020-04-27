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


class ImageSaveAsTIFFParameters(object):
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
        'compression': 'TiffSaveCompression',
        'jpeg_quality': 'int',
        'use_cmyk': 'bool'
    }

    attribute_map = {
        'file_id': 'FileId',
        'page_range': 'PageRange',
        'compression': 'Compression',
        'jpeg_quality': 'JpegQuality',
        'use_cmyk': 'UseCMYK'
    }

    def __init__(self, file_id=None, page_range='*', compression=None, jpeg_quality=75, use_cmyk=False, local_vars_configuration=None):  # noqa: E501
        """ImageSaveAsTIFFParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._page_range = None
        self._compression = None
        self._jpeg_quality = None
        self._use_cmyk = None
        self.discriminator = None

        self.file_id = file_id
        self.page_range = page_range
        if compression is not None:
            self.compression = compression
        if jpeg_quality is not None:
            self.jpeg_quality = jpeg_quality
        if use_cmyk is not None:
            self.use_cmyk = use_cmyk

    @property
    def file_id(self):
        """Gets the file_id of this ImageSaveAsTIFFParameters.  # noqa: E501

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :return: The file_id of this ImageSaveAsTIFFParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this ImageSaveAsTIFFParameters.

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :param file_id: The file_id of this ImageSaveAsTIFFParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def page_range(self):
        """Gets the page_range of this ImageSaveAsTIFFParameters.  # noqa: E501

        Specifies the number of the page, or the range of pages to be saved as TIFF.  # noqa: E501

        :return: The page_range of this ImageSaveAsTIFFParameters.  # noqa: E501
        :rtype: str
        """
        return self._page_range

    @page_range.setter
    def page_range(self, page_range):
        """Sets the page_range of this ImageSaveAsTIFFParameters.

        Specifies the number of the page, or the range of pages to be saved as TIFF.  # noqa: E501

        :param page_range: The page_range of this ImageSaveAsTIFFParameters.  # noqa: E501
        :type: str
        """

        self._page_range = page_range

    @property
    def compression(self):
        """Gets the compression of this ImageSaveAsTIFFParameters.  # noqa: E501


        :return: The compression of this ImageSaveAsTIFFParameters.  # noqa: E501
        :rtype: TiffSaveCompression
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """Sets the compression of this ImageSaveAsTIFFParameters.


        :param compression: The compression of this ImageSaveAsTIFFParameters.  # noqa: E501
        :type: TiffSaveCompression
        """

        self._compression = compression

    @property
    def jpeg_quality(self):
        """Gets the jpeg_quality of this ImageSaveAsTIFFParameters.  # noqa: E501

        Specifies the level of quality to be used if JPEG compression is used, from 1 (poorest) to 100 (greatest).  # noqa: E501

        :return: The jpeg_quality of this ImageSaveAsTIFFParameters.  # noqa: E501
        :rtype: int
        """
        return self._jpeg_quality

    @jpeg_quality.setter
    def jpeg_quality(self, jpeg_quality):
        """Sets the jpeg_quality of this ImageSaveAsTIFFParameters.

        Specifies the level of quality to be used if JPEG compression is used, from 1 (poorest) to 100 (greatest).  # noqa: E501

        :param jpeg_quality: The jpeg_quality of this ImageSaveAsTIFFParameters.  # noqa: E501
        :type: int
        """

        self._jpeg_quality = jpeg_quality

    @property
    def use_cmyk(self):
        """Gets the use_cmyk of this ImageSaveAsTIFFParameters.  # noqa: E501

        Specifies whether the TIFF shall be saved in CMYK color space or not.  # noqa: E501

        :return: The use_cmyk of this ImageSaveAsTIFFParameters.  # noqa: E501
        :rtype: bool
        """
        return self._use_cmyk

    @use_cmyk.setter
    def use_cmyk(self, use_cmyk):
        """Sets the use_cmyk of this ImageSaveAsTIFFParameters.

        Specifies whether the TIFF shall be saved in CMYK color space or not.  # noqa: E501

        :param use_cmyk: The use_cmyk of this ImageSaveAsTIFFParameters.  # noqa: E501
        :type: bool
        """

        self._use_cmyk = use_cmyk

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
        if not isinstance(other, ImageSaveAsTIFFParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageSaveAsTIFFParameters):
            return True

        return self.to_dict() != other.to_dict()
