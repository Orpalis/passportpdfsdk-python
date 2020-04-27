# PdfSplitParameters

Represents the parameters for a split action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**split_method** | [**PdfSplitMethod**](PdfSplitMethod.md) |  | 
**split_value** | **int** | Specifies, respectively for the SplitByPageCount and SplitByFileSize split methods, the number of pages or the maximum size, in kilobytes, of the produced files. | 
**immediate_download** | **bool** | Specifies whether the file(s) created as a result of the action shall be available for immediate download. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


