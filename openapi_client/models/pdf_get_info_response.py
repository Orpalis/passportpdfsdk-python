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


class PdfGetInfoResponse(object):
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
        'error': 'Error',
        'remaining_tokens': 'int',
        'page_count': 'int',
        'version': 'str',
        'author': 'str',
        'title': 'str',
        'subject': 'str',
        'producer': 'str',
        'metadata': 'str',
        'keywords': 'str',
        'has_user_password': 'bool',
        'has_owner_password': 'bool',
        'encryption': 'EncryptionAlgorithm',
        'can_print': 'bool',
        'can_copy': 'bool',
        'can_modify': 'bool',
        'can_add_notes': 'bool',
        'can_fill_fields': 'bool',
        'can_copy_access': 'bool',
        'can_assemble': 'bool',
        'can_print_full': 'bool'
    }

    attribute_map = {
        'error': 'Error',
        'remaining_tokens': 'RemainingTokens',
        'page_count': 'PageCount',
        'version': 'Version',
        'author': 'Author',
        'title': 'Title',
        'subject': 'Subject',
        'producer': 'Producer',
        'metadata': 'Metadata',
        'keywords': 'Keywords',
        'has_user_password': 'HasUserPassword',
        'has_owner_password': 'HasOwnerPassword',
        'encryption': 'Encryption',
        'can_print': 'CanPrint',
        'can_copy': 'CanCopy',
        'can_modify': 'CanModify',
        'can_add_notes': 'CanAddNotes',
        'can_fill_fields': 'CanFillFields',
        'can_copy_access': 'CanCopyAccess',
        'can_assemble': 'CanAssemble',
        'can_print_full': 'CanPrintFull'
    }

    def __init__(self, error=None, remaining_tokens=None, page_count=None, version=None, author=None, title=None, subject=None, producer=None, metadata=None, keywords=None, has_user_password=None, has_owner_password=None, encryption=None, can_print=None, can_copy=None, can_modify=None, can_add_notes=None, can_fill_fields=None, can_copy_access=None, can_assemble=None, can_print_full=None, local_vars_configuration=None):  # noqa: E501
        """PdfGetInfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._remaining_tokens = None
        self._page_count = None
        self._version = None
        self._author = None
        self._title = None
        self._subject = None
        self._producer = None
        self._metadata = None
        self._keywords = None
        self._has_user_password = None
        self._has_owner_password = None
        self._encryption = None
        self._can_print = None
        self._can_copy = None
        self._can_modify = None
        self._can_add_notes = None
        self._can_fill_fields = None
        self._can_copy_access = None
        self._can_assemble = None
        self._can_print_full = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if remaining_tokens is not None:
            self.remaining_tokens = remaining_tokens
        if page_count is not None:
            self.page_count = page_count
        self.version = version
        self.author = author
        self.title = title
        self.subject = subject
        self.producer = producer
        self.metadata = metadata
        self.keywords = keywords
        if has_user_password is not None:
            self.has_user_password = has_user_password
        if has_owner_password is not None:
            self.has_owner_password = has_owner_password
        if encryption is not None:
            self.encryption = encryption
        if can_print is not None:
            self.can_print = can_print
        if can_copy is not None:
            self.can_copy = can_copy
        if can_modify is not None:
            self.can_modify = can_modify
        if can_add_notes is not None:
            self.can_add_notes = can_add_notes
        if can_fill_fields is not None:
            self.can_fill_fields = can_fill_fields
        if can_copy_access is not None:
            self.can_copy_access = can_copy_access
        if can_assemble is not None:
            self.can_assemble = can_assemble
        if can_print_full is not None:
            self.can_print_full = can_print_full

    @property
    def error(self):
        """Gets the error of this PdfGetInfoResponse.  # noqa: E501


        :return: The error of this PdfGetInfoResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PdfGetInfoResponse.


        :param error: The error of this PdfGetInfoResponse.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def remaining_tokens(self):
        """Gets the remaining_tokens of this PdfGetInfoResponse.  # noqa: E501

        Specifies the number of remaining tokens.  # noqa: E501

        :return: The remaining_tokens of this PdfGetInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._remaining_tokens

    @remaining_tokens.setter
    def remaining_tokens(self, remaining_tokens):
        """Sets the remaining_tokens of this PdfGetInfoResponse.

        Specifies the number of remaining tokens.  # noqa: E501

        :param remaining_tokens: The remaining_tokens of this PdfGetInfoResponse.  # noqa: E501
        :type: int
        """

        self._remaining_tokens = remaining_tokens

    @property
    def page_count(self):
        """Gets the page_count of this PdfGetInfoResponse.  # noqa: E501

        Specifies the number of pages of the PDF.  # noqa: E501

        :return: The page_count of this PdfGetInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this PdfGetInfoResponse.

        Specifies the number of pages of the PDF.  # noqa: E501

        :param page_count: The page_count of this PdfGetInfoResponse.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def version(self):
        """Gets the version of this PdfGetInfoResponse.  # noqa: E501

        Specifies the version of the PDF.  # noqa: E501

        :return: The version of this PdfGetInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PdfGetInfoResponse.

        Specifies the version of the PDF.  # noqa: E501

        :param version: The version of this PdfGetInfoResponse.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def author(self):
        """Gets the author of this PdfGetInfoResponse.  # noqa: E501

        Specifies the author name specified within the PDF, if any.  # noqa: E501

        :return: The author of this PdfGetInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this PdfGetInfoResponse.

        Specifies the author name specified within the PDF, if any.  # noqa: E501

        :param author: The author of this PdfGetInfoResponse.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def title(self):
        """Gets the title of this PdfGetInfoResponse.  # noqa: E501

        Specifies the document title specified within the PDF, if any.  # noqa: E501

        :return: The title of this PdfGetInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PdfGetInfoResponse.

        Specifies the document title specified within the PDF, if any.  # noqa: E501

        :param title: The title of this PdfGetInfoResponse.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def subject(self):
        """Gets the subject of this PdfGetInfoResponse.  # noqa: E501

        Specifies the document subject specified within the PDF, if any.  # noqa: E501

        :return: The subject of this PdfGetInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PdfGetInfoResponse.

        Specifies the document subject specified within the PDF, if any.  # noqa: E501

        :param subject: The subject of this PdfGetInfoResponse.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def producer(self):
        """Gets the producer of this PdfGetInfoResponse.  # noqa: E501

        Specifies the producer name specified within the PDF, if any.  # noqa: E501

        :return: The producer of this PdfGetInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this PdfGetInfoResponse.

        Specifies the producer name specified within the PDF, if any.  # noqa: E501

        :param producer: The producer of this PdfGetInfoResponse.  # noqa: E501
        :type: str
        """

        self._producer = producer

    @property
    def metadata(self):
        """Gets the metadata of this PdfGetInfoResponse.  # noqa: E501

        Specifies the metadata contained within the PDF, if any.  # noqa: E501

        :return: The metadata of this PdfGetInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PdfGetInfoResponse.

        Specifies the metadata contained within the PDF, if any.  # noqa: E501

        :param metadata: The metadata of this PdfGetInfoResponse.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def keywords(self):
        """Gets the keywords of this PdfGetInfoResponse.  # noqa: E501

        Specifies the keywords associated with the PDF, if any.  # noqa: E501

        :return: The keywords of this PdfGetInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this PdfGetInfoResponse.

        Specifies the keywords associated with the PDF, if any.  # noqa: E501

        :param keywords: The keywords of this PdfGetInfoResponse.  # noqa: E501
        :type: str
        """

        self._keywords = keywords

    @property
    def has_user_password(self):
        """Gets the has_user_password of this PdfGetInfoResponse.  # noqa: E501

        Specifies if the PDF is protected with a user password.  # noqa: E501

        :return: The has_user_password of this PdfGetInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_user_password

    @has_user_password.setter
    def has_user_password(self, has_user_password):
        """Sets the has_user_password of this PdfGetInfoResponse.

        Specifies if the PDF is protected with a user password.  # noqa: E501

        :param has_user_password: The has_user_password of this PdfGetInfoResponse.  # noqa: E501
        :type: bool
        """

        self._has_user_password = has_user_password

    @property
    def has_owner_password(self):
        """Gets the has_owner_password of this PdfGetInfoResponse.  # noqa: E501

        Specifies if the PDF is protected with a owner password.  # noqa: E501

        :return: The has_owner_password of this PdfGetInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_owner_password

    @has_owner_password.setter
    def has_owner_password(self, has_owner_password):
        """Sets the has_owner_password of this PdfGetInfoResponse.

        Specifies if the PDF is protected with a owner password.  # noqa: E501

        :param has_owner_password: The has_owner_password of this PdfGetInfoResponse.  # noqa: E501
        :type: bool
        """

        self._has_owner_password = has_owner_password

    @property
    def encryption(self):
        """Gets the encryption of this PdfGetInfoResponse.  # noqa: E501


        :return: The encryption of this PdfGetInfoResponse.  # noqa: E501
        :rtype: EncryptionAlgorithm
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this PdfGetInfoResponse.


        :param encryption: The encryption of this PdfGetInfoResponse.  # noqa: E501
        :type: EncryptionAlgorithm
        """

        self._encryption = encryption

    @property
    def can_print(self):
        """Gets the can_print of this PdfGetInfoResponse.  # noqa: E501

        Specifies if the user is allowed to print the document, but possibly not at the highest quality level.  # noqa: E501

        :return: The can_print of this PdfGetInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._can_print

    @can_print.setter
    def can_print(self, can_print):
        """Sets the can_print of this PdfGetInfoResponse.

        Specifies if the user is allowed to print the document, but possibly not at the highest quality level.  # noqa: E501

        :param can_print: The can_print of this PdfGetInfoResponse.  # noqa: E501
        :type: bool
        """

        self._can_print = can_print

    @property
    def can_copy(self):
        """Gets the can_copy of this PdfGetInfoResponse.  # noqa: E501

        Specifies if the user is allowed to copy or extract text and graphics from the document.  # noqa: E501

        :return: The can_copy of this PdfGetInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._can_copy

    @can_copy.setter
    def can_copy(self, can_copy):
        """Sets the can_copy of this PdfGetInfoResponse.

        Specifies if the user is allowed to copy or extract text and graphics from the document.  # noqa: E501

        :param can_copy: The can_copy of this PdfGetInfoResponse.  # noqa: E501
        :type: bool
        """

        self._can_copy = can_copy

    @property
    def can_modify(self):
        """Gets the can_modify of this PdfGetInfoResponse.  # noqa: E501

        Specifies if the user is allowed to modify the document.  # noqa: E501

        :return: The can_modify of this PdfGetInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._can_modify

    @can_modify.setter
    def can_modify(self, can_modify):
        """Sets the can_modify of this PdfGetInfoResponse.

        Specifies if the user is allowed to modify the document.  # noqa: E501

        :param can_modify: The can_modify of this PdfGetInfoResponse.  # noqa: E501
        :type: bool
        """

        self._can_modify = can_modify

    @property
    def can_add_notes(self):
        """Gets the can_add_notes of this PdfGetInfoResponse.  # noqa: E501

        Specifies if the user is allowed to add annotations.  # noqa: E501

        :return: The can_add_notes of this PdfGetInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._can_add_notes

    @can_add_notes.setter
    def can_add_notes(self, can_add_notes):
        """Sets the can_add_notes of this PdfGetInfoResponse.

        Specifies if the user is allowed to add annotations.  # noqa: E501

        :param can_add_notes: The can_add_notes of this PdfGetInfoResponse.  # noqa: E501
        :type: bool
        """

        self._can_add_notes = can_add_notes

    @property
    def can_fill_fields(self):
        """Gets the can_fill_fields of this PdfGetInfoResponse.  # noqa: E501

        Specifies if the user is allowed to fill-in form fields.  # noqa: E501

        :return: The can_fill_fields of this PdfGetInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._can_fill_fields

    @can_fill_fields.setter
    def can_fill_fields(self, can_fill_fields):
        """Sets the can_fill_fields of this PdfGetInfoResponse.

        Specifies if the user is allowed to fill-in form fields.  # noqa: E501

        :param can_fill_fields: The can_fill_fields of this PdfGetInfoResponse.  # noqa: E501
        :type: bool
        """

        self._can_fill_fields = can_fill_fields

    @property
    def can_copy_access(self):
        """Gets the can_copy_access of this PdfGetInfoResponse.  # noqa: E501

        Specifies if the user is allowed for copying or extracting for use with accessibility features.  # noqa: E501

        :return: The can_copy_access of this PdfGetInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._can_copy_access

    @can_copy_access.setter
    def can_copy_access(self, can_copy_access):
        """Sets the can_copy_access of this PdfGetInfoResponse.

        Specifies if the user is allowed for copying or extracting for use with accessibility features.  # noqa: E501

        :param can_copy_access: The can_copy_access of this PdfGetInfoResponse.  # noqa: E501
        :type: bool
        """

        self._can_copy_access = can_copy_access

    @property
    def can_assemble(self):
        """Gets the can_assemble of this PdfGetInfoResponse.  # noqa: E501

        Specifies if the user is allowed to assemble the document.  # noqa: E501

        :return: The can_assemble of this PdfGetInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._can_assemble

    @can_assemble.setter
    def can_assemble(self, can_assemble):
        """Sets the can_assemble of this PdfGetInfoResponse.

        Specifies if the user is allowed to assemble the document.  # noqa: E501

        :param can_assemble: The can_assemble of this PdfGetInfoResponse.  # noqa: E501
        :type: bool
        """

        self._can_assemble = can_assemble

    @property
    def can_print_full(self):
        """Gets the can_print_full of this PdfGetInfoResponse.  # noqa: E501

        Specifies if the user is allowed to print the document with high resolution.  # noqa: E501

        :return: The can_print_full of this PdfGetInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._can_print_full

    @can_print_full.setter
    def can_print_full(self, can_print_full):
        """Sets the can_print_full of this PdfGetInfoResponse.

        Specifies if the user is allowed to print the document with high resolution.  # noqa: E501

        :param can_print_full: The can_print_full of this PdfGetInfoResponse.  # noqa: E501
        :type: bool
        """

        self._can_print_full = can_print_full

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
        if not isinstance(other, PdfGetInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PdfGetInfoResponse):
            return True

        return self.to_dict() != other.to_dict()