# ImageSaveAsPDFParameters

Represents the parameters for a save as PDF action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to be saved as PDF. | [optional] [default to '*']
**conformance** | [**PdfConformance**](PdfConformance.md) |  | [optional] 
**color_image_compression** | [**PdfImageCompressionScheme**](PdfImageCompressionScheme.md) |  | [optional] 
**bitonal_image_compression** | [**PdfImageCompressionScheme**](PdfImageCompressionScheme.md) |  | [optional] 
**enable_color_detection** | **bool** | Specifies is color detection must be used. | [optional] [default to False]
**image_quality** | **int** | Specifies the quality to be used for the compression of the images from the PDF.  Must be in the range [0 (best compression - worst quality) - 100 (worst quality - best compression)]. | [optional] [default to 75]
**downscale_resolution** | **int** | Specifies the resolution for downscaling images, if any. | [optional] [default to 0]
**fast_web_view** | **bool** | Specifies whether the PDF shall be optimized for online distribution. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


