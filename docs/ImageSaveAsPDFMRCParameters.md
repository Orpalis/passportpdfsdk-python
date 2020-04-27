# ImageSaveAsPDFMRCParameters

Represents the parameters for a save as PDF MRC action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to be saved as PDF MRC. | [optional] [default to '*']
**conformance** | [**PdfConformance**](PdfConformance.md) |  | [optional] 
**color_image_compression** | [**PdfImageCompressionScheme**](PdfImageCompressionScheme.md) |  | [optional] 
**bitonal_image_compression** | [**PdfImageCompressionScheme**](PdfImageCompressionScheme.md) |  | [optional] 
**image_quality** | **int** | Specifies the quality to be used for the compression of the images from the PDF.  Must be in the range [0 (best compression - worst quality) - 100 (worst quality - best compression)]. | [optional] [default to 60]
**downscale_resolution** | **int** | Specifies the resolution for downscaling the background layer, if any. | [optional] [default to 100]
**preserve_smoothing** | **bool** | Specifies whether the MRC engine should try to preserve smoothing between different layers.   Enabling this option should globally enhance the text quality but also reduce the compression rate. | [optional] [default to False]
**fast_web_view** | **bool** | Specifies whether the PDF shall be optimized for online distribution. | [optional] [default to False]
**jbig2_pms_threshold** | **float** | Specifies the threshold value for the JBIG2 encoder pattern matching and substitution between 0 and 1. Any number lower than 1 may lead to lossy compression. | [optional] [default to 0.85]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


