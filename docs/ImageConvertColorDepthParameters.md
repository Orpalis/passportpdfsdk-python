# ImageConvertColorDepthParameters

Represents the parameters for an image color depth change action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to process. | 
**convert_color_depth_mode** | [**ColorDepthConversionMethod**](ColorDepthConversionMethod.md) |  | 
**depth1_bpp_otsu_threshold** | **int** | Specifies the threshold for a conversion using the Depth1BppOtsu method. | [optional] [default to 50]
**depth1_bpp_bradley_threshold** | **int** | Specifies the threshold for a conversion using the Depth1BppBradley method. | [optional] [default to 38]
**depth1_bpp_sauvola_factor** | **float** | Specifies the factor for a conversion using the Depth1BppSauvola method. | [optional] [default to 0.35]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


