# coding: utf-8

"""
    PassportPDF API

    Another brick in the cloud  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.pdf_api import PDFApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPDFApi(unittest.TestCase):
    """PDFApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.pdf_api.PDFApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_annotate(self):
        """Test case for annotate

        Annotates a previously uploaded document.  # noqa: E501
        """
        pass

    def test_auto_deskew(self):
        """Test case for auto_deskew

        Performs auto deskew on a page range of a previously uploaded document.  # noqa: E501
        """
        pass

    def test_clear_page(self):
        """Test case for clear_page

        Clears a page range from a previously uploaded document.  # noqa: E501
        """
        pass

    def test_clone_page(self):
        """Test case for clone_page

        Clones specific pages from a previously uploaded document to another previously uploaded document.  # noqa: E501
        """
        pass

    def test_close_pdf(self):
        """Test case for close_pdf

        Closes a previously uploaded document.  # noqa: E501
        """
        pass

    def test_convert_to_pdfa(self):
        """Test case for convert_to_pdfa

        Converts a previously uploaded document to PDF/A.  # noqa: E501
        """
        pass

    def test_delete_page(self):
        """Test case for delete_page

        Deletes a page range from a previously uploaded document.  # noqa: E501
        """
        pass

    def test_detect_page_orientation(self):
        """Test case for detect_page_orientation

        Detects the orientation of the page(s) of a previously uploaded document and offers to automatically rotate them.  # noqa: E501
        """
        pass

    def test_digi_sign(self):
        """Test case for digi_sign

        Signs a previously uploaded document digitally.  # noqa: E501
        """
        pass

    def test_draw_image(self):
        """Test case for draw_image

        Draws an image on a page range of a previously uploaded document.  # noqa: E501
        """
        pass

    def test_extract_page(self):
        """Test case for extract_page

        Extracts a page range from a previously uploaded document into one or several new documents.  # noqa: E501
        """
        pass

    def test_extract_text(self):
        """Test case for extract_text

        Extracts text from the document pages.  # noqa: E501
        """
        pass

    def test_flatten(self):
        """Test case for flatten

        Flattens the form-fields, annotations, and/or the layers of a previously uploaded document.  # noqa: E501
        """
        pass

    def test_get_info(self):
        """Test case for get_info

        Gets information about a previously uploaded document.  # noqa: E501
        """
        pass

    def test_get_page_thumbnail(self):
        """Test case for get_page_thumbnail

        Gets a thumbnail of each page within the provided page range from a previously uploaded document.  # noqa: E501
        """
        pass

    def test_get_pdf_import_supported_file_extensions(self):
        """Test case for get_pdf_import_supported_file_extensions

        Gets the supported file extensions by the LoadDocumentAsPDF action.  # noqa: E501
        """
        pass

    def test_insert_image(self):
        """Test case for insert_image

        Inserts an image on a new page of a previously uploaded document.  # noqa: E501
        """
        pass

    def test_insert_new_page(self):
        """Test case for insert_new_page

        Inserts one or more new blank pages to a specific position in a previously uploaded document.  # noqa: E501
        """
        pass

    def test_insert_page_number(self):
        """Test case for insert_page_number

        Inserts page number(s) on a document.  # noqa: E501
        """
        pass

    def test_insert_text(self):
        """Test case for insert_text

        Inserts text on a document.  # noqa: E501
        """
        pass

    def test_linearize(self):
        """Test case for linearize

        Linearizes a previously uploaded document.  # noqa: E501
        """
        pass

    def test_load_document_as_pdf(self):
        """Test case for load_document_as_pdf

        Imports the provided document as PDF.  Supported document formats can be retrieved by the GetPDFImportSupportedFileExtensions action.  # noqa: E501
        """
        pass

    def test_load_document_as_pdf_multipart(self):
        """Test case for load_document_as_pdf_multipart

        Imports the provided document as PDF using Multipart Upload.  Supported document formats can be retrieved by the GetPDFImportSupportedFileExtensions action.  # noqa: E501
        """
        pass

    def test_merge(self):
        """Test case for merge

        Merges several previously uploaded documents into a new PDF.  # noqa: E501
        """
        pass

    def test_merge_pages(self):
        """Test case for merge_pages

        Merges multiple pages, vertically, within a previously uploaded document into one single page.  # noqa: E501
        """
        pass

    def test_move_page(self):
        """Test case for move_page

        Moves a page range from a previously uploaded document.  # noqa: E501
        """
        pass

    def test_o_cr(self):
        """Test case for o_cr

        Performs optical character recognition on a page range of a previously uploaded document.  The recognized text is added as invisible text on each processed page.  No token is charged for blank pages.  # noqa: E501
        """
        pass

    def test_protect(self):
        """Test case for protect

        Protects a previously uploaded document.  # noqa: E501
        """
        pass

    def test_read_barcodes(self):
        """Test case for read_barcodes

        Reads barcodes from a previously uploaded document.  # noqa: E501
        """
        pass

    def test_reduce(self):
        """Test case for reduce

        Reduces the size of a previously uploaded document.  # noqa: E501
        """
        pass

    def test_remove_page_form_fields(self):
        """Test case for remove_page_form_fields

        Removes the form fields from a page range of a previously uploaded document.  # noqa: E501
        """
        pass

    def test_remove_text(self):
        """Test case for remove_text

        Removes text (all text or only invisible one) from a previously uploaded PDF.  # noqa: E501
        """
        pass

    def test_reorder_pages(self):
        """Test case for reorder_pages

        Reorders pages of a previously uploaded document.  # noqa: E501
        """
        pass

    def test_repair_document(self):
        """Test case for repair_document

        Repairs a previously uploaded PDF document.  # noqa: E501
        """
        pass

    def test_rotate_page_standard(self):
        """Test case for rotate_page_standard

        Rotates (standardly) a page range from a previously uploaded document.  # noqa: E501
        """
        pass

    def test_save_as_jpeg(self):
        """Test case for save_as_jpeg

        Saves a previously uploaded document as JPEG, and sends the file data in a JSON-serialized object.  # noqa: E501
        """
        pass

    def test_save_as_jpeg_file(self):
        """Test case for save_as_jpeg_file

        Saves a previously uploaded document as JPEG, and streams the file binary data to the response (this is the most efficient download method).  # noqa: E501
        """
        pass

    def test_save_as_png(self):
        """Test case for save_as_png

        Saves a previously uploaded document as PNG, and sends the file data in a JSON-serialized object.  # noqa: E501
        """
        pass

    def test_save_as_png_file(self):
        """Test case for save_as_png_file

        Saves a previously uploaded document as PNG, and streams the file binary data to the response (this is the most efficient download method).  # noqa: E501
        """
        pass

    def test_save_as_tiff(self):
        """Test case for save_as_tiff

        Saves a previously uploaded document as TIFF, and sends the file data in a JSON-serialized object.  # noqa: E501
        """
        pass

    def test_save_as_tiff_file(self):
        """Test case for save_as_tiff_file

        Saves a previously uploaded document as TIFF, and streams the file binary data to the response (this is the most efficient download method).  # noqa: E501
        """
        pass

    def test_save_as_tiff_multipage(self):
        """Test case for save_as_tiff_multipage

        Saves a previously uploaded document as multipage TIFF, and sends the file data in a JSON-serialized object.  # noqa: E501
        """
        pass

    def test_save_as_tiff_multipage_file(self):
        """Test case for save_as_tiff_multipage_file

        Saves a previously uploaded document as multipage TIFF, and streams the file binary data to the response (this is the most efficient download method).  # noqa: E501
        """
        pass

    def test_save_document(self):
        """Test case for save_document

        Saves a previously uploaded document as PDF, and sends the file data in a JSON-serialized object.  # noqa: E501
        """
        pass

    def test_save_document_to_file(self):
        """Test case for save_document_to_file

        Saves a previously uploaded document as PDF, and streams the file binary data to the response (this is the most efficient download method).  # noqa: E501
        """
        pass

    def test_scale_page(self):
        """Test case for scale_page

        Scales a page range from a previously uploaded document.  # noqa: E501
        """
        pass

    def test_set_info(self):
        """Test case for set_info

        Sets information to a previously uploaded document.  # noqa: E501
        """
        pass

    def test_set_initial_view(self):
        """Test case for set_initial_view

        Sets various document level initial view options to a previously uploaded document.  # noqa: E501
        """
        pass

    def test_set_page_box(self):
        """Test case for set_page_box

        Sets pagebox to a page range from previously uploaded document.  # noqa: E501
        """
        pass

    def test_set_password(self):
        """Test case for set_password

        Unprotects a previously uploaded document.  # noqa: E501
        """
        pass

    def test_split(self):
        """Test case for split

        Splits a previously uploaded document into new ones.  # noqa: E501
        """
        pass

    def test_swap_pages(self):
        """Test case for swap_pages

        Swaps two pages from a previously uploaded document.  # noqa: E501
        """
        pass

    def test_unprotect(self):
        """Test case for unprotect

        Unprotects a previously uploaded document.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
