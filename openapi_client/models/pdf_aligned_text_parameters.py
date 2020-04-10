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


class PdfAlignedTextParameters(object):
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
        'text_vertical_alignment': 'TextAlignment',
        'text_horizontal_alignment': 'TextAlignment',
        'text': 'str',
        'text_color': 'str',
        'font_name': 'str',
        'standard_font_name': 'StandardFontName',
        'font_style': 'FontStyle',
        'font_size': 'int'
    }

    attribute_map = {
        'text_vertical_alignment': 'TextVerticalAlignment',
        'text_horizontal_alignment': 'TextHorizontalAlignment',
        'text': 'Text',
        'text_color': 'TextColor',
        'font_name': 'FontName',
        'standard_font_name': 'StandardFontName',
        'font_style': 'FontStyle',
        'font_size': 'FontSize'
    }

    def __init__(self, text_vertical_alignment=None, text_horizontal_alignment=None, text=None, text_color='black', font_name=None, standard_font_name=None, font_style=None, font_size=11, local_vars_configuration=None):  # noqa: E501
        """PdfAlignedTextParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._text_vertical_alignment = None
        self._text_horizontal_alignment = None
        self._text = None
        self._text_color = None
        self._font_name = None
        self._standard_font_name = None
        self._font_style = None
        self._font_size = None
        self.discriminator = None

        if text_vertical_alignment is not None:
            self.text_vertical_alignment = text_vertical_alignment
        if text_horizontal_alignment is not None:
            self.text_horizontal_alignment = text_horizontal_alignment
        self.text = text
        self.text_color = text_color
        self.font_name = font_name
        if standard_font_name is not None:
            self.standard_font_name = standard_font_name
        if font_style is not None:
            self.font_style = font_style
        if font_size is not None:
            self.font_size = font_size

    @property
    def text_vertical_alignment(self):
        """Gets the text_vertical_alignment of this PdfAlignedTextParameters.  # noqa: E501


        :return: The text_vertical_alignment of this PdfAlignedTextParameters.  # noqa: E501
        :rtype: TextAlignment
        """
        return self._text_vertical_alignment

    @text_vertical_alignment.setter
    def text_vertical_alignment(self, text_vertical_alignment):
        """Sets the text_vertical_alignment of this PdfAlignedTextParameters.


        :param text_vertical_alignment: The text_vertical_alignment of this PdfAlignedTextParameters.  # noqa: E501
        :type: TextAlignment
        """

        self._text_vertical_alignment = text_vertical_alignment

    @property
    def text_horizontal_alignment(self):
        """Gets the text_horizontal_alignment of this PdfAlignedTextParameters.  # noqa: E501


        :return: The text_horizontal_alignment of this PdfAlignedTextParameters.  # noqa: E501
        :rtype: TextAlignment
        """
        return self._text_horizontal_alignment

    @text_horizontal_alignment.setter
    def text_horizontal_alignment(self, text_horizontal_alignment):
        """Sets the text_horizontal_alignment of this PdfAlignedTextParameters.


        :param text_horizontal_alignment: The text_horizontal_alignment of this PdfAlignedTextParameters.  # noqa: E501
        :type: TextAlignment
        """

        self._text_horizontal_alignment = text_horizontal_alignment

    @property
    def text(self):
        """Gets the text of this PdfAlignedTextParameters.  # noqa: E501

        Specifies the text.  # noqa: E501

        :return: The text of this PdfAlignedTextParameters.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PdfAlignedTextParameters.

        Specifies the text.  # noqa: E501

        :param text: The text of this PdfAlignedTextParameters.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def text_color(self):
        """Gets the text_color of this PdfAlignedTextParameters.  # noqa: E501

        Specifies the color of the text, using the color name (ie: \"red\") or its RGBa code (ie: \"rgba(255,0,0,1)\").  # noqa: E501

        :return: The text_color of this PdfAlignedTextParameters.  # noqa: E501
        :rtype: str
        """
        return self._text_color

    @text_color.setter
    def text_color(self, text_color):
        """Sets the text_color of this PdfAlignedTextParameters.

        Specifies the color of the text, using the color name (ie: \"red\") or its RGBa code (ie: \"rgba(255,0,0,1)\").  # noqa: E501

        :param text_color: The text_color of this PdfAlignedTextParameters.  # noqa: E501
        :type: str
        """

        self._text_color = text_color

    @property
    def font_name(self):
        """Gets the font_name of this PdfAlignedTextParameters.  # noqa: E501

        Specifies the name of the font to be used.  # noqa: E501

        :return: The font_name of this PdfAlignedTextParameters.  # noqa: E501
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        """Sets the font_name of this PdfAlignedTextParameters.

        Specifies the name of the font to be used.  # noqa: E501

        :param font_name: The font_name of this PdfAlignedTextParameters.  # noqa: E501
        :type: str
        """

        self._font_name = font_name

    @property
    def standard_font_name(self):
        """Gets the standard_font_name of this PdfAlignedTextParameters.  # noqa: E501


        :return: The standard_font_name of this PdfAlignedTextParameters.  # noqa: E501
        :rtype: StandardFontName
        """
        return self._standard_font_name

    @standard_font_name.setter
    def standard_font_name(self, standard_font_name):
        """Sets the standard_font_name of this PdfAlignedTextParameters.


        :param standard_font_name: The standard_font_name of this PdfAlignedTextParameters.  # noqa: E501
        :type: StandardFontName
        """

        self._standard_font_name = standard_font_name

    @property
    def font_style(self):
        """Gets the font_style of this PdfAlignedTextParameters.  # noqa: E501


        :return: The font_style of this PdfAlignedTextParameters.  # noqa: E501
        :rtype: FontStyle
        """
        return self._font_style

    @font_style.setter
    def font_style(self, font_style):
        """Sets the font_style of this PdfAlignedTextParameters.


        :param font_style: The font_style of this PdfAlignedTextParameters.  # noqa: E501
        :type: FontStyle
        """

        self._font_style = font_style

    @property
    def font_size(self):
        """Gets the font_size of this PdfAlignedTextParameters.  # noqa: E501

        Specifies the size of the font.  # noqa: E501

        :return: The font_size of this PdfAlignedTextParameters.  # noqa: E501
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this PdfAlignedTextParameters.

        Specifies the size of the font.  # noqa: E501

        :param font_size: The font_size of this PdfAlignedTextParameters.  # noqa: E501
        :type: int
        """

        self._font_size = font_size

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
        if not isinstance(other, PdfAlignedTextParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PdfAlignedTextParameters):
            return True

        return self.to_dict() != other.to_dict()