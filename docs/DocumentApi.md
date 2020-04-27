# openapi_client.DocumentApi

All URIs are relative to *https://passportpdfapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_close**](DocumentApi.md#document_close) | **POST** /api/document/DocumentClose | Closes a previously uploaded document.
[**document_get_preview**](DocumentApi.md#document_get_preview) | **POST** /api/document/DocumentGetPreview | Gets the format, the page count and a thumbnail of a previously uploaded document.
[**document_load**](DocumentApi.md#document_load) | **POST** /api/document/DocumentLoad | Loads the provided document file.
[**document_load_from_uri**](DocumentApi.md#document_load_from_uri) | **POST** /api/document/DocumentLoadFromURI | Loads the provided document file from an URI.
[**document_load_multipart**](DocumentApi.md#document_load_multipart) | **POST** /api/document/DocumentLoadMultipart | Loads the provided document file using Multipart Upload.


# **document_close**
> DocumentCloseResponse document_close(document_close_parameters)

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
    api_instance = openapi_client.DocumentApi(api_client)
    document_close_parameters = openapi_client.DocumentCloseParameters() # DocumentCloseParameters | A DocumentCloseParameters object specifying the parameters of the action.

    try:
        # Closes a previously uploaded document.
        api_response = api_instance.document_close(document_close_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->document_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_close_parameters** | [**DocumentCloseParameters**](DocumentCloseParameters.md)| A DocumentCloseParameters object specifying the parameters of the action. | 

### Return type

[**DocumentCloseResponse**](DocumentCloseResponse.md)

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

# **document_get_preview**
> DocumentGetPreviewResponse document_get_preview(get_document_preview_parameters)

Gets the format, the page count and a thumbnail of a previously uploaded document.

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
    api_instance = openapi_client.DocumentApi(api_client)
    get_document_preview_parameters = openapi_client.GetDocumentPreviewParameters() # GetDocumentPreviewParameters | A GetDocumentPreviewParameters object specifying the parameters of the action.

    try:
        # Gets the format, the page count and a thumbnail of a previously uploaded document.
        api_response = api_instance.document_get_preview(get_document_preview_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->document_get_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_document_preview_parameters** | [**GetDocumentPreviewParameters**](GetDocumentPreviewParameters.md)| A GetDocumentPreviewParameters object specifying the parameters of the action. | 

### Return type

[**DocumentGetPreviewResponse**](DocumentGetPreviewResponse.md)

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

# **document_load**
> DocumentLoadResponse document_load(load_document_from_byte_array_parameters)

Loads the provided document file.

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
    api_instance = openapi_client.DocumentApi(api_client)
    load_document_from_byte_array_parameters = openapi_client.LoadDocumentFromByteArrayParameters() # LoadDocumentFromByteArrayParameters | A LoadDocumentFromByteArrayParameters object specifying the parameters of the action.

    try:
        # Loads the provided document file.
        api_response = api_instance.document_load(load_document_from_byte_array_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->document_load: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_document_from_byte_array_parameters** | [**LoadDocumentFromByteArrayParameters**](LoadDocumentFromByteArrayParameters.md)| A LoadDocumentFromByteArrayParameters object specifying the parameters of the action. | 

### Return type

[**DocumentLoadResponse**](DocumentLoadResponse.md)

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

# **document_load_from_uri**
> DocumentLoadResponse document_load_from_uri(load_document_from_uri_parameters)

Loads the provided document file from an URI.

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
    api_instance = openapi_client.DocumentApi(api_client)
    load_document_from_uri_parameters = openapi_client.LoadDocumentFromURIParameters() # LoadDocumentFromURIParameters | A LoadDocumentFromURIParameters object specifying the parameters of the action.

    try:
        # Loads the provided document file from an URI.
        api_response = api_instance.document_load_from_uri(load_document_from_uri_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->document_load_from_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_document_from_uri_parameters** | [**LoadDocumentFromURIParameters**](LoadDocumentFromURIParameters.md)| A LoadDocumentFromURIParameters object specifying the parameters of the action. | 

### Return type

[**DocumentLoadResponse**](DocumentLoadResponse.md)

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

# **document_load_multipart**
> DocumentLoadResponse document_load_multipart(file_data, load_document_parameters=load_document_parameters)

Loads the provided document file using Multipart Upload.

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
    api_instance = openapi_client.DocumentApi(api_client)
    file_data = '/path/to/file' # file | The data of the document.
load_document_parameters = openapi_client.LoadDocumentParameters() # LoadDocumentParameters |  (optional)

    try:
        # Loads the provided document file using Multipart Upload.
        api_response = api_instance.document_load_multipart(file_data, load_document_parameters=load_document_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->document_load_multipart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_data** | **file**| The data of the document. | 
 **load_document_parameters** | [**LoadDocumentParameters**](LoadDocumentParameters.md)|  | [optional] 

### Return type

[**DocumentLoadResponse**](DocumentLoadResponse.md)

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

