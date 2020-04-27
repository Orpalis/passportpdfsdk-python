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


class ImageSaveAsPDFParameters(object):
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
        'conformance': 'PdfConformance',
        'color_image_compression': 'PdfImageCompressionScheme',
        'bitonal_image_compression': 'PdfImageCompressionScheme',
        'enable_color_detection': 'bool',
        'image_quality': 'int',
        'downscale_resolution': 'int',
        'fast_web_view': 'bool'
    }

    attribute_map = {
        'file_id': 'FileId',
        'page_range': 'PageRange',
        'conformance': 'Conformance',
        'color_image_compression': 'ColorImageCompression',
        'bitonal_image_compression': 'BitonalImageCompression',
        'enable_color_detection': 'EnableColorDetection',
        'image_quality': 'ImageQuality',
        'downscale_resolution': 'DownscaleResolution',
        'fast_web_view': 'FastWebView'
    }

    def __init__(self, file_id=None, page_range='*', conformance=None, color_image_compression=None, bitonal_image_compression=None, enable_color_detection=False, image_quality=75, downscale_resolution=0, fast_web_view=False, local_vars_configuration=None):  # noqa: E501
        """ImageSaveAsPDFParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._page_range = None
        self._conformance = None
        self._color_image_compression = None
        self._bitonal_image_compression = None
        self._enable_color_detection = None
        self._image_quality = None
        self._downscale_resolution = None
        self._fast_web_view = None
        self.discriminator = None

        self.file_id = file_id
        self.page_range = page_range
        if conformance is not None:
            self.conformance = conformance
        if color_image_compression is not None:
            self.color_image_compression = color_image_compression
        if bitonal_image_compression is not None:
            self.bitonal_image_compression = bitonal_image_compression
        if enable_color_detection is not None:
            self.enable_color_detection = enable_color_detection
        if image_quality is not None:
            self.image_quality = image_quality
        if downscale_resolution is not None:
            self.downscale_resolution = downscale_resolution
        if fast_web_view is not None:
            self.fast_web_view = fast_web_view

    @property
    def file_id(self):
        """Gets the file_id of this ImageSaveAsPDFParameters.  # noqa: E501

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :return: The file_id of this ImageSaveAsPDFParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this ImageSaveAsPDFParameters.

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :param file_id: The file_id of this ImageSaveAsPDFParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def page_range(self):
        """Gets the page_range of this ImageSaveAsPDFParameters.  # noqa: E501

        Specifies the number of the page, or the range of pages to be saved as PDF.  # noqa: E501

        :return: The page_range of this ImageSaveAsPDFParameters.  # noqa: E501
        :rtype: str
        """
        return self._page_range

    @page_range.setter
    def page_range(self, page_range):
        """Sets the page_range of this ImageSaveAsPDFParameters.

        Specifies the number of the page, or the range of pages to be saved as PDF.  # noqa: E501

        :param page_range: The page_range of this ImageSaveAsPDFParameters.  # noqa: E501
        :type: str
        """

        self._page_range = page_range

    @property
    def conformance(self):
        """Gets the conformance of this ImageSaveAsPDFParameters.  # noqa: E501


        :return: The conformance of this ImageSaveAsPDFParameters.  # noqa: E501
        :rtype: PdfConformance
        """
        return self._conformance

    @conformance.setter
    def conformance(self, conformance):
        """Sets the conformance of this ImageSaveAsPDFParameters.


        :param conformance: The conformance of this ImageSaveAsPDFParameters.  # noqa: E501
        :type: PdfConformance
        """

        self._conformance = conformance

    @property
    def color_image_compression(self):
        """Gets the color_image_compression of this ImageSaveAsPDFParameters.  # noqa: E501


        :return: The color_image_compression of this ImageSaveAsPDFParameters.  # noqa: E501
        :rtype: PdfImageCompressionScheme
        """
        return self._color_image_compression

    @color_image_compression.setter
    def color_image_compression(self, color_image_compression):
        """Sets the color_image_compression of this ImageSaveAsPDFParameters.


        :param color_image_compression: The color_image_compression of this ImageSaveAsPDFParameters.  # noqa: E501
        :type: PdfImageCompressionScheme
        """

        self._color_image_compression = color_image_compression

    @property
    def bitonal_image_compression(self):
        """Gets the bitonal_image_compression of this ImageSaveAsPDFParameters.  # noqa: E501


        :return: The bitonal_image_compression of this ImageSaveAsPDFParameters.  # noqa: E501
        :rtype: PdfImageCompressionScheme
        """
        return self._bitonal_image_compression

    @bitonal_image_compression.setter
    def bitonal_image_compression(self, bitonal_image_compression):
        """Sets the bitonal_image_compression of this ImageSaveAsPDFParameters.


        :param bitonal_image_compression: The bitonal_image_compression of this ImageSaveAsPDFParameters.  # noqa: E501
        :type: PdfImageCompressionScheme
        """

        self._bitonal_image_compression = bitonal_image_compression

    @property
    def enable_color_detection(self):
        """Gets the enable_color_detection of this ImageSaveAsPDFParameters.  # noqa: E501

        Specifies is color detection must be used.  # noqa: E501

        :return: The enable_color_detection of this ImageSaveAsPDFParameters.  # noqa: E501
        :rtype: bool
        """
        return self._enable_color_detection

    @enable_color_detection.setter
    def enable_color_detection(self, enable_color_detection):
        """Sets the enable_color_detection of this ImageSaveAsPDFParameters.

        Specifies is color detection must be used.  # noqa: E501

        :param enable_color_detection: The enable_color_detection of this ImageSaveAsPDFParameters.  # noqa: E501
        :type: bool
        """

        self._enable_color_detection = enable_color_detection

    @property
    def image_quality(self):
        """Gets the image_quality of this ImageSaveAsPDFParameters.  # noqa: E501

        Specifies the quality to be used for the compression of the images from the PDF.  Must be in the range [0 (best compression - worst quality) - 100 (worst quality - best compression)].  # noqa: E501

        :return: The image_quality of this ImageSaveAsPDFParameters.  # noqa: E501
        :rtype: int
        """
        return self._image_quality

    @image_quality.setter
    def image_quality(self, image_quality):
        """Sets the image_quality of this ImageSaveAsPDFParameters.

        Specifies the quality to be used for the compression of the images from the PDF.  Must be in the range [0 (best compression - worst quality) - 100 (worst quality - best compression)].  # noqa: E501

        :param image_quality: The image_quality of this ImageSaveAsPDFParameters.  # noqa: E501
        :type: int
        """

        self._image_quality = image_quality

    @property
    def downscale_resolution(self):
        """Gets the downscale_resolution of this ImageSaveAsPDFParameters.  # noqa: E501

        Specifies the resolution for downscaling images, if any.  # noqa: E501

        :return: The downscale_resolution of this ImageSaveAsPDFParameters.  # noqa: E501
        :rtype: int
        """
        return self._downscale_resolution

    @downscale_resolution.setter
    def downscale_resolution(self, downscale_resolution):
        """Sets the downscale_resolution of this ImageSaveAsPDFParameters.

        Specifies the resolution for downscaling images, if any.  # noqa: E501

        :param downscale_resolution: The downscale_resolution of this ImageSaveAsPDFParameters.  # noqa: E501
        :type: int
        """

        self._downscale_resolution = downscale_resolution

    @property
    def fast_web_view(self):
        """Gets the fast_web_view of this ImageSaveAsPDFParameters.  # noqa: E501

        Specifies whether the PDF shall be optimized for online distribution.  # noqa: E501

        :return: The fast_web_view of this ImageSaveAsPDFParameters.  # noqa: E501
        :rtype: bool
        """
        return self._fast_web_view

    @fast_web_view.setter
    def fast_web_view(self, fast_web_view):
        """Sets the fast_web_view of this ImageSaveAsPDFParameters.

        Specifies whether the PDF shall be optimized for online distribution.  # noqa: E501

        :param fast_web_view: The fast_web_view of this ImageSaveAsPDFParameters.  # noqa: E501
        :type: bool
        """

        self._fast_web_view = fast_web_view

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
        if not isinstance(other, ImageSaveAsPDFParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageSaveAsPDFParameters):
            return True

        return self.to_dict() != other.to_dict()
