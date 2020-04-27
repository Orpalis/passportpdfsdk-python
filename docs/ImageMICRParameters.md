# ImageMICRParameters

Represents the parameters for a MICR action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the page or the range of page to be processed. | 
**font** | [**MicrFont**](MicrFont.md) |  | 
**context** | [**MicrContext**](MicrContext.md) |  | 
**white_list** | **str** | Specifies the characters to be ignored by the recognition process. | [optional] [default to '']
**roi_left** | **int** | Specifies the left coordinate, in pixel, of the region to process. | [optional] [default to 0]
**roi_top** | **int** | Specifies the top coordinate, in pixel, of the region to process. | [optional] [default to 0]
**roi_width** | **int** | Specifies the width, in pixel, of the region to process. 0 causes the entire image to be processed. | [optional] [default to 0]
**roi_height** | **int** | Specifies the height, in pixel, of the region to process. 0 causes the entire image to be processed. | [optional] [default to 0]
**expected_symbols_count** | **int** | Specifies the number of symbols expected to be detected, use 0 if unknown. | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


