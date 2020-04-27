# openapi_client.PassportPDFApplicationManagerApi

All URIs are relative to *https://passportpdfapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**passport_pdf_application_manager_get_application_download_link**](PassportPDFApplicationManagerApi.md#passport_pdf_application_manager_get_application_download_link) | **GET** /api/passportpdfapplicationmanager/PassportPDFApplicationManagerGetApplicationDownloadLink | 
[**passport_pdf_application_manager_get_application_latest_version**](PassportPDFApplicationManagerApi.md#passport_pdf_application_manager_get_application_latest_version) | **GET** /api/passportpdfapplicationmanager/PassportPDFApplicationManagerGetApplicationLatestVersion | 
[**passport_pdf_application_manager_get_application_minimum_supported_version**](PassportPDFApplicationManagerApi.md#passport_pdf_application_manager_get_application_minimum_supported_version) | **GET** /api/passportpdfapplicationmanager/PassportPDFApplicationManagerGetApplicationMinimumSupportedVersion | 
[**passport_pdf_application_manager_get_max_client_threads**](PassportPDFApplicationManagerApi.md#passport_pdf_application_manager_get_max_client_threads) | **GET** /api/passportpdfapplicationmanager/PassportPDFApplicationManagerGetMaxClientThreads | Gets the maximum number of threads to be used simultaneously by a client application.


# **passport_pdf_application_manager_get_application_download_link**
> StringResponse passport_pdf_application_manager_get_application_download_link(application_id)



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
    api_instance = openapi_client.PassportPDFApplicationManagerApi(api_client)
    application_id = 'application_id_example' # str | 

    try:
        api_response = api_instance.passport_pdf_application_manager_get_application_download_link(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PassportPDFApplicationManagerApi->passport_pdf_application_manager_get_application_download_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

### Return type

[**StringResponse**](StringResponse.md)

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

# **passport_pdf_application_manager_get_application_latest_version**
> StringResponse passport_pdf_application_manager_get_application_latest_version(application_id)



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
    api_instance = openapi_client.PassportPDFApplicationManagerApi(api_client)
    application_id = 'application_id_example' # str | 

    try:
        api_response = api_instance.passport_pdf_application_manager_get_application_latest_version(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PassportPDFApplicationManagerApi->passport_pdf_application_manager_get_application_latest_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

### Return type

[**StringResponse**](StringResponse.md)

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

# **passport_pdf_application_manager_get_application_minimum_supported_version**
> StringResponse passport_pdf_application_manager_get_application_minimum_supported_version(application_id)



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
    api_instance = openapi_client.PassportPDFApplicationManagerApi(api_client)
    application_id = 'application_id_example' # str | 

    try:
        api_response = api_instance.passport_pdf_application_manager_get_application_minimum_supported_version(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PassportPDFApplicationManagerApi->passport_pdf_application_manager_get_application_minimum_supported_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

### Return type

[**StringResponse**](StringResponse.md)

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

# **passport_pdf_application_manager_get_max_client_threads**
> IntegerResponse passport_pdf_application_manager_get_max_client_threads(application_id)

Gets the maximum number of threads to be used simultaneously by a client application.

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
    api_instance = openapi_client.PassportPDFApplicationManagerApi(api_client)
    application_id = 'application_id_example' # str | 

    try:
        # Gets the maximum number of threads to be used simultaneously by a client application.
        api_response = api_instance.passport_pdf_application_manager_get_max_client_threads(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PassportPDFApplicationManagerApi->passport_pdf_application_manager_get_max_client_threads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

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

