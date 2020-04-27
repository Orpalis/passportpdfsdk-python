# openapi_client.PDFApi

All URIs are relative to *https://passportpdfapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotate**](PDFApi.md#annotate) | **POST** /api/pdf/Annotate | Annotates a previously uploaded document.
[**auto_deskew**](PDFApi.md#auto_deskew) | **POST** /api/pdf/AutoDeskew | Performs auto deskew on a page range of a previously uploaded document.
[**clear_page**](PDFApi.md#clear_page) | **POST** /api/pdf/ClearPage | Clears a page range from a previously uploaded document.
[**clone_page**](PDFApi.md#clone_page) | **POST** /api/pdf/ClonePage | Clones specific pages from a previously uploaded document to another previously uploaded document.
[**close_pdf**](PDFApi.md#close_pdf) | **POST** /api/pdf/ClosePDF | Closes a previously uploaded document.
[**convert_to_pdfa**](PDFApi.md#convert_to_pdfa) | **POST** /api/pdf/ConvertToPDFA | Converts a previously uploaded document to PDF/A.
[**delete_page**](PDFApi.md#delete_page) | **POST** /api/pdf/DeletePage | Deletes a page range from a previously uploaded document.
[**detect_page_orientation**](PDFApi.md#detect_page_orientation) | **POST** /api/pdf/DetectPageOrientation | Detects the orientation of the page(s) of a previously uploaded document and offers to automatically rotate them.
[**digi_sign**](PDFApi.md#digi_sign) | **POST** /api/pdf/DigiSign | Signs a previously uploaded document digitally.
[**draw_image**](PDFApi.md#draw_image) | **POST** /api/pdf/DrawImage | Draws an image on a page range of a previously uploaded document.
[**extract_page**](PDFApi.md#extract_page) | **POST** /api/pdf/ExtractPage | Extracts a page range from a previously uploaded document into one or several new documents.
[**extract_text**](PDFApi.md#extract_text) | **POST** /api/pdf/ExtractText | Extracts text from the document pages.
[**flatten**](PDFApi.md#flatten) | **POST** /api/pdf/Flatten | Flattens the form-fields, annotations, and/or the layers of a previously uploaded document.
[**get_info**](PDFApi.md#get_info) | **POST** /api/pdf/GetInfo | Gets information about a previously uploaded document.
[**get_page_thumbnail**](PDFApi.md#get_page_thumbnail) | **POST** /api/pdf/GetPageThumbnail | Gets a thumbnail of each page within the provided page range from a previously uploaded document.
[**get_pdf_import_supported_file_extensions**](PDFApi.md#get_pdf_import_supported_file_extensions) | **GET** /api/pdf/GetPDFImportSupportedFileExtensions | Gets the supported file extensions by the LoadDocumentAsPDF action.
[**insert_image**](PDFApi.md#insert_image) | **POST** /api/pdf/InsertImage | Inserts an image on a new page of a previously uploaded document.
[**insert_new_page**](PDFApi.md#insert_new_page) | **POST** /api/pdf/InsertNewPage | Inserts one or more new blank pages to a specific position in a previously uploaded document.
[**insert_page_number**](PDFApi.md#insert_page_number) | **POST** /api/pdf/InsertPageNumber | Inserts page number(s) on a document.
[**insert_text**](PDFApi.md#insert_text) | **POST** /api/pdf/InsertText | Inserts text on a document.
[**linearize**](PDFApi.md#linearize) | **POST** /api/pdf/Linearize | Linearizes a previously uploaded document.
[**load_document_as_pdf**](PDFApi.md#load_document_as_pdf) | **POST** /api/pdf/LoadDocument | Imports the provided document as PDF.  Supported document formats can be retrieved by the GetPDFImportSupportedFileExtensions action.
[**load_document_as_pdf_multipart**](PDFApi.md#load_document_as_pdf_multipart) | **POST** /api/pdf/LoadDocumentAsPDFMultipart | Imports the provided document as PDF using Multipart Upload.  Supported document formats can be retrieved by the GetPDFImportSupportedFileExtensions action.
[**merge**](PDFApi.md#merge) | **POST** /api/pdf/Merge | Merges several previously uploaded documents into a new PDF.
[**merge_pages**](PDFApi.md#merge_pages) | **POST** /api/pdf/MergePages | Merges multiple pages, vertically, within a previously uploaded document into one single page.
[**move_page**](PDFApi.md#move_page) | **POST** /api/pdf/MovePage | Moves a page range from a previously uploaded document.
[**o_cr**](PDFApi.md#o_cr) | **POST** /api/pdf/OCR | Performs optical character recognition on a page range of a previously uploaded document.  The recognized text is added as invisible text on each processed page.  No token is charged for blank pages.
[**protect**](PDFApi.md#protect) | **POST** /api/pdf/Protect | Protects a previously uploaded document.
[**read_barcodes**](PDFApi.md#read_barcodes) | **POST** /api/pdf/ReadBarcodes | Reads barcodes from a previously uploaded document.
[**reduce**](PDFApi.md#reduce) | **POST** /api/pdf/Reduce | Reduces the size of a previously uploaded document.
[**remove_page_form_fields**](PDFApi.md#remove_page_form_fields) | **POST** /api/pdf/RemovePageFormFields | Removes the form fields from a page range of a previously uploaded document.
[**remove_text**](PDFApi.md#remove_text) | **POST** /api/pdf/RemoveText | Removes text (all text or only invisible one) from a previously uploaded PDF.
[**reorder_pages**](PDFApi.md#reorder_pages) | **POST** /api/pdf/ReorderPages | Reorders pages of a previously uploaded document.
[**repair_document**](PDFApi.md#repair_document) | **POST** /api/pdf/RepairDocument | Repairs a previously uploaded PDF document.
[**rotate_page_standard**](PDFApi.md#rotate_page_standard) | **POST** /api/pdf/RotatePageStandard | Rotates (standardly) a page range from a previously uploaded document.
[**save_as_jpeg**](PDFApi.md#save_as_jpeg) | **POST** /api/pdf/SaveAsJPEG | Saves a previously uploaded document as JPEG, and sends the file data in a JSON-serialized object.
[**save_as_jpeg_file**](PDFApi.md#save_as_jpeg_file) | **POST** /api/pdf/SaveAsJPEGFile | Saves a previously uploaded document as JPEG, and streams the file binary data to the response (this is the most efficient download method).
[**save_as_png**](PDFApi.md#save_as_png) | **POST** /api/pdf/SaveAsPNG | Saves a previously uploaded document as PNG, and sends the file data in a JSON-serialized object.
[**save_as_png_file**](PDFApi.md#save_as_png_file) | **POST** /api/pdf/SaveAsPNGFile | Saves a previously uploaded document as PNG, and streams the file binary data to the response (this is the most efficient download method).
[**save_as_tiff**](PDFApi.md#save_as_tiff) | **POST** /api/pdf/SaveAsTIFF | Saves a previously uploaded document as TIFF, and sends the file data in a JSON-serialized object.
[**save_as_tiff_file**](PDFApi.md#save_as_tiff_file) | **POST** /api/pdf/SaveAsTIFFFile | Saves a previously uploaded document as TIFF, and streams the file binary data to the response (this is the most efficient download method).
[**save_as_tiff_multipage**](PDFApi.md#save_as_tiff_multipage) | **POST** /api/pdf/SaveAsTIFFMultipage | Saves a previously uploaded document as multipage TIFF, and sends the file data in a JSON-serialized object.
[**save_as_tiff_multipage_file**](PDFApi.md#save_as_tiff_multipage_file) | **POST** /api/pdf/SaveAsTIFFMultipageFile | Saves a previously uploaded document as multipage TIFF, and streams the file binary data to the response (this is the most efficient download method).
[**save_document**](PDFApi.md#save_document) | **POST** /api/pdf/SaveDocument | Saves a previously uploaded document as PDF, and sends the file data in a JSON-serialized object.
[**save_document_to_file**](PDFApi.md#save_document_to_file) | **POST** /api/pdf/SaveDocumentToFile | Saves a previously uploaded document as PDF, and streams the file binary data to the response (this is the most efficient download method).
[**scale_page**](PDFApi.md#scale_page) | **POST** /api/pdf/ScalePage | Scales a page range from a previously uploaded document.
[**set_info**](PDFApi.md#set_info) | **POST** /api/pdf/SetInfo | Sets information to a previously uploaded document.
[**set_initial_view**](PDFApi.md#set_initial_view) | **POST** /api/pdf/SetInitialView | Sets various document level initial view options to a previously uploaded document.
[**set_page_box**](PDFApi.md#set_page_box) | **POST** /api/pdf/SetPageBox | Sets pagebox to a page range from previously uploaded document.
[**set_password**](PDFApi.md#set_password) | **POST** /api/pdf/SetPassword | Unprotects a previously uploaded document.
[**split**](PDFApi.md#split) | **POST** /api/pdf/Split | Splits a previously uploaded document into new ones.
[**swap_pages**](PDFApi.md#swap_pages) | **POST** /api/pdf/SwapPages | Swaps two pages from a previously uploaded document.
[**unprotect**](PDFApi.md#unprotect) | **POST** /api/pdf/Unprotect | Unprotects a previously uploaded document.


# **annotate**
> PdfAnnotateResponse annotate(pdf_annotate_parameters)

Annotates a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_annotate_parameters = openapi_client.PdfAnnotateParameters() # PdfAnnotateParameters | A PdfAnnotateParameters object specifying the parameters of the action.

    try:
        # Annotates a previously uploaded document.
        api_response = api_instance.annotate(pdf_annotate_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->annotate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_annotate_parameters** | [**PdfAnnotateParameters**](PdfAnnotateParameters.md)| A PdfAnnotateParameters object specifying the parameters of the action. | 

### Return type

[**PdfAnnotateResponse**](PdfAnnotateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auto_deskew**
> PdfAutoDeskewResponse auto_deskew(pdf_auto_deskew_parameters)

Performs auto deskew on a page range of a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_auto_deskew_parameters = openapi_client.PdfAutoDeskewParameters() # PdfAutoDeskewParameters | A PdfAutoDeskewParameters object specifying the parameters of the action.

    try:
        # Performs auto deskew on a page range of a previously uploaded document.
        api_response = api_instance.auto_deskew(pdf_auto_deskew_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->auto_deskew: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_auto_deskew_parameters** | [**PdfAutoDeskewParameters**](PdfAutoDeskewParameters.md)| A PdfAutoDeskewParameters object specifying the parameters of the action. | 

### Return type

[**PdfAutoDeskewResponse**](PdfAutoDeskewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_page**
> PdfClearPageResponse clear_page(pdf_clear_page_parameters)

Clears a page range from a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_clear_page_parameters = openapi_client.PdfClearPageParameters() # PdfClearPageParameters | A PdfClearPageParameters object specifying the parameters of the action.

    try:
        # Clears a page range from a previously uploaded document.
        api_response = api_instance.clear_page(pdf_clear_page_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->clear_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_clear_page_parameters** | [**PdfClearPageParameters**](PdfClearPageParameters.md)| A PdfClearPageParameters object specifying the parameters of the action. | 

### Return type

[**PdfClearPageResponse**](PdfClearPageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_page**
> PdfClonePageResponse clone_page(pdf_clone_page_parameters)

Clones specific pages from a previously uploaded document to another previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_clone_page_parameters = openapi_client.PdfClonePageParameters() # PdfClonePageParameters | A PdfClonePageParameters object specifying the parameters of the action.

    try:
        # Clones specific pages from a previously uploaded document to another previously uploaded document.
        api_response = api_instance.clone_page(pdf_clone_page_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->clone_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_clone_page_parameters** | [**PdfClonePageParameters**](PdfClonePageParameters.md)| A PdfClonePageParameters object specifying the parameters of the action. | 

### Return type

[**PdfClonePageResponse**](PdfClonePageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_pdf**
> PdfCloseDocumentResponse close_pdf(pdf_close_document_parameters)

Closes a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_close_document_parameters = openapi_client.PdfCloseDocumentParameters() # PdfCloseDocumentParameters | A PdfCloseDocumentParameters object specifying the parameters of the action.

    try:
        # Closes a previously uploaded document.
        api_response = api_instance.close_pdf(pdf_close_document_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->close_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_close_document_parameters** | [**PdfCloseDocumentParameters**](PdfCloseDocumentParameters.md)| A PdfCloseDocumentParameters object specifying the parameters of the action. | 

### Return type

[**PdfCloseDocumentResponse**](PdfCloseDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_to_pdfa**
> PdfConvertToPDFAResponse convert_to_pdfa(pdf_convert_to_pdfa_parameters)

Converts a previously uploaded document to PDF/A.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_convert_to_pdfa_parameters = openapi_client.PdfConvertToPDFAParameters() # PdfConvertToPDFAParameters | A PdfConvertToPDFAParameters object specifying the parameters of the action.

    try:
        # Converts a previously uploaded document to PDF/A.
        api_response = api_instance.convert_to_pdfa(pdf_convert_to_pdfa_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->convert_to_pdfa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_convert_to_pdfa_parameters** | [**PdfConvertToPDFAParameters**](PdfConvertToPDFAParameters.md)| A PdfConvertToPDFAParameters object specifying the parameters of the action. | 

### Return type

[**PdfConvertToPDFAResponse**](PdfConvertToPDFAResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page**
> PdfDeletePageResponse delete_page(pdf_delete_page_parameters)

Deletes a page range from a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_delete_page_parameters = openapi_client.PdfDeletePageParameters() # PdfDeletePageParameters | A PdfDeletePageParameters object specifying the parameters of the action.

    try:
        # Deletes a page range from a previously uploaded document.
        api_response = api_instance.delete_page(pdf_delete_page_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->delete_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_delete_page_parameters** | [**PdfDeletePageParameters**](PdfDeletePageParameters.md)| A PdfDeletePageParameters object specifying the parameters of the action. | 

### Return type

[**PdfDeletePageResponse**](PdfDeletePageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_page_orientation**
> PdfDetectPageOrientationResponse detect_page_orientation(pdf_detect_page_orientation_parameters)

Detects the orientation of the page(s) of a previously uploaded document and offers to automatically rotate them.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_detect_page_orientation_parameters = openapi_client.PdfDetectPageOrientationParameters() # PdfDetectPageOrientationParameters | A PdfDetectPageOrientationParameters object specifying the parameters of the action.

    try:
        # Detects the orientation of the page(s) of a previously uploaded document and offers to automatically rotate them.
        api_response = api_instance.detect_page_orientation(pdf_detect_page_orientation_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->detect_page_orientation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_detect_page_orientation_parameters** | [**PdfDetectPageOrientationParameters**](PdfDetectPageOrientationParameters.md)| A PdfDetectPageOrientationParameters object specifying the parameters of the action. | 

### Return type

[**PdfDetectPageOrientationResponse**](PdfDetectPageOrientationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **digi_sign**
> PdfDigiSignResponse digi_sign(pdf_digi_sign_parameters)

Signs a previously uploaded document digitally.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_digi_sign_parameters = openapi_client.PdfDigiSignParameters() # PdfDigiSignParameters | A PdfDigiSignParameters object specifying the parameters of the action.

    try:
        # Signs a previously uploaded document digitally.
        api_response = api_instance.digi_sign(pdf_digi_sign_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->digi_sign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_digi_sign_parameters** | [**PdfDigiSignParameters**](PdfDigiSignParameters.md)| A PdfDigiSignParameters object specifying the parameters of the action. | 

### Return type

[**PdfDigiSignResponse**](PdfDigiSignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **draw_image**
> PdfDrawImageResponse draw_image(pdf_draw_image_parameters)

Draws an image on a page range of a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_draw_image_parameters = openapi_client.PdfDrawImageParameters() # PdfDrawImageParameters | A PdfDrawImageParameters object specifying the parameters of the action.

    try:
        # Draws an image on a page range of a previously uploaded document.
        api_response = api_instance.draw_image(pdf_draw_image_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->draw_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_draw_image_parameters** | [**PdfDrawImageParameters**](PdfDrawImageParameters.md)| A PdfDrawImageParameters object specifying the parameters of the action. | 

### Return type

[**PdfDrawImageResponse**](PdfDrawImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_page**
> PdfExtractPageResponse extract_page(pdf_extract_page_parameters)

Extracts a page range from a previously uploaded document into one or several new documents.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_extract_page_parameters = openapi_client.PdfExtractPageParameters() # PdfExtractPageParameters | A PdfExtractPageParameters object specifying the parameters of the action.

    try:
        # Extracts a page range from a previously uploaded document into one or several new documents.
        api_response = api_instance.extract_page(pdf_extract_page_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->extract_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_extract_page_parameters** | [**PdfExtractPageParameters**](PdfExtractPageParameters.md)| A PdfExtractPageParameters object specifying the parameters of the action. | 

### Return type

[**PdfExtractPageResponse**](PdfExtractPageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_text**
> PdfExtractTextResponse extract_text(pdf_extract_text_parameters)

Extracts text from the document pages.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_extract_text_parameters = openapi_client.PdfExtractTextParameters() # PdfExtractTextParameters | A PdfExtractTextParameters object specifying the parameters of the action.

    try:
        # Extracts text from the document pages.
        api_response = api_instance.extract_text(pdf_extract_text_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->extract_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_extract_text_parameters** | [**PdfExtractTextParameters**](PdfExtractTextParameters.md)| A PdfExtractTextParameters object specifying the parameters of the action. | 

### Return type

[**PdfExtractTextResponse**](PdfExtractTextResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flatten**
> PdfFlattenResponse flatten(pdf_flatten_parameters)

Flattens the form-fields, annotations, and/or the layers of a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_flatten_parameters = openapi_client.PdfFlattenParameters() # PdfFlattenParameters | A PdfFlatten object specifying the parameters of the action.

    try:
        # Flattens the form-fields, annotations, and/or the layers of a previously uploaded document.
        api_response = api_instance.flatten(pdf_flatten_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->flatten: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_flatten_parameters** | [**PdfFlattenParameters**](PdfFlattenParameters.md)| A PdfFlatten object specifying the parameters of the action. | 

### Return type

[**PdfFlattenResponse**](PdfFlattenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_info**
> PdfGetInfoResponse get_info(pdf_get_info_parameters)

Gets information about a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_get_info_parameters = openapi_client.PdfGetInfoParameters() # PdfGetInfoParameters | A PdfGetInfoParameters object specifying the parameters of the action.

    try:
        # Gets information about a previously uploaded document.
        api_response = api_instance.get_info(pdf_get_info_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->get_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_get_info_parameters** | [**PdfGetInfoParameters**](PdfGetInfoParameters.md)| A PdfGetInfoParameters object specifying the parameters of the action. | 

### Return type

[**PdfGetInfoResponse**](PdfGetInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_thumbnail**
> PdfGetPageThumbnailResponse get_page_thumbnail(pdf_get_page_thumbnail_parameters)

Gets a thumbnail of each page within the provided page range from a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_get_page_thumbnail_parameters = openapi_client.PdfGetPageThumbnailParameters() # PdfGetPageThumbnailParameters | A PdfGetPageThumbnailParameters object specifying the parameters of the action.

    try:
        # Gets a thumbnail of each page within the provided page range from a previously uploaded document.
        api_response = api_instance.get_page_thumbnail(pdf_get_page_thumbnail_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->get_page_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_get_page_thumbnail_parameters** | [**PdfGetPageThumbnailParameters**](PdfGetPageThumbnailParameters.md)| A PdfGetPageThumbnailParameters object specifying the parameters of the action. | 

### Return type

[**PdfGetPageThumbnailResponse**](PdfGetPageThumbnailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_import_supported_file_extensions**
> StringArrayResponse get_pdf_import_supported_file_extensions()

Gets the supported file extensions by the LoadDocumentAsPDF action.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    
    try:
        # Gets the supported file extensions by the LoadDocumentAsPDF action.
        api_response = api_instance.get_pdf_import_supported_file_extensions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->get_pdf_import_supported_file_extensions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StringArrayResponse**](StringArrayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_image**
> PdfInsertImageResponse insert_image(pdf_insert_image_parameters)

Inserts an image on a new page of a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_insert_image_parameters = openapi_client.PdfInsertImageParameters() # PdfInsertImageParameters | A PdfInsertImageParameters object specifying the parameters of the action.

    try:
        # Inserts an image on a new page of a previously uploaded document.
        api_response = api_instance.insert_image(pdf_insert_image_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->insert_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_insert_image_parameters** | [**PdfInsertImageParameters**](PdfInsertImageParameters.md)| A PdfInsertImageParameters object specifying the parameters of the action. | 

### Return type

[**PdfInsertImageResponse**](PdfInsertImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_new_page**
> PdfInsertNewPageResponse insert_new_page(pdf_insert_new_page_parameters)

Inserts one or more new blank pages to a specific position in a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_insert_new_page_parameters = openapi_client.PdfInsertNewPageParameters() # PdfInsertNewPageParameters | A PdfInsertNewPageParameters object specifying the parameters of the action.

    try:
        # Inserts one or more new blank pages to a specific position in a previously uploaded document.
        api_response = api_instance.insert_new_page(pdf_insert_new_page_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->insert_new_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_insert_new_page_parameters** | [**PdfInsertNewPageParameters**](PdfInsertNewPageParameters.md)| A PdfInsertNewPageParameters object specifying the parameters of the action. | 

### Return type

[**PdfInsertNewPageResponse**](PdfInsertNewPageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_page_number**
> PdfInsertPageNumberResponse insert_page_number(pdf_insert_page_number_parameters)

Inserts page number(s) on a document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_insert_page_number_parameters = openapi_client.PdfInsertPageNumberParameters() # PdfInsertPageNumberParameters | A PdfInsertPageNumberParameters object specifying the parameters of the action.

    try:
        # Inserts page number(s) on a document.
        api_response = api_instance.insert_page_number(pdf_insert_page_number_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->insert_page_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_insert_page_number_parameters** | [**PdfInsertPageNumberParameters**](PdfInsertPageNumberParameters.md)| A PdfInsertPageNumberParameters object specifying the parameters of the action. | 

### Return type

[**PdfInsertPageNumberResponse**](PdfInsertPageNumberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_text**
> PdfInsertTextResponse insert_text(pdf_insert_text_parameters)

Inserts text on a document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_insert_text_parameters = openapi_client.PdfInsertTextParameters() # PdfInsertTextParameters | A PdfInsertTextParameters object specifying the parameters of the action.

    try:
        # Inserts text on a document.
        api_response = api_instance.insert_text(pdf_insert_text_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->insert_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_insert_text_parameters** | [**PdfInsertTextParameters**](PdfInsertTextParameters.md)| A PdfInsertTextParameters object specifying the parameters of the action. | 

### Return type

[**PdfInsertTextResponse**](PdfInsertTextResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **linearize**
> PdfLinearizeResponse linearize(pdf_linearize_parameters)

Linearizes a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_linearize_parameters = openapi_client.PdfLinearizeParameters() # PdfLinearizeParameters | A PdfLinearizeParameters object specifying the parameters of the action.

    try:
        # Linearizes a previously uploaded document.
        api_response = api_instance.linearize(pdf_linearize_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->linearize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_linearize_parameters** | [**PdfLinearizeParameters**](PdfLinearizeParameters.md)| A PdfLinearizeParameters object specifying the parameters of the action. | 

### Return type

[**PdfLinearizeResponse**](PdfLinearizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_document_as_pdf**
> PdfLoadDocumentResponse load_document_as_pdf(pdf_load_document_from_byte_array_parameters)

Imports the provided document as PDF.  Supported document formats can be retrieved by the GetPDFImportSupportedFileExtensions action.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_load_document_from_byte_array_parameters = openapi_client.PdfLoadDocumentFromByteArrayParameters() # PdfLoadDocumentFromByteArrayParameters | A PdfLoadDocumentFromByteArrayParameters object specifying the parameters of the action.

    try:
        # Imports the provided document as PDF.  Supported document formats can be retrieved by the GetPDFImportSupportedFileExtensions action.
        api_response = api_instance.load_document_as_pdf(pdf_load_document_from_byte_array_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->load_document_as_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_load_document_from_byte_array_parameters** | [**PdfLoadDocumentFromByteArrayParameters**](PdfLoadDocumentFromByteArrayParameters.md)| A PdfLoadDocumentFromByteArrayParameters object specifying the parameters of the action. | 

### Return type

[**PdfLoadDocumentResponse**](PdfLoadDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_document_as_pdf_multipart**
> PdfLoadDocumentResponse load_document_as_pdf_multipart(file_data, load_document_parameters=load_document_parameters)

Imports the provided document as PDF using Multipart Upload.  Supported document formats can be retrieved by the GetPDFImportSupportedFileExtensions action.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    file_data = '/path/to/file' # file | The data of the document.
load_document_parameters = openapi_client.PdfLoadDocumentParameters() # PdfLoadDocumentParameters |  (optional)

    try:
        # Imports the provided document as PDF using Multipart Upload.  Supported document formats can be retrieved by the GetPDFImportSupportedFileExtensions action.
        api_response = api_instance.load_document_as_pdf_multipart(file_data, load_document_parameters=load_document_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->load_document_as_pdf_multipart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_data** | **file**| The data of the document. | 
 **load_document_parameters** | [**PdfLoadDocumentParameters**](PdfLoadDocumentParameters.md)|  | [optional] 

### Return type

[**PdfLoadDocumentResponse**](PdfLoadDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge**
> PdfMergeResponse merge(pdf_merge_parameters)

Merges several previously uploaded documents into a new PDF.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_merge_parameters = openapi_client.PdfMergeParameters() # PdfMergeParameters | A PdfMergeParameters object specifying the parameters of the action.

    try:
        # Merges several previously uploaded documents into a new PDF.
        api_response = api_instance.merge(pdf_merge_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_merge_parameters** | [**PdfMergeParameters**](PdfMergeParameters.md)| A PdfMergeParameters object specifying the parameters of the action. | 

### Return type

[**PdfMergeResponse**](PdfMergeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_pages**
> PdfMergePagesResponse merge_pages(pdf_merge_pages_parameters)

Merges multiple pages, vertically, within a previously uploaded document into one single page.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_merge_pages_parameters = openapi_client.PdfMergePagesParameters() # PdfMergePagesParameters | A PdfMergePages object specifying the parameters of the action.

    try:
        # Merges multiple pages, vertically, within a previously uploaded document into one single page.
        api_response = api_instance.merge_pages(pdf_merge_pages_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->merge_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_merge_pages_parameters** | [**PdfMergePagesParameters**](PdfMergePagesParameters.md)| A PdfMergePages object specifying the parameters of the action. | 

### Return type

[**PdfMergePagesResponse**](PdfMergePagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_page**
> PdfMovePageResponse move_page(pdf_move_page_parameters)

Moves a page range from a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_move_page_parameters = openapi_client.PdfMovePageParameters() # PdfMovePageParameters | A PdfMovePageParameters object specifying the parameters of the action.

    try:
        # Moves a page range from a previously uploaded document.
        api_response = api_instance.move_page(pdf_move_page_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->move_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_move_page_parameters** | [**PdfMovePageParameters**](PdfMovePageParameters.md)| A PdfMovePageParameters object specifying the parameters of the action. | 

### Return type

[**PdfMovePageResponse**](PdfMovePageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_cr**
> PdfOCRResponse o_cr(pdf_ocr_parameters)

Performs optical character recognition on a page range of a previously uploaded document.  The recognized text is added as invisible text on each processed page.  No token is charged for blank pages.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_ocr_parameters = openapi_client.PdfOCRParameters() # PdfOCRParameters | A PdfOCRParameters object specifying the parameters of the action.

    try:
        # Performs optical character recognition on a page range of a previously uploaded document.  The recognized text is added as invisible text on each processed page.  No token is charged for blank pages.
        api_response = api_instance.o_cr(pdf_ocr_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->o_cr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_ocr_parameters** | [**PdfOCRParameters**](PdfOCRParameters.md)| A PdfOCRParameters object specifying the parameters of the action. | 

### Return type

[**PdfOCRResponse**](PdfOCRResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect**
> PdfProtectResponse protect(pdf_protect_parameters)

Protects a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_protect_parameters = openapi_client.PdfProtectParameters() # PdfProtectParameters | A PdfProtectParameters object specifying the parameters of the action.

    try:
        # Protects a previously uploaded document.
        api_response = api_instance.protect(pdf_protect_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->protect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_protect_parameters** | [**PdfProtectParameters**](PdfProtectParameters.md)| A PdfProtectParameters object specifying the parameters of the action. | 

### Return type

[**PdfProtectResponse**](PdfProtectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_barcodes**
> ReadBarcodesResponse read_barcodes(pdf_read_barcodes_parameters)

Reads barcodes from a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_read_barcodes_parameters = openapi_client.PdfReadBarcodesParameters() # PdfReadBarcodesParameters | A PdfReadBarcodesParameters object specifying the parameters of the action.

    try:
        # Reads barcodes from a previously uploaded document.
        api_response = api_instance.read_barcodes(pdf_read_barcodes_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->read_barcodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_read_barcodes_parameters** | [**PdfReadBarcodesParameters**](PdfReadBarcodesParameters.md)| A PdfReadBarcodesParameters object specifying the parameters of the action. | 

### Return type

[**ReadBarcodesResponse**](ReadBarcodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reduce**
> PdfReduceResponse reduce(pdf_reduce_parameters)

Reduces the size of a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_reduce_parameters = openapi_client.PdfReduceParameters() # PdfReduceParameters | A PdfReduceParameters object specifying the parameters of the action.

    try:
        # Reduces the size of a previously uploaded document.
        api_response = api_instance.reduce(pdf_reduce_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->reduce: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_reduce_parameters** | [**PdfReduceParameters**](PdfReduceParameters.md)| A PdfReduceParameters object specifying the parameters of the action. | 

### Return type

[**PdfReduceResponse**](PdfReduceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_page_form_fields**
> PdfRemovePageFormFieldsResponse remove_page_form_fields(pdf_remove_page_form_fields_parameters)

Removes the form fields from a page range of a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_remove_page_form_fields_parameters = openapi_client.PdfRemovePageFormFieldsParameters() # PdfRemovePageFormFieldsParameters | A PdfRemovePageFormFieldsParameters object specifying the parameters of the action.

    try:
        # Removes the form fields from a page range of a previously uploaded document.
        api_response = api_instance.remove_page_form_fields(pdf_remove_page_form_fields_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->remove_page_form_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_remove_page_form_fields_parameters** | [**PdfRemovePageFormFieldsParameters**](PdfRemovePageFormFieldsParameters.md)| A PdfRemovePageFormFieldsParameters object specifying the parameters of the action. | 

### Return type

[**PdfRemovePageFormFieldsResponse**](PdfRemovePageFormFieldsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_text**
> PdfRemoveTextResponse remove_text(pdf_remove_text_parameters)

Removes text (all text or only invisible one) from a previously uploaded PDF.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_remove_text_parameters = openapi_client.PdfRemoveTextParameters() # PdfRemoveTextParameters | A PdfRemoveTextParameters object specifying the parameters of the action.

    try:
        # Removes text (all text or only invisible one) from a previously uploaded PDF.
        api_response = api_instance.remove_text(pdf_remove_text_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->remove_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_remove_text_parameters** | [**PdfRemoveTextParameters**](PdfRemoveTextParameters.md)| A PdfRemoveTextParameters object specifying the parameters of the action. | 

### Return type

[**PdfRemoveTextResponse**](PdfRemoveTextResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_pages**
> PdfReorderPagesResponse reorder_pages(pdf_reorder_pages_parameters)

Reorders pages of a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_reorder_pages_parameters = openapi_client.PdfReorderPagesParameters() # PdfReorderPagesParameters | A PdfReorderPagesParameters object specifying the parameters of the action.

    try:
        # Reorders pages of a previously uploaded document.
        api_response = api_instance.reorder_pages(pdf_reorder_pages_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->reorder_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_reorder_pages_parameters** | [**PdfReorderPagesParameters**](PdfReorderPagesParameters.md)| A PdfReorderPagesParameters object specifying the parameters of the action. | 

### Return type

[**PdfReorderPagesResponse**](PdfReorderPagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repair_document**
> PdfRepairDocumentResponse repair_document(pdf_repair_document_parameters)

Repairs a previously uploaded PDF document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_repair_document_parameters = openapi_client.PdfRepairDocumentParameters() # PdfRepairDocumentParameters | A PdfRepairDocumentParameters object specifying the parameters of the action.

    try:
        # Repairs a previously uploaded PDF document.
        api_response = api_instance.repair_document(pdf_repair_document_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->repair_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_repair_document_parameters** | [**PdfRepairDocumentParameters**](PdfRepairDocumentParameters.md)| A PdfRepairDocumentParameters object specifying the parameters of the action. | 

### Return type

[**PdfRepairDocumentResponse**](PdfRepairDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_page_standard**
> PdfRotatePageStandardResponse rotate_page_standard(pdf_rotate_page_standard_parameters)

Rotates (standardly) a page range from a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_rotate_page_standard_parameters = openapi_client.PdfRotatePageStandardParameters() # PdfRotatePageStandardParameters | A PdfRotatePageStandardParameters object specifying the parameters of the action.

    try:
        # Rotates (standardly) a page range from a previously uploaded document.
        api_response = api_instance.rotate_page_standard(pdf_rotate_page_standard_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->rotate_page_standard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_rotate_page_standard_parameters** | [**PdfRotatePageStandardParameters**](PdfRotatePageStandardParameters.md)| A PdfRotatePageStandardParameters object specifying the parameters of the action. | 

### Return type

[**PdfRotatePageStandardResponse**](PdfRotatePageStandardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_jpeg**
> PdfSaveAsJPEGResponse save_as_jpeg(pdf_save_as_jpeg_parameters)

Saves a previously uploaded document as JPEG, and sends the file data in a JSON-serialized object.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_save_as_jpeg_parameters = openapi_client.PdfSaveAsJPEGParameters() # PdfSaveAsJPEGParameters | A PdfSaveAsJPEGParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded document as JPEG, and sends the file data in a JSON-serialized object.
        api_response = api_instance.save_as_jpeg(pdf_save_as_jpeg_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->save_as_jpeg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_save_as_jpeg_parameters** | [**PdfSaveAsJPEGParameters**](PdfSaveAsJPEGParameters.md)| A PdfSaveAsJPEGParameters object specifying the parameters of the action. | 

### Return type

[**PdfSaveAsJPEGResponse**](PdfSaveAsJPEGResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_jpeg_file**
> file save_as_jpeg_file(pdf_save_as_jpeg_parameters)

Saves a previously uploaded document as JPEG, and streams the file binary data to the response (this is the most efficient download method).

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_save_as_jpeg_parameters = openapi_client.PdfSaveAsJPEGParameters() # PdfSaveAsJPEGParameters | A PdfSaveAsJPEGParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded document as JPEG, and streams the file binary data to the response (this is the most efficient download method).
        api_response = api_instance.save_as_jpeg_file(pdf_save_as_jpeg_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->save_as_jpeg_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_save_as_jpeg_parameters** | [**PdfSaveAsJPEGParameters**](PdfSaveAsJPEGParameters.md)| A PdfSaveAsJPEGParameters object specifying the parameters of the action. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_png**
> PdfSaveAsPNGResponse save_as_png(pdf_save_as_png_parameters)

Saves a previously uploaded document as PNG, and sends the file data in a JSON-serialized object.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_save_as_png_parameters = openapi_client.PdfSaveAsPNGParameters() # PdfSaveAsPNGParameters | A PdfSaveAsPNGParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded document as PNG, and sends the file data in a JSON-serialized object.
        api_response = api_instance.save_as_png(pdf_save_as_png_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->save_as_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_save_as_png_parameters** | [**PdfSaveAsPNGParameters**](PdfSaveAsPNGParameters.md)| A PdfSaveAsPNGParameters object specifying the parameters of the action. | 

### Return type

[**PdfSaveAsPNGResponse**](PdfSaveAsPNGResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_png_file**
> file save_as_png_file(pdf_save_as_png_parameters)

Saves a previously uploaded document as PNG, and streams the file binary data to the response (this is the most efficient download method).

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_save_as_png_parameters = openapi_client.PdfSaveAsPNGParameters() # PdfSaveAsPNGParameters | A PdfSaveAsPNGParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded document as PNG, and streams the file binary data to the response (this is the most efficient download method).
        api_response = api_instance.save_as_png_file(pdf_save_as_png_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->save_as_png_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_save_as_png_parameters** | [**PdfSaveAsPNGParameters**](PdfSaveAsPNGParameters.md)| A PdfSaveAsPNGParameters object specifying the parameters of the action. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_tiff**
> PdfSaveAsTIFFResponse save_as_tiff(pdf_save_as_tiff_parameters)

Saves a previously uploaded document as TIFF, and sends the file data in a JSON-serialized object.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_save_as_tiff_parameters = openapi_client.PdfSaveAsTIFFParameters() # PdfSaveAsTIFFParameters | A PdfSaveAsTIFFParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded document as TIFF, and sends the file data in a JSON-serialized object.
        api_response = api_instance.save_as_tiff(pdf_save_as_tiff_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->save_as_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_save_as_tiff_parameters** | [**PdfSaveAsTIFFParameters**](PdfSaveAsTIFFParameters.md)| A PdfSaveAsTIFFParameters object specifying the parameters of the action. | 

### Return type

[**PdfSaveAsTIFFResponse**](PdfSaveAsTIFFResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_tiff_file**
> file save_as_tiff_file(pdf_save_as_tiff_parameters)

Saves a previously uploaded document as TIFF, and streams the file binary data to the response (this is the most efficient download method).

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_save_as_tiff_parameters = openapi_client.PdfSaveAsTIFFParameters() # PdfSaveAsTIFFParameters | A PdfSaveAsTIFFParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded document as TIFF, and streams the file binary data to the response (this is the most efficient download method).
        api_response = api_instance.save_as_tiff_file(pdf_save_as_tiff_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->save_as_tiff_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_save_as_tiff_parameters** | [**PdfSaveAsTIFFParameters**](PdfSaveAsTIFFParameters.md)| A PdfSaveAsTIFFParameters object specifying the parameters of the action. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_tiff_multipage**
> PdfSaveAsTIFFMultipageResponse save_as_tiff_multipage(pdf_save_as_tiff_multipage_parameters)

Saves a previously uploaded document as multipage TIFF, and sends the file data in a JSON-serialized object.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_save_as_tiff_multipage_parameters = openapi_client.PdfSaveAsTIFFMultipageParameters() # PdfSaveAsTIFFMultipageParameters | A PdfSaveAsTIFFMultipageParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded document as multipage TIFF, and sends the file data in a JSON-serialized object.
        api_response = api_instance.save_as_tiff_multipage(pdf_save_as_tiff_multipage_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->save_as_tiff_multipage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_save_as_tiff_multipage_parameters** | [**PdfSaveAsTIFFMultipageParameters**](PdfSaveAsTIFFMultipageParameters.md)| A PdfSaveAsTIFFMultipageParameters object specifying the parameters of the action. | 

### Return type

[**PdfSaveAsTIFFMultipageResponse**](PdfSaveAsTIFFMultipageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_tiff_multipage_file**
> file save_as_tiff_multipage_file(pdf_save_as_tiff_multipage_parameters)

Saves a previously uploaded document as multipage TIFF, and streams the file binary data to the response (this is the most efficient download method).

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_save_as_tiff_multipage_parameters = openapi_client.PdfSaveAsTIFFMultipageParameters() # PdfSaveAsTIFFMultipageParameters | A PdfSaveAsTIFFMultipageParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded document as multipage TIFF, and streams the file binary data to the response (this is the most efficient download method).
        api_response = api_instance.save_as_tiff_multipage_file(pdf_save_as_tiff_multipage_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->save_as_tiff_multipage_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_save_as_tiff_multipage_parameters** | [**PdfSaveAsTIFFMultipageParameters**](PdfSaveAsTIFFMultipageParameters.md)| A PdfSaveAsTIFFMultipageParameters object specifying the parameters of the action. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_document**
> PdfSaveDocumentResponse save_document(pdf_save_document_parameters)

Saves a previously uploaded document as PDF, and sends the file data in a JSON-serialized object.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_save_document_parameters = openapi_client.PdfSaveDocumentParameters() # PdfSaveDocumentParameters | A PdfSaveDocumentParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded document as PDF, and sends the file data in a JSON-serialized object.
        api_response = api_instance.save_document(pdf_save_document_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->save_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_save_document_parameters** | [**PdfSaveDocumentParameters**](PdfSaveDocumentParameters.md)| A PdfSaveDocumentParameters object specifying the parameters of the action. | 

### Return type

[**PdfSaveDocumentResponse**](PdfSaveDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_document_to_file**
> file save_document_to_file(pdf_save_document_parameters)

Saves a previously uploaded document as PDF, and streams the file binary data to the response (this is the most efficient download method).

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_save_document_parameters = openapi_client.PdfSaveDocumentParameters() # PdfSaveDocumentParameters | A PdfSaveDocumentParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded document as PDF, and streams the file binary data to the response (this is the most efficient download method).
        api_response = api_instance.save_document_to_file(pdf_save_document_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->save_document_to_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_save_document_parameters** | [**PdfSaveDocumentParameters**](PdfSaveDocumentParameters.md)| A PdfSaveDocumentParameters object specifying the parameters of the action. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scale_page**
> PdfScalePageResponse scale_page(pdf_scale_page_parameters)

Scales a page range from a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_scale_page_parameters = openapi_client.PdfScalePageParameters() # PdfScalePageParameters | A PdfScalePage object specifying the parameters of the action.

    try:
        # Scales a page range from a previously uploaded document.
        api_response = api_instance.scale_page(pdf_scale_page_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->scale_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_scale_page_parameters** | [**PdfScalePageParameters**](PdfScalePageParameters.md)| A PdfScalePage object specifying the parameters of the action. | 

### Return type

[**PdfScalePageResponse**](PdfScalePageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_info**
> PdfSetInfoResponse set_info(pdf_set_info_parameters)

Sets information to a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_set_info_parameters = openapi_client.PdfSetInfoParameters() # PdfSetInfoParameters | A PdfSetInfoParameters object specifying the parameters of the action.

    try:
        # Sets information to a previously uploaded document.
        api_response = api_instance.set_info(pdf_set_info_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->set_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_set_info_parameters** | [**PdfSetInfoParameters**](PdfSetInfoParameters.md)| A PdfSetInfoParameters object specifying the parameters of the action. | 

### Return type

[**PdfSetInfoResponse**](PdfSetInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_initial_view**
> PdfSetInitialViewResponse set_initial_view(pdf_set_initial_view_parameters)

Sets various document level initial view options to a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_set_initial_view_parameters = openapi_client.PdfSetInitialViewParameters() # PdfSetInitialViewParameters | A PdfsetInitialViewParameters object specifying the parameters of the action.

    try:
        # Sets various document level initial view options to a previously uploaded document.
        api_response = api_instance.set_initial_view(pdf_set_initial_view_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->set_initial_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_set_initial_view_parameters** | [**PdfSetInitialViewParameters**](PdfSetInitialViewParameters.md)| A PdfsetInitialViewParameters object specifying the parameters of the action. | 

### Return type

[**PdfSetInitialViewResponse**](PdfSetInitialViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_page_box**
> PdfSetPageBoxResponse set_page_box(pdf_set_page_box_parameters)

Sets pagebox to a page range from previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_set_page_box_parameters = openapi_client.PdfSetPageBoxParameters() # PdfSetPageBoxParameters | A PdfSetPageBoxParameters object specifying the parameters of the action.

    try:
        # Sets pagebox to a page range from previously uploaded document.
        api_response = api_instance.set_page_box(pdf_set_page_box_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->set_page_box: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_set_page_box_parameters** | [**PdfSetPageBoxParameters**](PdfSetPageBoxParameters.md)| A PdfSetPageBoxParameters object specifying the parameters of the action. | 

### Return type

[**PdfSetPageBoxResponse**](PdfSetPageBoxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_password**
> PdfSetPasswordResponse set_password(pdf_set_password_parameters)

Unprotects a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_set_password_parameters = openapi_client.PdfSetPasswordParameters() # PdfSetPasswordParameters | A PdfSetPasswordParameters object specifying the parameters of the action.

    try:
        # Unprotects a previously uploaded document.
        api_response = api_instance.set_password(pdf_set_password_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->set_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_set_password_parameters** | [**PdfSetPasswordParameters**](PdfSetPasswordParameters.md)| A PdfSetPasswordParameters object specifying the parameters of the action. | 

### Return type

[**PdfSetPasswordResponse**](PdfSetPasswordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split**
> PdfSplitResponse split(pdf_split_parameters)

Splits a previously uploaded document into new ones.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_split_parameters = openapi_client.PdfSplitParameters() # PdfSplitParameters | A PdfSplitParameters object specifying the parameters of the action.

    try:
        # Splits a previously uploaded document into new ones.
        api_response = api_instance.split(pdf_split_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->split: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_split_parameters** | [**PdfSplitParameters**](PdfSplitParameters.md)| A PdfSplitParameters object specifying the parameters of the action. | 

### Return type

[**PdfSplitResponse**](PdfSplitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swap_pages**
> PdfSwapPagesResponse swap_pages(pdf_swap_pages_parameters)

Swaps two pages from a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_swap_pages_parameters = openapi_client.PdfSwapPagesParameters() # PdfSwapPagesParameters | A PdfSwapPagesParameters object specifying the parameters of the action.

    try:
        # Swaps two pages from a previously uploaded document.
        api_response = api_instance.swap_pages(pdf_swap_pages_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->swap_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_swap_pages_parameters** | [**PdfSwapPagesParameters**](PdfSwapPagesParameters.md)| A PdfSwapPagesParameters object specifying the parameters of the action. | 

### Return type

[**PdfSwapPagesResponse**](PdfSwapPagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unprotect**
> PdfUnprotectResponse unprotect(pdf_unprotect_parameters)

Unprotects a previously uploaded document.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PDFApi(api_client)
    pdf_unprotect_parameters = openapi_client.PdfUnprotectParameters() # PdfUnprotectParameters | A PdfUnprotectParameters object specifying the parameters of the action.

    try:
        # Unprotects a previously uploaded document.
        api_response = api_instance.unprotect(pdf_unprotect_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFApi->unprotect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_unprotect_parameters** | [**PdfUnprotectParameters**](PdfUnprotectParameters.md)| A PdfUnprotectParameters object specifying the parameters of the action. | 

### Return type

[**PdfUnprotectResponse**](PdfUnprotectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

