# openapi_client.DocuViewareApi

All URIs are relative to *https://passportpdfapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**docu_vieware_get_control**](DocuViewareApi.md#docu_vieware_get_control) | **POST** /api/docuvieware/DocuViewareGetControl | Gets the HTML dom of a DocuVieware control.
[**docu_vieware_get_version**](DocuViewareApi.md#docu_vieware_get_version) | **GET** /api/docuvieware/DocuViewareGetVersion | Get the DocuVieware engine version.
[**docu_vieware_save**](DocuViewareApi.md#docu_vieware_save) | **POST** /api/docuvieware/DocuViewareSave | Saves the document being handled by a specific DocuVieware control, in its current state.


# **docu_vieware_get_control**
> DocuViewareGetControlResponse docu_vieware_get_control(docu_vieware_get_control_parameters)

Gets the HTML dom of a DocuVieware control.

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
    api_instance = openapi_client.DocuViewareApi(api_client)
    docu_vieware_get_control_parameters = openapi_client.DocuViewareGetControlParameters() # DocuViewareGetControlParameters | A DocuViewareGetControlParameters object specifying the parameters of the action.

    try:
        # Gets the HTML dom of a DocuVieware control.
        api_response = api_instance.docu_vieware_get_control(docu_vieware_get_control_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocuViewareApi->docu_vieware_get_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docu_vieware_get_control_parameters** | [**DocuViewareGetControlParameters**](DocuViewareGetControlParameters.md)| A DocuViewareGetControlParameters object specifying the parameters of the action. | 

### Return type

[**DocuViewareGetControlResponse**](DocuViewareGetControlResponse.md)

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

# **docu_vieware_get_version**
> StringResponse docu_vieware_get_version()

Get the DocuVieware engine version.

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
    api_instance = openapi_client.DocuViewareApi(api_client)
    
    try:
        # Get the DocuVieware engine version.
        api_response = api_instance.docu_vieware_get_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocuViewareApi->docu_vieware_get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **docu_vieware_save**
> DocuViewareSaveResponse docu_vieware_save(docu_vieware_save_parameters)

Saves the document being handled by a specific DocuVieware control, in its current state.

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
    api_instance = openapi_client.DocuViewareApi(api_client)
    docu_vieware_save_parameters = openapi_client.DocuViewareSaveParameters() # DocuViewareSaveParameters | A DocuViewareSaveParameters object specifying the parameters of the action.

    try:
        # Saves the document being handled by a specific DocuVieware control, in its current state.
        api_response = api_instance.docu_vieware_save(docu_vieware_save_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocuViewareApi->docu_vieware_save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docu_vieware_save_parameters** | [**DocuViewareSaveParameters**](DocuViewareSaveParameters.md)| A DocuViewareSaveParameters object specifying the parameters of the action. | 

### Return type

[**DocuViewareSaveResponse**](DocuViewareSaveResponse.md)

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

