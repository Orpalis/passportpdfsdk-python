# ImageSaveAsTIFFParameters

Represents the parameters for a save as TIFF action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to be saved as TIFF. | [optional] [default to '*']
**compression** | [**TiffSaveCompression**](TiffSaveCompression.md) |  | [optional] 
**jpeg_quality** | **int** | Specifies the level of quality to be used if JPEG compression is used, from 1 (poorest) to 100 (greatest). | [optional] [default to 75]
**use_cmyk** | **bool** | Specifies whether the TIFF shall be saved in CMYK color space or not. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


