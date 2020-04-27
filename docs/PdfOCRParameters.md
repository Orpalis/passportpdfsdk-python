# PdfOCRParameters

Represents the parameters for an OCR action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the page or the page range to be processed. | 
**language** | **str** | Specifies the language to be used for the OCR. | [optional] [default to 'eng']
**skip_page_with_text** | **bool** | Specifies if pages containing text must be ignored (in such case no token is charged). | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


