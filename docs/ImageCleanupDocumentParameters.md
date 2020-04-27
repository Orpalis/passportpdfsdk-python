# ImageCleanupDocumentParameters

Represents the parameters for a cleanup document action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to cleanup. | 
**remove_black_borders** | **bool** | Specifies whether the dark borders of the document image shall be replaced with white content. | [optional] [default to False]
**deskew** | **bool** | Specifies whether the document shall be deskewed. | [optional] [default to False]
**remove_left_margin_punch_holes** | **bool** | Specifies whether punch holes shall be removed from the left margin of the document. | [optional] [default to False]
**remove_top_margin_punch_holes** | **bool** | Specifies whether punch holes shall be removed from the top margin of the document. | [optional] [default to False]
**remove_right_margin_punch_holes** | **bool** | Specifies whether punch holes shall be removed from the right margin of the document. | [optional] [default to False]
**remove_bottom_margin_punch_holes** | **bool** | Specifies whether punch holes shall be removed from the bottom margin of the document. | [optional] [default to False]
**despeckle_strength** | **int** | Specifies the strength of the despeckle filter to be applied on the image. | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


