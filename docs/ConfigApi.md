# openapi_client.ConfigApi

All URIs are relative to *https://passportpdfapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_get_api_version**](ConfigApi.md#config_get_api_version) | **GET** /api/config/ConfigGetAPIVersion | 
[**config_get_max_allowed_content_length**](ConfigApi.md#config_get_max_allowed_content_length) | **GET** /api/config/ConfigGetMaxAllowedContentLength | Gets the maximal length of a request content, in bytes.
[**config_get_suggested_client_timeout**](ConfigApi.md#config_get_suggested_client_timeout) | **GET** /api/config/ConfigGetSuggestedClientTimeout | Gets the suggested client API timeout, in milliseconds.
[**config_get_suggested_max_client_threads**](ConfigApi.md#config_get_suggested_max_client_threads) | **GET** /api/config/ConfigGetSuggestedMaxClientThreads | Gets the suggested maximum number of threads to be used simultaneously by a client application.
[**config_get_supported_fonts**](ConfigApi.md#config_get_supported_fonts) | **GET** /api/config/ConfigGetSupportedFonts | Gets the list of supported fonts for text drawing operations.
[**config_get_supported_ocr_languages**](ConfigApi.md#config_get_supported_ocr_languages) | **GET** /api/config/ConfigGetSupportedOCRLanguages | Gets the list of supported languages for OCR.


# **config_get_api_version**
> str config_get_api_version()



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
    api_instance = openapi_client.ConfigApi(api_client)
    
    try:
        api_response = api_instance.config_get_api_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_api_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **config_get_max_allowed_content_length**
> LongResponse config_get_max_allowed_content_length()

Gets the maximal length of a request content, in bytes.

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
    api_instance = openapi_client.ConfigApi(api_client)
    
    try:
        # Gets the maximal length of a request content, in bytes.
        api_response = api_instance.config_get_max_allowed_content_length()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_max_allowed_content_length: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LongResponse**](LongResponse.md)

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

# **config_get_suggested_client_timeout**
> IntegerResponse config_get_suggested_client_timeout()

Gets the suggested client API timeout, in milliseconds.

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
    api_instance = openapi_client.ConfigApi(api_client)
    
    try:
        # Gets the suggested client API timeout, in milliseconds.
        api_response = api_instance.config_get_suggested_client_timeout()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_suggested_client_timeout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IntegerResponse**](IntegerResponse.md)

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

# **config_get_suggested_max_client_threads**
> IntegerResponse config_get_suggested_max_client_threads()

Gets the suggested maximum number of threads to be used simultaneously by a client application.

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
    api_instance = openapi_client.ConfigApi(api_client)
    
    try:
        # Gets the suggested maximum number of threads to be used simultaneously by a client application.
        api_response = api_instance.config_get_suggested_max_client_threads()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_suggested_max_client_threads: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IntegerResponse**](IntegerResponse.md)

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

# **config_get_supported_fonts**
> list[Font] config_get_supported_fonts()

Gets the list of supported fonts for text drawing operations.

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
    api_instance = openapi_client.ConfigApi(api_client)
    
    try:
        # Gets the list of supported fonts for text drawing operations.
        api_response = api_instance.config_get_supported_fonts()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_supported_fonts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Font]**](Font.md)

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

# **config_get_supported_ocr_languages**
> StringArrayResponse config_get_supported_ocr_languages()

Gets the list of supported languages for OCR.

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
    api_instance = openapi_client.ConfigApi(api_client)
    
    try:
        # Gets the list of supported languages for OCR.
        api_response = api_instance.config_get_supported_ocr_languages()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_supported_ocr_languages: %s\n" % e)
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

