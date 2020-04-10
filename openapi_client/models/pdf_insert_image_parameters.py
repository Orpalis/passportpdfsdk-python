# coding: utf-8

"""
    PassportPDF API

          Introduction:    PassportPDF API is a REST API that lets you perform complex operations on documents and images easily.  You may consume the API by using our.NET SDK (other platforms / languages are soon to come), or any REST client by sending your requests to the appropriate endpoints.   A list of all the available endpoints can be found on the API reference page at https://passportpdfapi.com/references/api/index.html        Authentication:    Each available operation has a predefined cost, expressed as a number of tokens.  These tokens are deducted from your \"passport,\" which has a unique identifier that acts as an API key. This key is, therefore, required to be provided with each request for the latter to be honored(except if the operation does not have a cost, typically when you request a simple data with a GET).  Your key must be included in the header of the request, under the name \"X-PassportPdf-API-Key.\"  If you are using the.NET SDK, you can either set your key in the ApiKey property of your API instance(PdfApi or ImageApi, for example) or set it globally in the GlobalConfiguration instance if you want to set it once for the whole life cycle of your application.          Communication with the API:    All the available actions are listed on the API reference page, as previously mentioned.  There are several different controllers, i.e., routes, which categorize the actions.For example, you may use the PDF controller(\"/api/pdf\" route) to perform PDF - related operations, and the Image controller(\"/api/image\") for images.  Each action defines what kind of parameters(if any) is expected, and what kind of response is served.Parameters and responses are represented using data models, or \"schemas,\" and are listed in the \"Schemas\" section of the reference.   Parameters and response models of a given action are both prefixed by the controller name, the action name, and \"Parameters\" / \"Response,\" e.g. \"api/pdf/reduce\" respectively receives and serves a PdfReduceParameters and PdfReduceResponse models.  Using the .NET SDK, you will find the objects to interact with the different controllers in the PassportPDF.Api namespace and all the schemas in the PassportPDF.Model namespace.        Processing documents:    Each document manipulation starts with importing the file onto the API.  The LoadDocument action of the PDF controller lets you import your document as a PDF.  Note that the GetPDFImportSupportedFileExtensions action of the same controller will let you know all the different types of files that you may import as a PDF. LoadDocument responds with a JSON-serialized PdfLoadDocumentResponse model, which contains a \"FileId\" property.This identifier is required for the API to know about your document for further manipulations, hence the presence of a \"FileId\" property in the PdfReduceParameters schema (and many other parameters schemas). To download the changes made to a file, you need, of course, to download the new version of the file from the API.  To save your document as a PDF, you will need to use the SaveDocument action of the PDF controller and provide a PdfSaveDocumentParameters data model that contains the identifier of your file.        Errors:    Conventional HTTP response codes are used to indicate the success or failure of an API request.   The Error data model also defines some information about an error that occurred on the API.   Each response model has an Error in its definition, and its sole existence in the serialized response - which should thus always be checked - indicates that something went wrong.  Among the information given by the Error schema, \"ResultCode\" specifies a value of the \"PassportPDFStatus\" enumeration, that defines a first level of error information. \"InternalErrorId\" defines a unique identifier for the error, which comes very handy for us to troubleshoot any issue you may encounter quickly.        Efficiency considerations:    Multipart upload/download is available and lets you directly stream a file to/from the API.  In the PDF controller, LoadDocument/LoadDocumentMultipart and SaveDocument/SaveDocumentToFile may be used to upload/download a document using respectively binary data serialization and streaming multipart HTTP requests.  The second approach should be favored when dealing with large files, as it will be much more efficient in that context.    # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class PdfInsertImageParameters(object):
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
        'image_data': 'str',
        'image_file_id': 'str',
        'quality': 'int',
        'color_image_compression': 'PdfImageCompressionScheme',
        'bitonal_compression': 'PdfImageCompressionScheme'
    }

    attribute_map = {
        'file_id': 'FileId',
        'page_range': 'PageRange',
        'image_data': 'ImageData',
        'image_file_id': 'ImageFileId',
        'quality': 'Quality',
        'color_image_compression': 'ColorImageCompression',
        'bitonal_compression': 'BitonalCompression'
    }

    def __init__(self, file_id=None, page_range=None, image_data=None, image_file_id='', quality=75, color_image_compression=None, bitonal_compression=None, local_vars_configuration=None):  # noqa: E501
        """PdfInsertImageParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._page_range = None
        self._image_data = None
        self._image_file_id = None
        self._quality = None
        self._color_image_compression = None
        self._bitonal_compression = None
        self.discriminator = None

        self.file_id = file_id
        self.page_range = page_range
        self.image_data = image_data
        self.image_file_id = image_file_id
        if quality is not None:
            self.quality = quality
        if color_image_compression is not None:
            self.color_image_compression = color_image_compression
        if bitonal_compression is not None:
            self.bitonal_compression = bitonal_compression

    @property
    def file_id(self):
        """Gets the file_id of this PdfInsertImageParameters.  # noqa: E501

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :return: The file_id of this PdfInsertImageParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this PdfInsertImageParameters.

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :param file_id: The file_id of this PdfInsertImageParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def page_range(self):
        """Gets the page_range of this PdfInsertImageParameters.  # noqa: E501

        Specifies the page or the range of pages where the image shall be inserted.  # noqa: E501

        :return: The page_range of this PdfInsertImageParameters.  # noqa: E501
        :rtype: str
        """
        return self._page_range

    @page_range.setter
    def page_range(self, page_range):
        """Sets the page_range of this PdfInsertImageParameters.

        Specifies the page or the range of pages where the image shall be inserted.  # noqa: E501

        :param page_range: The page_range of this PdfInsertImageParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and page_range is None:  # noqa: E501
            raise ValueError("Invalid value for `page_range`, must not be `None`")  # noqa: E501

        self._page_range = page_range

    @property
    def image_data(self):
        """Gets the image_data of this PdfInsertImageParameters.  # noqa: E501

        Specifies the data of the image to be inserted.  # noqa: E501

        :return: The image_data of this PdfInsertImageParameters.  # noqa: E501
        :rtype: str
        """
        return self._image_data

    @image_data.setter
    def image_data(self, image_data):
        """Sets the image_data of this PdfInsertImageParameters.

        Specifies the data of the image to be inserted.  # noqa: E501

        :param image_data: The image_data of this PdfInsertImageParameters.  # noqa: E501
        :type: str
        """

        self._image_data = image_data

    @property
    def image_file_id(self):
        """Gets the image_file_id of this PdfInsertImageParameters.  # noqa: E501

        Specifies the file ID of the image to be drawn.  # noqa: E501

        :return: The image_file_id of this PdfInsertImageParameters.  # noqa: E501
        :rtype: str
        """
        return self._image_file_id

    @image_file_id.setter
    def image_file_id(self, image_file_id):
        """Sets the image_file_id of this PdfInsertImageParameters.

        Specifies the file ID of the image to be drawn.  # noqa: E501

        :param image_file_id: The image_file_id of this PdfInsertImageParameters.  # noqa: E501
        :type: str
        """

        self._image_file_id = image_file_id

    @property
    def quality(self):
        """Gets the quality of this PdfInsertImageParameters.  # noqa: E501

        Specifies the level of quality to be used for the compression, from 1 (poorest) to 100 (greatest).  # noqa: E501

        :return: The quality of this PdfInsertImageParameters.  # noqa: E501
        :rtype: int
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this PdfInsertImageParameters.

        Specifies the level of quality to be used for the compression, from 1 (poorest) to 100 (greatest).  # noqa: E501

        :param quality: The quality of this PdfInsertImageParameters.  # noqa: E501
        :type: int
        """

        self._quality = quality

    @property
    def color_image_compression(self):
        """Gets the color_image_compression of this PdfInsertImageParameters.  # noqa: E501


        :return: The color_image_compression of this PdfInsertImageParameters.  # noqa: E501
        :rtype: PdfImageCompressionScheme
        """
        return self._color_image_compression

    @color_image_compression.setter
    def color_image_compression(self, color_image_compression):
        """Sets the color_image_compression of this PdfInsertImageParameters.


        :param color_image_compression: The color_image_compression of this PdfInsertImageParameters.  # noqa: E501
        :type: PdfImageCompressionScheme
        """

        self._color_image_compression = color_image_compression

    @property
    def bitonal_compression(self):
        """Gets the bitonal_compression of this PdfInsertImageParameters.  # noqa: E501


        :return: The bitonal_compression of this PdfInsertImageParameters.  # noqa: E501
        :rtype: PdfImageCompressionScheme
        """
        return self._bitonal_compression

    @bitonal_compression.setter
    def bitonal_compression(self, bitonal_compression):
        """Sets the bitonal_compression of this PdfInsertImageParameters.


        :param bitonal_compression: The bitonal_compression of this PdfInsertImageParameters.  # noqa: E501
        :type: PdfImageCompressionScheme
        """

        self._bitonal_compression = bitonal_compression

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
        if not isinstance(other, PdfInsertImageParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PdfInsertImageParameters):
            return True

        return self.to_dict() != other.to_dict()
