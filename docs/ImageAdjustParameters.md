# ImageAdjustParameters

Represents the parameters for an image adjustment action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to adjust. | 
**roi_left** | **int** | Specifies the left coordinate, in pixel, of the region to process. | [optional] [default to 0]
**roi_top** | **int** | Specifies the top coordinate, in pixel, of the region to process. | [optional] [default to 0]
**roi_width** | **int** | Specifies the width, in pixel, of the region to process. 0 causes the entire image to be processed. | [optional] [default to 0]
**roi_height** | **int** | Specifies the height, in pixel, of the region to process. 0 causes the entire image to be processed. | [optional] [default to 0]
**gamma_correction** | **int** | Specifies the gamma correction parameter. | [optional] [default to 0]
**brightness** | **int** | Specifies the brightness parameter. | [optional] [default to 0]
**contrast** | **int** | Specifies the contrast parameter. | [optional] [default to 0]
**saturation** | **int** | Specifies the saturation parameter. | [optional] [default to 0]
**auto_contrast_enhancement** | **bool** | Specifies whether the contrast shall be automatically enhanced. | [optional] [default to False]
**contrast_histogram_stretch** | **bool** | Specifies whether a contrast histogram stretch filter shall be performed. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


