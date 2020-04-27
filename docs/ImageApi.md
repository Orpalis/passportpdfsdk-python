# openapi_client.ImageApi

All URIs are relative to *https://passportpdfapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_adjust**](ImageApi.md#image_adjust) | **POST** /api/image/ImageAdjust | Adjusts a previously uploaded image.
[**image_auto_crop**](ImageApi.md#image_auto_crop) | **POST** /api/image/ImageAutoCrop | Automatically crops a previously uploaded image.
[**image_cleanup_document**](ImageApi.md#image_cleanup_document) | **POST** /api/image/ImageCleanupDocument | Cleanup a previously uploaded image.
[**image_clone_regions**](ImageApi.md#image_clone_regions) | **POST** /api/image/ImageCloneRegions | Clones regions from a previously uploaded image into new images.
[**image_close**](ImageApi.md#image_close) | **POST** /api/image/ImageClose | Closes a previously uploaded image.
[**image_convert_color_depth**](ImageApi.md#image_convert_color_depth) | **POST** /api/image/ImageConvertColorDepth | Converts the color depth of a previously uploaded image.
[**image_crop**](ImageApi.md#image_crop) | **POST** /api/image/ImageCrop | Crops a previously uploaded image.
[**image_delete_page**](ImageApi.md#image_delete_page) | **POST** /api/image/ImageDeletePage | Deletes a page range from a previously uploaded image.
[**image_detect_blank_pages**](ImageApi.md#image_detect_blank_pages) | **POST** /api/image/ImageDetectBlankPages | Detects the blank page(s) from a previously uploaded image and offers to remove them.
[**image_detect_color**](ImageApi.md#image_detect_color) | **POST** /api/image/ImageDetectColor | Performs color detection  on a previously uploaded image.
[**image_detect_page_orientation**](ImageApi.md#image_detect_page_orientation) | **POST** /api/image/ImageDetectPageOrientation | Detects the orientation of the page(s) of a previously uploaded image and offers to automatically rotate them.
[**image_filter**](ImageApi.md#image_filter) | **POST** /api/image/ImageFilter | Applies filters to a previously uploaded image.
[**image_get_page_thumbnail**](ImageApi.md#image_get_page_thumbnail) | **POST** /api/image/ImageGetPageThumbnail | Gets a thumbnail of each page within the provided page range from a previously uploaded image.
[**image_get_supported_file_extensions**](ImageApi.md#image_get_supported_file_extensions) | **GET** /api/image/ImageGetSupportedFileExtensions | Gets the supported file extensions by the image loading actions.
[**image_load**](ImageApi.md#image_load) | **POST** /api/image/ImageLoad | Loads the provided image file.  Supported image formats can be retrieved by the GetSupportedImageFileExtensions action.
[**image_load_multipart**](ImageApi.md#image_load_multipart) | **POST** /api/image/ImageLoadMultipart | Loads the provided image file using Multipart Upload.  Supported image formats can be retrieved by the GetSupportedImageFileExtensions action.
[**image_micr**](ImageApi.md#image_micr) | **POST** /api/image/ImageMICR | Performs MICR (Magnetic Ink Character Recognition) on a previously uploaded image.
[**image_read_barcodes**](ImageApi.md#image_read_barcodes) | **POST** /api/image/ImageReadBarcodes | Reads barcodes from a previously uploaded image.
[**image_resize**](ImageApi.md#image_resize) | **POST** /api/image/ImageResize | Resizes a previously uploaded image.
[**image_rotate**](ImageApi.md#image_rotate) | **POST** /api/image/ImageRotate | Rotates and/or flips a previously uploaded image.
[**image_save_as_jpeg**](ImageApi.md#image_save_as_jpeg) | **POST** /api/image/ImageSaveAsJPEG | Saves a previously uploaded image as JPEG, and sends the file data in a JSON-serialized object.
[**image_save_as_jpeg_file**](ImageApi.md#image_save_as_jpeg_file) | **POST** /api/image/ImageSaveAsJPEGFile | Saves a previously uploaded image as JPEG, and streams the file binary data to the response (this is the most efficient download method).
[**image_save_as_pdf**](ImageApi.md#image_save_as_pdf) | **POST** /api/image/ImageSaveAsPDF | Saves a previously uploaded image as PDF, and sends the file data in a JSON-serialized object.
[**image_save_as_pdf_file**](ImageApi.md#image_save_as_pdf_file) | **POST** /api/image/ImageSaveAsPDFFile | Saves a previously uploaded image as PDF, and streams the file binary data to the response (this is the most efficient download method).
[**image_save_as_pdfmrc**](ImageApi.md#image_save_as_pdfmrc) | **POST** /api/image/ImageSaveAsPDFMRC | Saves a previously uploaded image as PDF using MRC compression, and sends the file data in a JSON-serialized object.
[**image_save_as_pdfmrc_file**](ImageApi.md#image_save_as_pdfmrc_file) | **POST** /api/image/ImageSaveAsPDFMRCFile | Saves a previously uploaded image as PDF using MRC compression, and streams the file binary data to the response (this is the most efficient download method).
[**image_save_as_png**](ImageApi.md#image_save_as_png) | **POST** /api/image/ImageSaveAsPNG | Saves a previously uploaded image as PNG, and sends the file data in a JSON-serialized object.
[**image_save_as_png_file**](ImageApi.md#image_save_as_png_file) | **POST** /api/image/ImageSaveAsPNGFile | Saves a previously uploaded image as PNG, and streams the file binary data to the response (this is the most efficient download method).
[**image_save_as_tiff**](ImageApi.md#image_save_as_tiff) | **POST** /api/image/ImageSaveAsTIFF | Saves a previously uploaded image as TIFF, and sends the file data in a JSON-serialized object.
[**image_save_as_tiff_file**](ImageApi.md#image_save_as_tiff_file) | **POST** /api/image/ImageSaveAsTIFFFile | Saves a previously uploaded image as TIFF, and streams the file binary data to the response (this is the most efficient download method).
[**image_save_as_tiff_multipage**](ImageApi.md#image_save_as_tiff_multipage) | **POST** /api/image/ImageSaveAsTIFFMultipage | Saves a previously uploaded image as multipage TIFF, and sends the file data in a JSON-serialized object.
[**image_save_as_tiff_multipage_file**](ImageApi.md#image_save_as_tiff_multipage_file) | **POST** /api/image/ImageSaveAsTIFFMultipageFile | Saves a previously uploaded image as multipage TIFF, and streams the file binary data to the response (this is the most efficient download method).
[**image_swap_pages**](ImageApi.md#image_swap_pages) | **POST** /api/image/ImageSwapPages | Swaps two pages from a previously uploaded image.


# **image_adjust**
> ImageAdjustResponse image_adjust(image_adjust_parameters)

Adjusts a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_adjust_parameters = openapi_client.ImageAdjustParameters() # ImageAdjustParameters | An ImageAdjustParameters object specifying the parameters for the action.

    try:
        # Adjusts a previously uploaded image.
        api_response = api_instance.image_adjust(image_adjust_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_adjust: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_adjust_parameters** | [**ImageAdjustParameters**](ImageAdjustParameters.md)| An ImageAdjustParameters object specifying the parameters for the action. | 

### Return type

[**ImageAdjustResponse**](ImageAdjustResponse.md)

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

# **image_auto_crop**
> ImageAutoCropResponse image_auto_crop(image_auto_crop_parameters)

Automatically crops a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_auto_crop_parameters = openapi_client.ImageAutoCropParameters() # ImageAutoCropParameters | An ImageAutoCropParameters object specifying the parameters for the action.

    try:
        # Automatically crops a previously uploaded image.
        api_response = api_instance.image_auto_crop(image_auto_crop_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_auto_crop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_auto_crop_parameters** | [**ImageAutoCropParameters**](ImageAutoCropParameters.md)| An ImageAutoCropParameters object specifying the parameters for the action. | 

### Return type

[**ImageAutoCropResponse**](ImageAutoCropResponse.md)

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

# **image_cleanup_document**
> ImageCleanupDocumentResponse image_cleanup_document(image_cleanup_document_parameters)

Cleanup a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_cleanup_document_parameters = openapi_client.ImageCleanupDocumentParameters() # ImageCleanupDocumentParameters | An ImageCleanupDocumentParameters object specifying the parameters for the action.

    try:
        # Cleanup a previously uploaded image.
        api_response = api_instance.image_cleanup_document(image_cleanup_document_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_cleanup_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_cleanup_document_parameters** | [**ImageCleanupDocumentParameters**](ImageCleanupDocumentParameters.md)| An ImageCleanupDocumentParameters object specifying the parameters for the action. | 

### Return type

[**ImageCleanupDocumentResponse**](ImageCleanupDocumentResponse.md)

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

# **image_clone_regions**
> ImageCloneRegionsResponse image_clone_regions(image_clone_regions_parameters)

Clones regions from a previously uploaded image into new images.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_clone_regions_parameters = openapi_client.ImageCloneRegionsParameters() # ImageCloneRegionsParameters | An ImageCloneRegionsParameters object specifying the parameters of the action.

    try:
        # Clones regions from a previously uploaded image into new images.
        api_response = api_instance.image_clone_regions(image_clone_regions_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_clone_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_clone_regions_parameters** | [**ImageCloneRegionsParameters**](ImageCloneRegionsParameters.md)| An ImageCloneRegionsParameters object specifying the parameters of the action. | 

### Return type

[**ImageCloneRegionsResponse**](ImageCloneRegionsResponse.md)

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

# **image_close**
> ImageCloseResponse image_close(image_close_parameters)

Closes a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_close_parameters = openapi_client.ImageCloseParameters() # ImageCloseParameters | An ImageCloseParameters object specifying the parameters of the action.

    try:
        # Closes a previously uploaded image.
        api_response = api_instance.image_close(image_close_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_close_parameters** | [**ImageCloseParameters**](ImageCloseParameters.md)| An ImageCloseParameters object specifying the parameters of the action. | 

### Return type

[**ImageCloseResponse**](ImageCloseResponse.md)

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

# **image_convert_color_depth**
> ImageConvertColorDepthResponse image_convert_color_depth(image_convert_color_depth_parameters)

Converts the color depth of a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_convert_color_depth_parameters = openapi_client.ImageConvertColorDepthParameters() # ImageConvertColorDepthParameters | An ImageConvertColorDepthParameters object specifying the parameters for the action.

    try:
        # Converts the color depth of a previously uploaded image.
        api_response = api_instance.image_convert_color_depth(image_convert_color_depth_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_convert_color_depth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_convert_color_depth_parameters** | [**ImageConvertColorDepthParameters**](ImageConvertColorDepthParameters.md)| An ImageConvertColorDepthParameters object specifying the parameters for the action. | 

### Return type

[**ImageConvertColorDepthResponse**](ImageConvertColorDepthResponse.md)

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

# **image_crop**
> ImageCropResponse image_crop(image_crop_parameters)

Crops a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_crop_parameters = openapi_client.ImageCropParameters() # ImageCropParameters | An ImageCropParameters object specifying the parameters for the action.

    try:
        # Crops a previously uploaded image.
        api_response = api_instance.image_crop(image_crop_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_crop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_crop_parameters** | [**ImageCropParameters**](ImageCropParameters.md)| An ImageCropParameters object specifying the parameters for the action. | 

### Return type

[**ImageCropResponse**](ImageCropResponse.md)

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

# **image_delete_page**
> ImageDeletePageResponse image_delete_page(image_delete_page_parameters)

Deletes a page range from a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_delete_page_parameters = openapi_client.ImageDeletePageParameters() # ImageDeletePageParameters | An ImageDeletePageParameters object specifying the parameters of the action.

    try:
        # Deletes a page range from a previously uploaded image.
        api_response = api_instance.image_delete_page(image_delete_page_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_delete_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_delete_page_parameters** | [**ImageDeletePageParameters**](ImageDeletePageParameters.md)| An ImageDeletePageParameters object specifying the parameters of the action. | 

### Return type

[**ImageDeletePageResponse**](ImageDeletePageResponse.md)

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

# **image_detect_blank_pages**
> ImageDetectBlankPagesResponse image_detect_blank_pages(image_detect_blank_pages_parameters)

Detects the blank page(s) from a previously uploaded image and offers to remove them.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_detect_blank_pages_parameters = openapi_client.ImageDetectBlankPagesParameters() # ImageDetectBlankPagesParameters | An ImageDetectBlankPagesParameters object specifying the parameters of the action.

    try:
        # Detects the blank page(s) from a previously uploaded image and offers to remove them.
        api_response = api_instance.image_detect_blank_pages(image_detect_blank_pages_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_detect_blank_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_detect_blank_pages_parameters** | [**ImageDetectBlankPagesParameters**](ImageDetectBlankPagesParameters.md)| An ImageDetectBlankPagesParameters object specifying the parameters of the action. | 

### Return type

[**ImageDetectBlankPagesResponse**](ImageDetectBlankPagesResponse.md)

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

# **image_detect_color**
> ImageDetectColorResponse image_detect_color(image_detect_color_parameters)

Performs color detection  on a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_detect_color_parameters = openapi_client.ImageDetectColorParameters() # ImageDetectColorParameters | An ImageDetectColorParameters object specifying the parameters for the action.

    try:
        # Performs color detection  on a previously uploaded image.
        api_response = api_instance.image_detect_color(image_detect_color_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_detect_color: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_detect_color_parameters** | [**ImageDetectColorParameters**](ImageDetectColorParameters.md)| An ImageDetectColorParameters object specifying the parameters for the action. | 

### Return type

[**ImageDetectColorResponse**](ImageDetectColorResponse.md)

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

# **image_detect_page_orientation**
> ImageDetectPageOrientationResponse image_detect_page_orientation(image_detect_page_orientation_parameters)

Detects the orientation of the page(s) of a previously uploaded image and offers to automatically rotate them.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_detect_page_orientation_parameters = openapi_client.ImageDetectPageOrientationParameters() # ImageDetectPageOrientationParameters | An ImagedetectPageOrientationParameters object specifying the parameters of the action.

    try:
        # Detects the orientation of the page(s) of a previously uploaded image and offers to automatically rotate them.
        api_response = api_instance.image_detect_page_orientation(image_detect_page_orientation_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_detect_page_orientation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_detect_page_orientation_parameters** | [**ImageDetectPageOrientationParameters**](ImageDetectPageOrientationParameters.md)| An ImagedetectPageOrientationParameters object specifying the parameters of the action. | 

### Return type

[**ImageDetectPageOrientationResponse**](ImageDetectPageOrientationResponse.md)

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

# **image_filter**
> ImageFilterResponse image_filter(image_filter_parameters)

Applies filters to a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_filter_parameters = openapi_client.ImageFilterParameters() # ImageFilterParameters | An ImageFilterParameters object specifying the parameters for the action.

    try:
        # Applies filters to a previously uploaded image.
        api_response = api_instance.image_filter(image_filter_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_filter_parameters** | [**ImageFilterParameters**](ImageFilterParameters.md)| An ImageFilterParameters object specifying the parameters for the action. | 

### Return type

[**ImageFilterResponse**](ImageFilterResponse.md)

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

# **image_get_page_thumbnail**
> ImageGetPageThumbnailResponse image_get_page_thumbnail(image_get_page_thumbnail_parameters)

Gets a thumbnail of each page within the provided page range from a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_get_page_thumbnail_parameters = openapi_client.ImageGetPageThumbnailParameters() # ImageGetPageThumbnailParameters | A PDFGetPageThumbnailParameters object specifying the parameters of the action.

    try:
        # Gets a thumbnail of each page within the provided page range from a previously uploaded image.
        api_response = api_instance.image_get_page_thumbnail(image_get_page_thumbnail_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_get_page_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_get_page_thumbnail_parameters** | [**ImageGetPageThumbnailParameters**](ImageGetPageThumbnailParameters.md)| A PDFGetPageThumbnailParameters object specifying the parameters of the action. | 

### Return type

[**ImageGetPageThumbnailResponse**](ImageGetPageThumbnailResponse.md)

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

# **image_get_supported_file_extensions**
> StringArrayResponse image_get_supported_file_extensions()

Gets the supported file extensions by the image loading actions.

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
    api_instance = openapi_client.ImageApi(api_client)
    
    try:
        # Gets the supported file extensions by the image loading actions.
        api_response = api_instance.image_get_supported_file_extensions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_get_supported_file_extensions: %s\n" % e)
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

# **image_load**
> ImageLoadResponse image_load(load_image_from_byte_array_parameters)

Loads the provided image file.  Supported image formats can be retrieved by the GetSupportedImageFileExtensions action.

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
    api_instance = openapi_client.ImageApi(api_client)
    load_image_from_byte_array_parameters = openapi_client.LoadImageFromByteArrayParameters() # LoadImageFromByteArrayParameters | A LoadImageFromByteArrayParameters object specifying the parameters of the action.

    try:
        # Loads the provided image file.  Supported image formats can be retrieved by the GetSupportedImageFileExtensions action.
        api_response = api_instance.image_load(load_image_from_byte_array_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_load: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_image_from_byte_array_parameters** | [**LoadImageFromByteArrayParameters**](LoadImageFromByteArrayParameters.md)| A LoadImageFromByteArrayParameters object specifying the parameters of the action. | 

### Return type

[**ImageLoadResponse**](ImageLoadResponse.md)

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

# **image_load_multipart**
> ImageLoadResponse image_load_multipart(file_data, load_image_parameters=load_image_parameters)

Loads the provided image file using Multipart Upload.  Supported image formats can be retrieved by the GetSupportedImageFileExtensions action.

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
    api_instance = openapi_client.ImageApi(api_client)
    file_data = '/path/to/file' # file | The data of the document.
load_image_parameters = openapi_client.LoadImageParameters() # LoadImageParameters |  (optional)

    try:
        # Loads the provided image file using Multipart Upload.  Supported image formats can be retrieved by the GetSupportedImageFileExtensions action.
        api_response = api_instance.image_load_multipart(file_data, load_image_parameters=load_image_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_load_multipart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_data** | **file**| The data of the document. | 
 **load_image_parameters** | [**LoadImageParameters**](LoadImageParameters.md)|  | [optional] 

### Return type

[**ImageLoadResponse**](ImageLoadResponse.md)

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

# **image_micr**
> ImageMICRResponse image_micr(image_micr_parameters)

Performs MICR (Magnetic Ink Character Recognition) on a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_micr_parameters = openapi_client.ImageMICRParameters() # ImageMICRParameters | An ImageMICRParameters object specifying the parameters of the action.

    try:
        # Performs MICR (Magnetic Ink Character Recognition) on a previously uploaded image.
        api_response = api_instance.image_micr(image_micr_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_micr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_micr_parameters** | [**ImageMICRParameters**](ImageMICRParameters.md)| An ImageMICRParameters object specifying the parameters of the action. | 

### Return type

[**ImageMICRResponse**](ImageMICRResponse.md)

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

# **image_read_barcodes**
> ReadBarcodesResponse image_read_barcodes(image_read_barcodes_parameters)

Reads barcodes from a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_read_barcodes_parameters = openapi_client.ImageReadBarcodesParameters() # ImageReadBarcodesParameters | An ImageReadBarcodesParameters object specifying the parameters of the action.

    try:
        # Reads barcodes from a previously uploaded image.
        api_response = api_instance.image_read_barcodes(image_read_barcodes_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_read_barcodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_read_barcodes_parameters** | [**ImageReadBarcodesParameters**](ImageReadBarcodesParameters.md)| An ImageReadBarcodesParameters object specifying the parameters of the action. | 

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

# **image_resize**
> ImageResizeResponse image_resize(image_resize_parameters)

Resizes a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_resize_parameters = openapi_client.ImageResizeParameters() # ImageResizeParameters | An ImageResizeParameters object specifying the parameters for the action.

    try:
        # Resizes a previously uploaded image.
        api_response = api_instance.image_resize(image_resize_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_resize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_resize_parameters** | [**ImageResizeParameters**](ImageResizeParameters.md)| An ImageResizeParameters object specifying the parameters for the action. | 

### Return type

[**ImageResizeResponse**](ImageResizeResponse.md)

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

# **image_rotate**
> ImageRotateResponse image_rotate(image_rotate_parameters)

Rotates and/or flips a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_rotate_parameters = openapi_client.ImageRotateParameters() # ImageRotateParameters | An ImageRotateParameters object specifying the parameters for the action.

    try:
        # Rotates and/or flips a previously uploaded image.
        api_response = api_instance.image_rotate(image_rotate_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_rotate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_rotate_parameters** | [**ImageRotateParameters**](ImageRotateParameters.md)| An ImageRotateParameters object specifying the parameters for the action. | 

### Return type

[**ImageRotateResponse**](ImageRotateResponse.md)

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

# **image_save_as_jpeg**
> ImageSaveAsJPEGResponse image_save_as_jpeg(image_save_as_jpeg_parameters)

Saves a previously uploaded image as JPEG, and sends the file data in a JSON-serialized object.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_jpeg_parameters = openapi_client.ImageSaveAsJPEGParameters() # ImageSaveAsJPEGParameters | An ImageSaveAsJPEGParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as JPEG, and sends the file data in a JSON-serialized object.
        api_response = api_instance.image_save_as_jpeg(image_save_as_jpeg_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_jpeg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_jpeg_parameters** | [**ImageSaveAsJPEGParameters**](ImageSaveAsJPEGParameters.md)| An ImageSaveAsJPEGParameters object specifying the parameters of the action. | 

### Return type

[**ImageSaveAsJPEGResponse**](ImageSaveAsJPEGResponse.md)

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

# **image_save_as_jpeg_file**
> file image_save_as_jpeg_file(image_save_as_jpeg_parameters)

Saves a previously uploaded image as JPEG, and streams the file binary data to the response (this is the most efficient download method).

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_jpeg_parameters = openapi_client.ImageSaveAsJPEGParameters() # ImageSaveAsJPEGParameters | An ImageSaveAsJPEGParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as JPEG, and streams the file binary data to the response (this is the most efficient download method).
        api_response = api_instance.image_save_as_jpeg_file(image_save_as_jpeg_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_jpeg_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_jpeg_parameters** | [**ImageSaveAsJPEGParameters**](ImageSaveAsJPEGParameters.md)| An ImageSaveAsJPEGParameters object specifying the parameters of the action. | 

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

# **image_save_as_pdf**
> ImageSaveAsPDFResponse image_save_as_pdf(image_save_as_pdf_parameters)

Saves a previously uploaded image as PDF, and sends the file data in a JSON-serialized object.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_pdf_parameters = openapi_client.ImageSaveAsPDFParameters() # ImageSaveAsPDFParameters | An ImagesaveAsPDFParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as PDF, and sends the file data in a JSON-serialized object.
        api_response = api_instance.image_save_as_pdf(image_save_as_pdf_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_pdf_parameters** | [**ImageSaveAsPDFParameters**](ImageSaveAsPDFParameters.md)| An ImagesaveAsPDFParameters object specifying the parameters of the action. | 

### Return type

[**ImageSaveAsPDFResponse**](ImageSaveAsPDFResponse.md)

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

# **image_save_as_pdf_file**
> file image_save_as_pdf_file(image_save_as_pdf_parameters)

Saves a previously uploaded image as PDF, and streams the file binary data to the response (this is the most efficient download method).

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_pdf_parameters = openapi_client.ImageSaveAsPDFParameters() # ImageSaveAsPDFParameters | An ImagesaveAsPDFParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as PDF, and streams the file binary data to the response (this is the most efficient download method).
        api_response = api_instance.image_save_as_pdf_file(image_save_as_pdf_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_pdf_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_pdf_parameters** | [**ImageSaveAsPDFParameters**](ImageSaveAsPDFParameters.md)| An ImagesaveAsPDFParameters object specifying the parameters of the action. | 

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

# **image_save_as_pdfmrc**
> ImageSaveAsPDFMRCResponse image_save_as_pdfmrc(image_save_as_pdfmrc_parameters)

Saves a previously uploaded image as PDF using MRC compression, and sends the file data in a JSON-serialized object.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_pdfmrc_parameters = openapi_client.ImageSaveAsPDFMRCParameters() # ImageSaveAsPDFMRCParameters | An ImagesaveAsPDFMRCParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as PDF using MRC compression, and sends the file data in a JSON-serialized object.
        api_response = api_instance.image_save_as_pdfmrc(image_save_as_pdfmrc_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_pdfmrc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_pdfmrc_parameters** | [**ImageSaveAsPDFMRCParameters**](ImageSaveAsPDFMRCParameters.md)| An ImagesaveAsPDFMRCParameters object specifying the parameters of the action. | 

### Return type

[**ImageSaveAsPDFMRCResponse**](ImageSaveAsPDFMRCResponse.md)

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

# **image_save_as_pdfmrc_file**
> file image_save_as_pdfmrc_file(image_save_as_pdfmrc_parameters)

Saves a previously uploaded image as PDF using MRC compression, and streams the file binary data to the response (this is the most efficient download method).

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_pdfmrc_parameters = openapi_client.ImageSaveAsPDFMRCParameters() # ImageSaveAsPDFMRCParameters | An ImagesaveAsPDFMRCParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as PDF using MRC compression, and streams the file binary data to the response (this is the most efficient download method).
        api_response = api_instance.image_save_as_pdfmrc_file(image_save_as_pdfmrc_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_pdfmrc_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_pdfmrc_parameters** | [**ImageSaveAsPDFMRCParameters**](ImageSaveAsPDFMRCParameters.md)| An ImagesaveAsPDFMRCParameters object specifying the parameters of the action. | 

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

# **image_save_as_png**
> ImageSaveAsPNGResponse image_save_as_png(image_save_as_png_parameters)

Saves a previously uploaded image as PNG, and sends the file data in a JSON-serialized object.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_png_parameters = openapi_client.ImageSaveAsPNGParameters() # ImageSaveAsPNGParameters | An ImageSaveAsPNGParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as PNG, and sends the file data in a JSON-serialized object.
        api_response = api_instance.image_save_as_png(image_save_as_png_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_png_parameters** | [**ImageSaveAsPNGParameters**](ImageSaveAsPNGParameters.md)| An ImageSaveAsPNGParameters object specifying the parameters of the action. | 

### Return type

[**ImageSaveAsPNGResponse**](ImageSaveAsPNGResponse.md)

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

# **image_save_as_png_file**
> file image_save_as_png_file(image_save_as_png_parameters)

Saves a previously uploaded image as PNG, and streams the file binary data to the response (this is the most efficient download method).

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_png_parameters = openapi_client.ImageSaveAsPNGParameters() # ImageSaveAsPNGParameters | An ImageSaveAsPNGParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as PNG, and streams the file binary data to the response (this is the most efficient download method).
        api_response = api_instance.image_save_as_png_file(image_save_as_png_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_png_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_png_parameters** | [**ImageSaveAsPNGParameters**](ImageSaveAsPNGParameters.md)| An ImageSaveAsPNGParameters object specifying the parameters of the action. | 

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

# **image_save_as_tiff**
> ImageSaveAsTIFFResponse image_save_as_tiff(image_save_as_tiff_parameters)

Saves a previously uploaded image as TIFF, and sends the file data in a JSON-serialized object.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_tiff_parameters = openapi_client.ImageSaveAsTIFFParameters() # ImageSaveAsTIFFParameters | An ImageSaveAsTIFFParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as TIFF, and sends the file data in a JSON-serialized object.
        api_response = api_instance.image_save_as_tiff(image_save_as_tiff_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_tiff_parameters** | [**ImageSaveAsTIFFParameters**](ImageSaveAsTIFFParameters.md)| An ImageSaveAsTIFFParameters object specifying the parameters of the action. | 

### Return type

[**ImageSaveAsTIFFResponse**](ImageSaveAsTIFFResponse.md)

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

# **image_save_as_tiff_file**
> file image_save_as_tiff_file(image_save_as_tiff_parameters)

Saves a previously uploaded image as TIFF, and streams the file binary data to the response (this is the most efficient download method).

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_tiff_parameters = openapi_client.ImageSaveAsTIFFParameters() # ImageSaveAsTIFFParameters | An ImageSaveAsTIFFParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as TIFF, and streams the file binary data to the response (this is the most efficient download method).
        api_response = api_instance.image_save_as_tiff_file(image_save_as_tiff_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_tiff_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_tiff_parameters** | [**ImageSaveAsTIFFParameters**](ImageSaveAsTIFFParameters.md)| An ImageSaveAsTIFFParameters object specifying the parameters of the action. | 

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

# **image_save_as_tiff_multipage**
> ImageSaveAsTIFFMultipageResponse image_save_as_tiff_multipage(image_save_as_tiff_multipage_parameters)

Saves a previously uploaded image as multipage TIFF, and sends the file data in a JSON-serialized object.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_tiff_multipage_parameters = openapi_client.ImageSaveAsTIFFMultipageParameters() # ImageSaveAsTIFFMultipageParameters | An ImageSaveAsTIFFMultipageParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as multipage TIFF, and sends the file data in a JSON-serialized object.
        api_response = api_instance.image_save_as_tiff_multipage(image_save_as_tiff_multipage_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_tiff_multipage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_tiff_multipage_parameters** | [**ImageSaveAsTIFFMultipageParameters**](ImageSaveAsTIFFMultipageParameters.md)| An ImageSaveAsTIFFMultipageParameters object specifying the parameters of the action. | 

### Return type

[**ImageSaveAsTIFFMultipageResponse**](ImageSaveAsTIFFMultipageResponse.md)

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

# **image_save_as_tiff_multipage_file**
> file image_save_as_tiff_multipage_file(image_save_as_tiff_multipage_parameters)

Saves a previously uploaded image as multipage TIFF, and streams the file binary data to the response (this is the most efficient download method).

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
    api_instance = openapi_client.ImageApi(api_client)
    image_save_as_tiff_multipage_parameters = openapi_client.ImageSaveAsTIFFMultipageParameters() # ImageSaveAsTIFFMultipageParameters | An ImageSaveAsTIFFMultipageParameters object specifying the parameters of the action.

    try:
        # Saves a previously uploaded image as multipage TIFF, and streams the file binary data to the response (this is the most efficient download method).
        api_response = api_instance.image_save_as_tiff_multipage_file(image_save_as_tiff_multipage_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_save_as_tiff_multipage_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_save_as_tiff_multipage_parameters** | [**ImageSaveAsTIFFMultipageParameters**](ImageSaveAsTIFFMultipageParameters.md)| An ImageSaveAsTIFFMultipageParameters object specifying the parameters of the action. | 

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

# **image_swap_pages**
> ImageSwapPagesResponse image_swap_pages(image_swap_pages_parameters)

Swaps two pages from a previously uploaded image.

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
    api_instance = openapi_client.ImageApi(api_client)
    image_swap_pages_parameters = openapi_client.ImageSwapPagesParameters() # ImageSwapPagesParameters | An ImageSwapPagesParameters object specifying the parameters of the action.

    try:
        # Swaps two pages from a previously uploaded image.
        api_response = api_instance.image_swap_pages(image_swap_pages_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->image_swap_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_swap_pages_parameters** | [**ImageSwapPagesParameters**](ImageSwapPagesParameters.md)| An ImageSwapPagesParameters object specifying the parameters of the action. | 

### Return type

[**ImageSwapPagesResponse**](ImageSwapPagesResponse.md)

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

