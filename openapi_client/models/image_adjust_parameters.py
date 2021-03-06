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


class ImageAdjustParameters(object):
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
        'roi_left': 'int',
        'roi_top': 'int',
        'roi_width': 'int',
        'roi_height': 'int',
        'gamma_correction': 'int',
        'brightness': 'int',
        'contrast': 'int',
        'saturation': 'int',
        'auto_contrast_enhancement': 'bool',
        'contrast_histogram_stretch': 'bool'
    }

    attribute_map = {
        'file_id': 'FileId',
        'page_range': 'PageRange',
        'roi_left': 'RoiLeft',
        'roi_top': 'RoiTop',
        'roi_width': 'RoiWidth',
        'roi_height': 'RoiHeight',
        'gamma_correction': 'GammaCorrection',
        'brightness': 'Brightness',
        'contrast': 'Contrast',
        'saturation': 'Saturation',
        'auto_contrast_enhancement': 'AutoContrastEnhancement',
        'contrast_histogram_stretch': 'ContrastHistogramStretch'
    }

    def __init__(self, file_id=None, page_range=None, roi_left=0, roi_top=0, roi_width=0, roi_height=0, gamma_correction=0, brightness=0, contrast=0, saturation=0, auto_contrast_enhancement=False, contrast_histogram_stretch=False, local_vars_configuration=None):  # noqa: E501
        """ImageAdjustParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._page_range = None
        self._roi_left = None
        self._roi_top = None
        self._roi_width = None
        self._roi_height = None
        self._gamma_correction = None
        self._brightness = None
        self._contrast = None
        self._saturation = None
        self._auto_contrast_enhancement = None
        self._contrast_histogram_stretch = None
        self.discriminator = None

        self.file_id = file_id
        self.page_range = page_range
        if roi_left is not None:
            self.roi_left = roi_left
        if roi_top is not None:
            self.roi_top = roi_top
        if roi_width is not None:
            self.roi_width = roi_width
        if roi_height is not None:
            self.roi_height = roi_height
        if gamma_correction is not None:
            self.gamma_correction = gamma_correction
        if brightness is not None:
            self.brightness = brightness
        if contrast is not None:
            self.contrast = contrast
        if saturation is not None:
            self.saturation = saturation
        if auto_contrast_enhancement is not None:
            self.auto_contrast_enhancement = auto_contrast_enhancement
        if contrast_histogram_stretch is not None:
            self.contrast_histogram_stretch = contrast_histogram_stretch

    @property
    def file_id(self):
        """Gets the file_id of this ImageAdjustParameters.  # noqa: E501

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :return: The file_id of this ImageAdjustParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this ImageAdjustParameters.

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :param file_id: The file_id of this ImageAdjustParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def page_range(self):
        """Gets the page_range of this ImageAdjustParameters.  # noqa: E501

        Specifies the number of the page, or the range of pages to adjust.  # noqa: E501

        :return: The page_range of this ImageAdjustParameters.  # noqa: E501
        :rtype: str
        """
        return self._page_range

    @page_range.setter
    def page_range(self, page_range):
        """Sets the page_range of this ImageAdjustParameters.

        Specifies the number of the page, or the range of pages to adjust.  # noqa: E501

        :param page_range: The page_range of this ImageAdjustParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and page_range is None:  # noqa: E501
            raise ValueError("Invalid value for `page_range`, must not be `None`")  # noqa: E501

        self._page_range = page_range

    @property
    def roi_left(self):
        """Gets the roi_left of this ImageAdjustParameters.  # noqa: E501

        Specifies the left coordinate, in pixel, of the region to process.  # noqa: E501

        :return: The roi_left of this ImageAdjustParameters.  # noqa: E501
        :rtype: int
        """
        return self._roi_left

    @roi_left.setter
    def roi_left(self, roi_left):
        """Sets the roi_left of this ImageAdjustParameters.

        Specifies the left coordinate, in pixel, of the region to process.  # noqa: E501

        :param roi_left: The roi_left of this ImageAdjustParameters.  # noqa: E501
        :type: int
        """

        self._roi_left = roi_left

    @property
    def roi_top(self):
        """Gets the roi_top of this ImageAdjustParameters.  # noqa: E501

        Specifies the top coordinate, in pixel, of the region to process.  # noqa: E501

        :return: The roi_top of this ImageAdjustParameters.  # noqa: E501
        :rtype: int
        """
        return self._roi_top

    @roi_top.setter
    def roi_top(self, roi_top):
        """Sets the roi_top of this ImageAdjustParameters.

        Specifies the top coordinate, in pixel, of the region to process.  # noqa: E501

        :param roi_top: The roi_top of this ImageAdjustParameters.  # noqa: E501
        :type: int
        """

        self._roi_top = roi_top

    @property
    def roi_width(self):
        """Gets the roi_width of this ImageAdjustParameters.  # noqa: E501

        Specifies the width, in pixel, of the region to process. 0 causes the entire image to be processed.  # noqa: E501

        :return: The roi_width of this ImageAdjustParameters.  # noqa: E501
        :rtype: int
        """
        return self._roi_width

    @roi_width.setter
    def roi_width(self, roi_width):
        """Sets the roi_width of this ImageAdjustParameters.

        Specifies the width, in pixel, of the region to process. 0 causes the entire image to be processed.  # noqa: E501

        :param roi_width: The roi_width of this ImageAdjustParameters.  # noqa: E501
        :type: int
        """

        self._roi_width = roi_width

    @property
    def roi_height(self):
        """Gets the roi_height of this ImageAdjustParameters.  # noqa: E501

        Specifies the height, in pixel, of the region to process. 0 causes the entire image to be processed.  # noqa: E501

        :return: The roi_height of this ImageAdjustParameters.  # noqa: E501
        :rtype: int
        """
        return self._roi_height

    @roi_height.setter
    def roi_height(self, roi_height):
        """Sets the roi_height of this ImageAdjustParameters.

        Specifies the height, in pixel, of the region to process. 0 causes the entire image to be processed.  # noqa: E501

        :param roi_height: The roi_height of this ImageAdjustParameters.  # noqa: E501
        :type: int
        """

        self._roi_height = roi_height

    @property
    def gamma_correction(self):
        """Gets the gamma_correction of this ImageAdjustParameters.  # noqa: E501

        Specifies the gamma correction parameter.  # noqa: E501

        :return: The gamma_correction of this ImageAdjustParameters.  # noqa: E501
        :rtype: int
        """
        return self._gamma_correction

    @gamma_correction.setter
    def gamma_correction(self, gamma_correction):
        """Sets the gamma_correction of this ImageAdjustParameters.

        Specifies the gamma correction parameter.  # noqa: E501

        :param gamma_correction: The gamma_correction of this ImageAdjustParameters.  # noqa: E501
        :type: int
        """

        self._gamma_correction = gamma_correction

    @property
    def brightness(self):
        """Gets the brightness of this ImageAdjustParameters.  # noqa: E501

        Specifies the brightness parameter.  # noqa: E501

        :return: The brightness of this ImageAdjustParameters.  # noqa: E501
        :rtype: int
        """
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        """Sets the brightness of this ImageAdjustParameters.

        Specifies the brightness parameter.  # noqa: E501

        :param brightness: The brightness of this ImageAdjustParameters.  # noqa: E501
        :type: int
        """

        self._brightness = brightness

    @property
    def contrast(self):
        """Gets the contrast of this ImageAdjustParameters.  # noqa: E501

        Specifies the contrast parameter.  # noqa: E501

        :return: The contrast of this ImageAdjustParameters.  # noqa: E501
        :rtype: int
        """
        return self._contrast

    @contrast.setter
    def contrast(self, contrast):
        """Sets the contrast of this ImageAdjustParameters.

        Specifies the contrast parameter.  # noqa: E501

        :param contrast: The contrast of this ImageAdjustParameters.  # noqa: E501
        :type: int
        """

        self._contrast = contrast

    @property
    def saturation(self):
        """Gets the saturation of this ImageAdjustParameters.  # noqa: E501

        Specifies the saturation parameter.  # noqa: E501

        :return: The saturation of this ImageAdjustParameters.  # noqa: E501
        :rtype: int
        """
        return self._saturation

    @saturation.setter
    def saturation(self, saturation):
        """Sets the saturation of this ImageAdjustParameters.

        Specifies the saturation parameter.  # noqa: E501

        :param saturation: The saturation of this ImageAdjustParameters.  # noqa: E501
        :type: int
        """

        self._saturation = saturation

    @property
    def auto_contrast_enhancement(self):
        """Gets the auto_contrast_enhancement of this ImageAdjustParameters.  # noqa: E501

        Specifies whether the contrast shall be automatically enhanced.  # noqa: E501

        :return: The auto_contrast_enhancement of this ImageAdjustParameters.  # noqa: E501
        :rtype: bool
        """
        return self._auto_contrast_enhancement

    @auto_contrast_enhancement.setter
    def auto_contrast_enhancement(self, auto_contrast_enhancement):
        """Sets the auto_contrast_enhancement of this ImageAdjustParameters.

        Specifies whether the contrast shall be automatically enhanced.  # noqa: E501

        :param auto_contrast_enhancement: The auto_contrast_enhancement of this ImageAdjustParameters.  # noqa: E501
        :type: bool
        """

        self._auto_contrast_enhancement = auto_contrast_enhancement

    @property
    def contrast_histogram_stretch(self):
        """Gets the contrast_histogram_stretch of this ImageAdjustParameters.  # noqa: E501

        Specifies whether a contrast histogram stretch filter shall be performed.  # noqa: E501

        :return: The contrast_histogram_stretch of this ImageAdjustParameters.  # noqa: E501
        :rtype: bool
        """
        return self._contrast_histogram_stretch

    @contrast_histogram_stretch.setter
    def contrast_histogram_stretch(self, contrast_histogram_stretch):
        """Sets the contrast_histogram_stretch of this ImageAdjustParameters.

        Specifies whether a contrast histogram stretch filter shall be performed.  # noqa: E501

        :param contrast_histogram_stretch: The contrast_histogram_stretch of this ImageAdjustParameters.  # noqa: E501
        :type: bool
        """

        self._contrast_histogram_stretch = contrast_histogram_stretch

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
        if not isinstance(other, ImageAdjustParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageAdjustParameters):
            return True

        return self.to_dict() != other.to_dict()
