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


class PdfDigiSignParameters(object):
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
        'certificate_data': 'str',
        'certificate_password': 'str',
        'signature_mode': 'SignatureMode',
        'signature_certification_level': 'SignatureCertificationLevel',
        'signature_hash_algorithm': 'SignatureHash',
        'signer_name': 'str',
        'reason': 'str',
        'location': 'str',
        'contact_info': 'str',
        'time_stamp_url': 'str',
        'time_stamp_user_name': 'str',
        'time_stamp_password': 'str',
        'linearize': 'bool',
        'draw_signature': 'bool',
        'page_number': 'int',
        'show_validation_mark': 'bool',
        'image_data': 'str',
        'signature_layout': 'DrawableContentLayoutParameters',
        'signature_text': 'PdfAlignedTextParameters'
    }

    attribute_map = {
        'file_id': 'FileId',
        'certificate_data': 'CertificateData',
        'certificate_password': 'CertificatePassword',
        'signature_mode': 'SignatureMode',
        'signature_certification_level': 'SignatureCertificationLevel',
        'signature_hash_algorithm': 'SignatureHashAlgorithm',
        'signer_name': 'SignerName',
        'reason': 'Reason',
        'location': 'Location',
        'contact_info': 'ContactInfo',
        'time_stamp_url': 'TimeStampURL',
        'time_stamp_user_name': 'TimeStampUserName',
        'time_stamp_password': 'TimeStampPassword',
        'linearize': 'Linearize',
        'draw_signature': 'DrawSignature',
        'page_number': 'PageNumber',
        'show_validation_mark': 'ShowValidationMark',
        'image_data': 'ImageData',
        'signature_layout': 'SignatureLayout',
        'signature_text': 'SignatureText'
    }

    def __init__(self, file_id=None, certificate_data=None, certificate_password=None, signature_mode=None, signature_certification_level=None, signature_hash_algorithm=None, signer_name='PassportPDF', reason='', location='', contact_info='', time_stamp_url='', time_stamp_user_name='', time_stamp_password='', linearize=False, draw_signature=False, page_number=1, show_validation_mark=False, image_data=None, signature_layout=None, signature_text=None, local_vars_configuration=None):  # noqa: E501
        """PdfDigiSignParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._certificate_data = None
        self._certificate_password = None
        self._signature_mode = None
        self._signature_certification_level = None
        self._signature_hash_algorithm = None
        self._signer_name = None
        self._reason = None
        self._location = None
        self._contact_info = None
        self._time_stamp_url = None
        self._time_stamp_user_name = None
        self._time_stamp_password = None
        self._linearize = None
        self._draw_signature = None
        self._page_number = None
        self._show_validation_mark = None
        self._image_data = None
        self._signature_layout = None
        self._signature_text = None
        self.discriminator = None

        self.file_id = file_id
        self.certificate_data = certificate_data
        self.certificate_password = certificate_password
        if signature_mode is not None:
            self.signature_mode = signature_mode
        if signature_certification_level is not None:
            self.signature_certification_level = signature_certification_level
        if signature_hash_algorithm is not None:
            self.signature_hash_algorithm = signature_hash_algorithm
        self.signer_name = signer_name
        self.reason = reason
        self.location = location
        self.contact_info = contact_info
        self.time_stamp_url = time_stamp_url
        self.time_stamp_user_name = time_stamp_user_name
        self.time_stamp_password = time_stamp_password
        if linearize is not None:
            self.linearize = linearize
        if draw_signature is not None:
            self.draw_signature = draw_signature
        if page_number is not None:
            self.page_number = page_number
        if show_validation_mark is not None:
            self.show_validation_mark = show_validation_mark
        self.image_data = image_data
        if signature_layout is not None:
            self.signature_layout = signature_layout
        if signature_text is not None:
            self.signature_text = signature_text

    @property
    def file_id(self):
        """Gets the file_id of this PdfDigiSignParameters.  # noqa: E501

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :return: The file_id of this PdfDigiSignParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this PdfDigiSignParameters.

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :param file_id: The file_id of this PdfDigiSignParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def certificate_data(self):
        """Gets the certificate_data of this PdfDigiSignParameters.  # noqa: E501

        Specifies the data of the digital PKCS#12 certificate file.  # noqa: E501

        :return: The certificate_data of this PdfDigiSignParameters.  # noqa: E501
        :rtype: str
        """
        return self._certificate_data

    @certificate_data.setter
    def certificate_data(self, certificate_data):
        """Sets the certificate_data of this PdfDigiSignParameters.

        Specifies the data of the digital PKCS#12 certificate file.  # noqa: E501

        :param certificate_data: The certificate_data of this PdfDigiSignParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and certificate_data is None:  # noqa: E501
            raise ValueError("Invalid value for `certificate_data`, must not be `None`")  # noqa: E501

        self._certificate_data = certificate_data

    @property
    def certificate_password(self):
        """Gets the certificate_password of this PdfDigiSignParameters.  # noqa: E501

        Specifies the certificate password.  # noqa: E501

        :return: The certificate_password of this PdfDigiSignParameters.  # noqa: E501
        :rtype: str
        """
        return self._certificate_password

    @certificate_password.setter
    def certificate_password(self, certificate_password):
        """Sets the certificate_password of this PdfDigiSignParameters.

        Specifies the certificate password.  # noqa: E501

        :param certificate_password: The certificate_password of this PdfDigiSignParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and certificate_password is None:  # noqa: E501
            raise ValueError("Invalid value for `certificate_password`, must not be `None`")  # noqa: E501

        self._certificate_password = certificate_password

    @property
    def signature_mode(self):
        """Gets the signature_mode of this PdfDigiSignParameters.  # noqa: E501


        :return: The signature_mode of this PdfDigiSignParameters.  # noqa: E501
        :rtype: SignatureMode
        """
        return self._signature_mode

    @signature_mode.setter
    def signature_mode(self, signature_mode):
        """Sets the signature_mode of this PdfDigiSignParameters.


        :param signature_mode: The signature_mode of this PdfDigiSignParameters.  # noqa: E501
        :type: SignatureMode
        """

        self._signature_mode = signature_mode

    @property
    def signature_certification_level(self):
        """Gets the signature_certification_level of this PdfDigiSignParameters.  # noqa: E501


        :return: The signature_certification_level of this PdfDigiSignParameters.  # noqa: E501
        :rtype: SignatureCertificationLevel
        """
        return self._signature_certification_level

    @signature_certification_level.setter
    def signature_certification_level(self, signature_certification_level):
        """Sets the signature_certification_level of this PdfDigiSignParameters.


        :param signature_certification_level: The signature_certification_level of this PdfDigiSignParameters.  # noqa: E501
        :type: SignatureCertificationLevel
        """

        self._signature_certification_level = signature_certification_level

    @property
    def signature_hash_algorithm(self):
        """Gets the signature_hash_algorithm of this PdfDigiSignParameters.  # noqa: E501


        :return: The signature_hash_algorithm of this PdfDigiSignParameters.  # noqa: E501
        :rtype: SignatureHash
        """
        return self._signature_hash_algorithm

    @signature_hash_algorithm.setter
    def signature_hash_algorithm(self, signature_hash_algorithm):
        """Sets the signature_hash_algorithm of this PdfDigiSignParameters.


        :param signature_hash_algorithm: The signature_hash_algorithm of this PdfDigiSignParameters.  # noqa: E501
        :type: SignatureHash
        """

        self._signature_hash_algorithm = signature_hash_algorithm

    @property
    def signer_name(self):
        """Gets the signer_name of this PdfDigiSignParameters.  # noqa: E501

        Specifies the name of the signer.  # noqa: E501

        :return: The signer_name of this PdfDigiSignParameters.  # noqa: E501
        :rtype: str
        """
        return self._signer_name

    @signer_name.setter
    def signer_name(self, signer_name):
        """Sets the signer_name of this PdfDigiSignParameters.

        Specifies the name of the signer.  # noqa: E501

        :param signer_name: The signer_name of this PdfDigiSignParameters.  # noqa: E501
        :type: str
        """

        self._signer_name = signer_name

    @property
    def reason(self):
        """Gets the reason of this PdfDigiSignParameters.  # noqa: E501

        Specifies the reason of the signature.  # noqa: E501

        :return: The reason of this PdfDigiSignParameters.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PdfDigiSignParameters.

        Specifies the reason of the signature.  # noqa: E501

        :param reason: The reason of this PdfDigiSignParameters.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def location(self):
        """Gets the location of this PdfDigiSignParameters.  # noqa: E501

        Specifies the location where the signature is applied.  # noqa: E501

        :return: The location of this PdfDigiSignParameters.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PdfDigiSignParameters.

        Specifies the location where the signature is applied.  # noqa: E501

        :param location: The location of this PdfDigiSignParameters.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def contact_info(self):
        """Gets the contact_info of this PdfDigiSignParameters.  # noqa: E501

        Specifies contact information about the signer.  # noqa: E501

        :return: The contact_info of this PdfDigiSignParameters.  # noqa: E501
        :rtype: str
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        """Sets the contact_info of this PdfDigiSignParameters.

        Specifies contact information about the signer.  # noqa: E501

        :param contact_info: The contact_info of this PdfDigiSignParameters.  # noqa: E501
        :type: str
        """

        self._contact_info = contact_info

    @property
    def time_stamp_url(self):
        """Gets the time_stamp_url of this PdfDigiSignParameters.  # noqa: E501

        Specifies the URL of the server responsible of providing a time stamp.  # noqa: E501

        :return: The time_stamp_url of this PdfDigiSignParameters.  # noqa: E501
        :rtype: str
        """
        return self._time_stamp_url

    @time_stamp_url.setter
    def time_stamp_url(self, time_stamp_url):
        """Sets the time_stamp_url of this PdfDigiSignParameters.

        Specifies the URL of the server responsible of providing a time stamp.  # noqa: E501

        :param time_stamp_url: The time_stamp_url of this PdfDigiSignParameters.  # noqa: E501
        :type: str
        """

        self._time_stamp_url = time_stamp_url

    @property
    def time_stamp_user_name(self):
        """Gets the time_stamp_user_name of this PdfDigiSignParameters.  # noqa: E501

        Specifies the optional user name associated with the time stamp server.  # noqa: E501

        :return: The time_stamp_user_name of this PdfDigiSignParameters.  # noqa: E501
        :rtype: str
        """
        return self._time_stamp_user_name

    @time_stamp_user_name.setter
    def time_stamp_user_name(self, time_stamp_user_name):
        """Sets the time_stamp_user_name of this PdfDigiSignParameters.

        Specifies the optional user name associated with the time stamp server.  # noqa: E501

        :param time_stamp_user_name: The time_stamp_user_name of this PdfDigiSignParameters.  # noqa: E501
        :type: str
        """

        self._time_stamp_user_name = time_stamp_user_name

    @property
    def time_stamp_password(self):
        """Gets the time_stamp_password of this PdfDigiSignParameters.  # noqa: E501

        Specifies the optional password associated with the time stamp server.  # noqa: E501

        :return: The time_stamp_password of this PdfDigiSignParameters.  # noqa: E501
        :rtype: str
        """
        return self._time_stamp_password

    @time_stamp_password.setter
    def time_stamp_password(self, time_stamp_password):
        """Sets the time_stamp_password of this PdfDigiSignParameters.

        Specifies the optional password associated with the time stamp server.  # noqa: E501

        :param time_stamp_password: The time_stamp_password of this PdfDigiSignParameters.  # noqa: E501
        :type: str
        """

        self._time_stamp_password = time_stamp_password

    @property
    def linearize(self):
        """Gets the linearize of this PdfDigiSignParameters.  # noqa: E501

        Specifies whether the signed PDF shall be linearized.  # noqa: E501

        :return: The linearize of this PdfDigiSignParameters.  # noqa: E501
        :rtype: bool
        """
        return self._linearize

    @linearize.setter
    def linearize(self, linearize):
        """Sets the linearize of this PdfDigiSignParameters.

        Specifies whether the signed PDF shall be linearized.  # noqa: E501

        :param linearize: The linearize of this PdfDigiSignParameters.  # noqa: E501
        :type: bool
        """

        self._linearize = linearize

    @property
    def draw_signature(self):
        """Gets the draw_signature of this PdfDigiSignParameters.  # noqa: E501

        Specifies whether the signature shall be drawn on the document.  # noqa: E501

        :return: The draw_signature of this PdfDigiSignParameters.  # noqa: E501
        :rtype: bool
        """
        return self._draw_signature

    @draw_signature.setter
    def draw_signature(self, draw_signature):
        """Sets the draw_signature of this PdfDigiSignParameters.

        Specifies whether the signature shall be drawn on the document.  # noqa: E501

        :param draw_signature: The draw_signature of this PdfDigiSignParameters.  # noqa: E501
        :type: bool
        """

        self._draw_signature = draw_signature

    @property
    def page_number(self):
        """Gets the page_number of this PdfDigiSignParameters.  # noqa: E501

        Specifies the number of the page on which the signature shall be drawn.  # noqa: E501

        :return: The page_number of this PdfDigiSignParameters.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this PdfDigiSignParameters.

        Specifies the number of the page on which the signature shall be drawn.  # noqa: E501

        :param page_number: The page_number of this PdfDigiSignParameters.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def show_validation_mark(self):
        """Gets the show_validation_mark of this PdfDigiSignParameters.  # noqa: E501

        Specifies whether a validation mark shall be drawn with the signature.  # noqa: E501

        :return: The show_validation_mark of this PdfDigiSignParameters.  # noqa: E501
        :rtype: bool
        """
        return self._show_validation_mark

    @show_validation_mark.setter
    def show_validation_mark(self, show_validation_mark):
        """Sets the show_validation_mark of this PdfDigiSignParameters.

        Specifies whether a validation mark shall be drawn with the signature.  # noqa: E501

        :param show_validation_mark: The show_validation_mark of this PdfDigiSignParameters.  # noqa: E501
        :type: bool
        """

        self._show_validation_mark = show_validation_mark

    @property
    def image_data(self):
        """Gets the image_data of this PdfDigiSignParameters.  # noqa: E501

        Specifies the data of the image to be drawn at the signature location.  # noqa: E501

        :return: The image_data of this PdfDigiSignParameters.  # noqa: E501
        :rtype: str
        """
        return self._image_data

    @image_data.setter
    def image_data(self, image_data):
        """Sets the image_data of this PdfDigiSignParameters.

        Specifies the data of the image to be drawn at the signature location.  # noqa: E501

        :param image_data: The image_data of this PdfDigiSignParameters.  # noqa: E501
        :type: str
        """

        self._image_data = image_data

    @property
    def signature_layout(self):
        """Gets the signature_layout of this PdfDigiSignParameters.  # noqa: E501


        :return: The signature_layout of this PdfDigiSignParameters.  # noqa: E501
        :rtype: DrawableContentLayoutParameters
        """
        return self._signature_layout

    @signature_layout.setter
    def signature_layout(self, signature_layout):
        """Sets the signature_layout of this PdfDigiSignParameters.


        :param signature_layout: The signature_layout of this PdfDigiSignParameters.  # noqa: E501
        :type: DrawableContentLayoutParameters
        """

        self._signature_layout = signature_layout

    @property
    def signature_text(self):
        """Gets the signature_text of this PdfDigiSignParameters.  # noqa: E501


        :return: The signature_text of this PdfDigiSignParameters.  # noqa: E501
        :rtype: PdfAlignedTextParameters
        """
        return self._signature_text

    @signature_text.setter
    def signature_text(self, signature_text):
        """Sets the signature_text of this PdfDigiSignParameters.


        :param signature_text: The signature_text of this PdfDigiSignParameters.  # noqa: E501
        :type: PdfAlignedTextParameters
        """

        self._signature_text = signature_text

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
        if not isinstance(other, PdfDigiSignParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PdfDigiSignParameters):
            return True

        return self.to_dict() != other.to_dict()