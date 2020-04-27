# PdfReduceResponse

Represents the response to a reduce action request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 
**remaining_tokens** | **int** | Specifies the number of remaining tokens. | [optional] 
**error_info** | [**ReduceErrorInfo**](ReduceErrorInfo.md) |  | [optional] 
**warnings_info** | [**list[ReduceWarningInfo]**](ReduceWarningInfo.md) | Specifies the different warnings that occured during the process of the reduce action. | [optional] [readonly] 
**content_removed** | **bool** | Specifies whether content has been removed from the PDF during the process of the reduce action. | [optional] [readonly] 
**version_changed** | **bool** | Specifies whether the version of the PDF has changed during the process of the reduce action. | [optional] [readonly] 
**new_file_size** | **int** | Specify the size of the new created document. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


