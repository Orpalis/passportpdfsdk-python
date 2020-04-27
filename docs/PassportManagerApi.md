# openapi_client.PassportManagerApi

All URIs are relative to *https://passportpdfapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**passport_manager_get_passport_info**](PassportManagerApi.md#passport_manager_get_passport_info) | **GET** /api/passportmanager/PassportManagerGetPassportInfo | 


# **passport_manager_get_passport_info**
> PassportPDFPassport passport_manager_get_passport_info(passport_id)



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
    api_instance = openapi_client.PassportManagerApi(api_client)
    passport_id = 'passport_id_example' # str | 

    try:
        api_response = api_instance.passport_manager_get_passport_info(passport_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PassportManagerApi->passport_manager_get_passport_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **passport_id** | **str**|  | 

### Return type

[**PassportPDFPassport**](PassportPDFPassport.md)

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

