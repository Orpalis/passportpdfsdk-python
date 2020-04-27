# PdfConvertToPDFAParameters

Represents the parameters for a convert to PDF/A action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**conformance** | [**PdfAConformance**](PdfAConformance.md) |  | [optional] 
**allow_vectorization** | **bool** | If set to true, conversion engine will use the page vectorization in case direct conversion is not possible. | [optional] [default to True]
**allow_rasterization** | **bool** | If set to true, conversion engine will use the page rasterization in case direct conversion and verorization are not possible or allowed. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


