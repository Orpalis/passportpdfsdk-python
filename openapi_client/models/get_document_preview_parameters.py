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


class GetDocumentPreviewParameters(object):
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
        'file_data': 'str',
        'file_name': 'str',
        'thumbnail_width': 'int',
        'thumbnail_height': 'int',
        'thumbnail_background_color': 'str',
        'thumbnail_fit_to_page_size': 'bool'
    }

    attribute_map = {
        'file_id': 'FileId',
        'file_data': 'FileData',
        'file_name': 'FileName',
        'thumbnail_width': 'ThumbnailWidth',
        'thumbnail_height': 'ThumbnailHeight',
        'thumbnail_background_color': 'ThumbnailBackgroundColor',
        'thumbnail_fit_to_page_size': 'ThumbnailFitToPageSize'
    }

    def __init__(self, file_id=None, file_data=None, file_name=None, thumbnail_width=140, thumbnail_height=220, thumbnail_background_color='rgba(0,0,0,0)', thumbnail_fit_to_page_size=True, local_vars_configuration=None):  # noqa: E501
        """GetDocumentPreviewParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._file_data = None
        self._file_name = None
        self._thumbnail_width = None
        self._thumbnail_height = None
        self._thumbnail_background_color = None
        self._thumbnail_fit_to_page_size = None
        self.discriminator = None

        self.file_id = file_id
        self.file_data = file_data
        self.file_name = file_name
        if thumbnail_width is not None:
            self.thumbnail_width = thumbnail_width
        if thumbnail_height is not None:
            self.thumbnail_height = thumbnail_height
        self.thumbnail_background_color = thumbnail_background_color
        if thumbnail_fit_to_page_size is not None:
            self.thumbnail_fit_to_page_size = thumbnail_fit_to_page_size

    @property
    def file_id(self):
        """Gets the file_id of this GetDocumentPreviewParameters.  # noqa: E501

        Specifies the identifier of the file to be previewed.  # noqa: E501

        :return: The file_id of this GetDocumentPreviewParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this GetDocumentPreviewParameters.

        Specifies the identifier of the file to be previewed.  # noqa: E501

        :param file_id: The file_id of this GetDocumentPreviewParameters.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def file_data(self):
        """Gets the file_data of this GetDocumentPreviewParameters.  # noqa: E501

        Specifies the data of the document to be previewed.  # noqa: E501

        :return: The file_data of this GetDocumentPreviewParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_data

    @file_data.setter
    def file_data(self, file_data):
        """Sets the file_data of this GetDocumentPreviewParameters.

        Specifies the data of the document to be previewed.  # noqa: E501

        :param file_data: The file_data of this GetDocumentPreviewParameters.  # noqa: E501
        :type: str
        """

        self._file_data = file_data

    @property
    def file_name(self):
        """Gets the file_name of this GetDocumentPreviewParameters.  # noqa: E501

        Specifies the name of the file to be previewed.  # noqa: E501

        :return: The file_name of this GetDocumentPreviewParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this GetDocumentPreviewParameters.

        Specifies the name of the file to be previewed.  # noqa: E501

        :param file_name: The file_name of this GetDocumentPreviewParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def thumbnail_width(self):
        """Gets the thumbnail_width of this GetDocumentPreviewParameters.  # noqa: E501

        Specifies, in pixels, the width of the thumbnail to be retrieved.  # noqa: E501

        :return: The thumbnail_width of this GetDocumentPreviewParameters.  # noqa: E501
        :rtype: int
        """
        return self._thumbnail_width

    @thumbnail_width.setter
    def thumbnail_width(self, thumbnail_width):
        """Sets the thumbnail_width of this GetDocumentPreviewParameters.

        Specifies, in pixels, the width of the thumbnail to be retrieved.  # noqa: E501

        :param thumbnail_width: The thumbnail_width of this GetDocumentPreviewParameters.  # noqa: E501
        :type: int
        """

        self._thumbnail_width = thumbnail_width

    @property
    def thumbnail_height(self):
        """Gets the thumbnail_height of this GetDocumentPreviewParameters.  # noqa: E501

        Specifies, in pixels, the height of the thumbnail to be retrieved.  # noqa: E501

        :return: The thumbnail_height of this GetDocumentPreviewParameters.  # noqa: E501
        :rtype: int
        """
        return self._thumbnail_height

    @thumbnail_height.setter
    def thumbnail_height(self, thumbnail_height):
        """Sets the thumbnail_height of this GetDocumentPreviewParameters.

        Specifies, in pixels, the height of the thumbnail to be retrieved.  # noqa: E501

        :param thumbnail_height: The thumbnail_height of this GetDocumentPreviewParameters.  # noqa: E501
        :type: int
        """

        self._thumbnail_height = thumbnail_height

    @property
    def thumbnail_background_color(self):
        """Gets the thumbnail_background_color of this GetDocumentPreviewParameters.  # noqa: E501

        Specifies the background color of the thumbnail, using the color name (ie: \"red\") or its RGBa code (ie: \"rgba(255,0,0,1)\").  # noqa: E501

        :return: The thumbnail_background_color of this GetDocumentPreviewParameters.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_background_color

    @thumbnail_background_color.setter
    def thumbnail_background_color(self, thumbnail_background_color):
        """Sets the thumbnail_background_color of this GetDocumentPreviewParameters.

        Specifies the background color of the thumbnail, using the color name (ie: \"red\") or its RGBa code (ie: \"rgba(255,0,0,1)\").  # noqa: E501

        :param thumbnail_background_color: The thumbnail_background_color of this GetDocumentPreviewParameters.  # noqa: E501
        :type: str
        """

        self._thumbnail_background_color = thumbnail_background_color

    @property
    def thumbnail_fit_to_page_size(self):
        """Gets the thumbnail_fit_to_page_size of this GetDocumentPreviewParameters.  # noqa: E501

        Specifies if the size of the produced thumbnail is automatically adjusted to don't have any margin.  # noqa: E501

        :return: The thumbnail_fit_to_page_size of this GetDocumentPreviewParameters.  # noqa: E501
        :rtype: bool
        """
        return self._thumbnail_fit_to_page_size

    @thumbnail_fit_to_page_size.setter
    def thumbnail_fit_to_page_size(self, thumbnail_fit_to_page_size):
        """Sets the thumbnail_fit_to_page_size of this GetDocumentPreviewParameters.

        Specifies if the size of the produced thumbnail is automatically adjusted to don't have any margin.  # noqa: E501

        :param thumbnail_fit_to_page_size: The thumbnail_fit_to_page_size of this GetDocumentPreviewParameters.  # noqa: E501
        :type: bool
        """

        self._thumbnail_fit_to_page_size = thumbnail_fit_to_page_size

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
        if not isinstance(other, GetDocumentPreviewParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDocumentPreviewParameters):
            return True

        return self.to_dict() != other.to_dict()
