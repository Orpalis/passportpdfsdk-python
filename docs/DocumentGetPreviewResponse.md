# DocumentGetPreviewResponse

Represents the response to a get document preview action request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 
**remaining_tokens** | **int** | Specifies the number of remaining tokens. | [optional] 
**page_count** | **int** | Specifies the page count of the document. | [optional] [readonly] 
**thumbnail_data** | **str** | Specifies the data of a thumbnail from the first page of the document, in PNG format. | [optional] [readonly] 
**document_format** | [**DocumentFormat**](DocumentFormat.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


