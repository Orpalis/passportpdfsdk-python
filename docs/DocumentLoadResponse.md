# DocumentLoadResponse

Represents the response to a document loading action request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 
**remaining_tokens** | **int** | Specifies the number of remaining tokens. | [optional] 
**file_id** | **str** | Specifies the file identifier of the loaded document. | [optional] [readonly] 
**document_format** | [**DocumentFormat**](DocumentFormat.md) |  | [optional] 
**page_count** | **int** | Specifies the number of pages into the loaded document. | [optional] [readonly] 
**thumbnail_data** | **str** | Specifies the data of a thumbnail from the first page of the document, in PNG format. Only applicable if the GetPreview field of the request has been set to true. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


