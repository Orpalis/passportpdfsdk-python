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


class PdfSetInitialViewParameters(object):
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
        'page_mode': 'PdfInitViewPageMode',
        'layout_mode': 'PdfInitViewLayoutMode',
        'non_full_screen_page_mode': 'PdfInitViewNonFullScreenPageMode',
        'open_page': 'int',
        'open_zoom': 'float',
        'hide_toolbar': 'bool',
        'hide_menubar': 'bool',
        'hide_window_ui': 'bool',
        'fit_window': 'bool',
        'center_window': 'bool',
        'display_doc_title': 'bool'
    }

    attribute_map = {
        'file_id': 'FileId',
        'page_mode': 'PageMode',
        'layout_mode': 'LayoutMode',
        'non_full_screen_page_mode': 'NonFullScreenPageMode',
        'open_page': 'OpenPage',
        'open_zoom': 'OpenZoom',
        'hide_toolbar': 'HideToolbar',
        'hide_menubar': 'HideMenubar',
        'hide_window_ui': 'HideWindowUI',
        'fit_window': 'FitWindow',
        'center_window': 'CenterWindow',
        'display_doc_title': 'DisplayDocTitle'
    }

    def __init__(self, file_id=None, page_mode=None, layout_mode=None, non_full_screen_page_mode=None, open_page=1, open_zoom=1, hide_toolbar=False, hide_menubar=False, hide_window_ui=False, fit_window=False, center_window=False, display_doc_title=False, local_vars_configuration=None):  # noqa: E501
        """PdfSetInitialViewParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._page_mode = None
        self._layout_mode = None
        self._non_full_screen_page_mode = None
        self._open_page = None
        self._open_zoom = None
        self._hide_toolbar = None
        self._hide_menubar = None
        self._hide_window_ui = None
        self._fit_window = None
        self._center_window = None
        self._display_doc_title = None
        self.discriminator = None

        self.file_id = file_id
        if page_mode is not None:
            self.page_mode = page_mode
        if layout_mode is not None:
            self.layout_mode = layout_mode
        if non_full_screen_page_mode is not None:
            self.non_full_screen_page_mode = non_full_screen_page_mode
        if open_page is not None:
            self.open_page = open_page
        if open_zoom is not None:
            self.open_zoom = open_zoom
        if hide_toolbar is not None:
            self.hide_toolbar = hide_toolbar
        if hide_menubar is not None:
            self.hide_menubar = hide_menubar
        if hide_window_ui is not None:
            self.hide_window_ui = hide_window_ui
        if fit_window is not None:
            self.fit_window = fit_window
        if center_window is not None:
            self.center_window = center_window
        if display_doc_title is not None:
            self.display_doc_title = display_doc_title

    @property
    def file_id(self):
        """Gets the file_id of this PdfSetInitialViewParameters.  # noqa: E501

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :return: The file_id of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this PdfSetInitialViewParameters.

        The identifier of the previously uploaded file to be processed.  # noqa: E501

        :param file_id: The file_id of this PdfSetInitialViewParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def page_mode(self):
        """Gets the page_mode of this PdfSetInitialViewParameters.  # noqa: E501


        :return: The page_mode of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: PdfInitViewPageMode
        """
        return self._page_mode

    @page_mode.setter
    def page_mode(self, page_mode):
        """Sets the page_mode of this PdfSetInitialViewParameters.


        :param page_mode: The page_mode of this PdfSetInitialViewParameters.  # noqa: E501
        :type: PdfInitViewPageMode
        """

        self._page_mode = page_mode

    @property
    def layout_mode(self):
        """Gets the layout_mode of this PdfSetInitialViewParameters.  # noqa: E501


        :return: The layout_mode of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: PdfInitViewLayoutMode
        """
        return self._layout_mode

    @layout_mode.setter
    def layout_mode(self, layout_mode):
        """Sets the layout_mode of this PdfSetInitialViewParameters.


        :param layout_mode: The layout_mode of this PdfSetInitialViewParameters.  # noqa: E501
        :type: PdfInitViewLayoutMode
        """

        self._layout_mode = layout_mode

    @property
    def non_full_screen_page_mode(self):
        """Gets the non_full_screen_page_mode of this PdfSetInitialViewParameters.  # noqa: E501


        :return: The non_full_screen_page_mode of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: PdfInitViewNonFullScreenPageMode
        """
        return self._non_full_screen_page_mode

    @non_full_screen_page_mode.setter
    def non_full_screen_page_mode(self, non_full_screen_page_mode):
        """Sets the non_full_screen_page_mode of this PdfSetInitialViewParameters.


        :param non_full_screen_page_mode: The non_full_screen_page_mode of this PdfSetInitialViewParameters.  # noqa: E501
        :type: PdfInitViewNonFullScreenPageMode
        """

        self._non_full_screen_page_mode = non_full_screen_page_mode

    @property
    def open_page(self):
        """Gets the open_page of this PdfSetInitialViewParameters.  # noqa: E501

        Specifies which page should be displayed when the document is opened.  # noqa: E501

        :return: The open_page of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: int
        """
        return self._open_page

    @open_page.setter
    def open_page(self, open_page):
        """Sets the open_page of this PdfSetInitialViewParameters.

        Specifies which page should be displayed when the document is opened.  # noqa: E501

        :param open_page: The open_page of this PdfSetInitialViewParameters.  # noqa: E501
        :type: int
        """

        self._open_page = open_page

    @property
    def open_zoom(self):
        """Gets the open_zoom of this PdfSetInitialViewParameters.  # noqa: E501

        Specifies the default zoom factor to be used when the document is opened. Value of 1 to represent the 100% zoom, 2 means 200%, 0,5 means 50%, etc.  # noqa: E501

        :return: The open_zoom of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: float
        """
        return self._open_zoom

    @open_zoom.setter
    def open_zoom(self, open_zoom):
        """Sets the open_zoom of this PdfSetInitialViewParameters.

        Specifies the default zoom factor to be used when the document is opened. Value of 1 to represent the 100% zoom, 2 means 200%, 0,5 means 50%, etc.  # noqa: E501

        :param open_zoom: The open_zoom of this PdfSetInitialViewParameters.  # noqa: E501
        :type: float
        """

        self._open_zoom = open_zoom

    @property
    def hide_toolbar(self):
        """Gets the hide_toolbar of this PdfSetInitialViewParameters.  # noqa: E501

        A flag specifying whether to hide the viewer application’s tool bars when the document is active. Default value: false.  # noqa: E501

        :return: The hide_toolbar of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: bool
        """
        return self._hide_toolbar

    @hide_toolbar.setter
    def hide_toolbar(self, hide_toolbar):
        """Sets the hide_toolbar of this PdfSetInitialViewParameters.

        A flag specifying whether to hide the viewer application’s tool bars when the document is active. Default value: false.  # noqa: E501

        :param hide_toolbar: The hide_toolbar of this PdfSetInitialViewParameters.  # noqa: E501
        :type: bool
        """

        self._hide_toolbar = hide_toolbar

    @property
    def hide_menubar(self):
        """Gets the hide_menubar of this PdfSetInitialViewParameters.  # noqa: E501

        (Optional) A flag specifying whether to hide the viewer application’s menu bar when the document is active. Default value: false.  # noqa: E501

        :return: The hide_menubar of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: bool
        """
        return self._hide_menubar

    @hide_menubar.setter
    def hide_menubar(self, hide_menubar):
        """Sets the hide_menubar of this PdfSetInitialViewParameters.

        (Optional) A flag specifying whether to hide the viewer application’s menu bar when the document is active. Default value: false.  # noqa: E501

        :param hide_menubar: The hide_menubar of this PdfSetInitialViewParameters.  # noqa: E501
        :type: bool
        """

        self._hide_menubar = hide_menubar

    @property
    def hide_window_ui(self):
        """Gets the hide_window_ui of this PdfSetInitialViewParameters.  # noqa: E501

        (Optional) A flag specifying whether to hide user interface elements in the document’s window (such as scroll bars and navigation controls),  leaving only the document’s contents displayed. Default value: false.  # noqa: E501

        :return: The hide_window_ui of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: bool
        """
        return self._hide_window_ui

    @hide_window_ui.setter
    def hide_window_ui(self, hide_window_ui):
        """Sets the hide_window_ui of this PdfSetInitialViewParameters.

        (Optional) A flag specifying whether to hide user interface elements in the document’s window (such as scroll bars and navigation controls),  leaving only the document’s contents displayed. Default value: false.  # noqa: E501

        :param hide_window_ui: The hide_window_ui of this PdfSetInitialViewParameters.  # noqa: E501
        :type: bool
        """

        self._hide_window_ui = hide_window_ui

    @property
    def fit_window(self):
        """Gets the fit_window of this PdfSetInitialViewParameters.  # noqa: E501

        (Optional) A flag specifying whether to resize the document’s window to fit the size of the first displayed page. Default value: false.  # noqa: E501

        :return: The fit_window of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: bool
        """
        return self._fit_window

    @fit_window.setter
    def fit_window(self, fit_window):
        """Sets the fit_window of this PdfSetInitialViewParameters.

        (Optional) A flag specifying whether to resize the document’s window to fit the size of the first displayed page. Default value: false.  # noqa: E501

        :param fit_window: The fit_window of this PdfSetInitialViewParameters.  # noqa: E501
        :type: bool
        """

        self._fit_window = fit_window

    @property
    def center_window(self):
        """Gets the center_window of this PdfSetInitialViewParameters.  # noqa: E501

        (Optional) A flag specifying whether to position the document’s window in the center of the screen. Default value: false.  # noqa: E501

        :return: The center_window of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: bool
        """
        return self._center_window

    @center_window.setter
    def center_window(self, center_window):
        """Sets the center_window of this PdfSetInitialViewParameters.

        (Optional) A flag specifying whether to position the document’s window in the center of the screen. Default value: false.  # noqa: E501

        :param center_window: The center_window of this PdfSetInitialViewParameters.  # noqa: E501
        :type: bool
        """

        self._center_window = center_window

    @property
    def display_doc_title(self):
        """Gets the display_doc_title of this PdfSetInitialViewParameters.  # noqa: E501

        (Optional; PDF 1.4) A flag specifying whether the window’s title bar should display the document title taken from the Title entry of the document information dictionary.  If false, the title bar should instead display the name of the PDF file containing the document. Default value: false.  # noqa: E501

        :return: The display_doc_title of this PdfSetInitialViewParameters.  # noqa: E501
        :rtype: bool
        """
        return self._display_doc_title

    @display_doc_title.setter
    def display_doc_title(self, display_doc_title):
        """Sets the display_doc_title of this PdfSetInitialViewParameters.

        (Optional; PDF 1.4) A flag specifying whether the window’s title bar should display the document title taken from the Title entry of the document information dictionary.  If false, the title bar should instead display the name of the PDF file containing the document. Default value: false.  # noqa: E501

        :param display_doc_title: The display_doc_title of this PdfSetInitialViewParameters.  # noqa: E501
        :type: bool
        """

        self._display_doc_title = display_doc_title

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
        if not isinstance(other, PdfSetInitialViewParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PdfSetInitialViewParameters):
            return True

        return self.to_dict() != other.to_dict()