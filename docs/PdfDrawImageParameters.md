# PdfDrawImageParameters

Represents the parameters for a draw image action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the page or the page range on which the image shall be drawn. | 
**image_data** | **str** | Specifies the data of the image to be drawn. | [optional] 
**image_file_id** | **str** | Specifies the file ID of the image to be drawn. | [optional] [default to '']
**quality** | **int** | Specifies the level of quality to be used for the compression, from 1 (poorest) to 100 (greatest). | [optional] [default to 75]
**color_image_compression** | [**PdfImageCompressionScheme**](PdfImageCompressionScheme.md) |  | [optional] 
**bitonal_compression** | [**PdfImageCompressionScheme**](PdfImageCompressionScheme.md) |  | [optional] 
**image_layout** | [**DrawableContentLayoutParameters**](DrawableContentLayoutParameters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


