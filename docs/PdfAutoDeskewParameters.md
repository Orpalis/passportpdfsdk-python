# PdfAutoDeskewParameters

Represents the parameters for an auto deskew action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the page or the page range to be auto-deskewed. | 
**max_angle_of_research** | **float** | Specifies the maximum skew angle to be detected. A value of below 15 is suggested. | [optional] [default to 15]
**optimistic** | **bool** | Specifies whether the skew detection engine must be optimistic when detecting angles.  If you know the image is skewed, you should set this to true. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


