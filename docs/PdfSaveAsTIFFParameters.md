# PdfSaveAsTIFFParameters

Represents the parameters for a save as TIFF action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to be saved as TIFF. | [optional] [default to '*']
**compression** | [**TiffSaveCompression**](TiffSaveCompression.md) |  | [optional] 
**jpeg_quality** | **int** | Specifies the level of quality to be used if JPEG compression is used, from 1 (poorest) to 100 (greatest). | [optional] [default to 75]
**use_cmyk** | **bool** | Specifies whether the TIFF shall be saved in CMYK color space or not. | [optional] [default to False]
**resolution** | **float** | Specifies the resolution to be used for the rendition process. | [optional] [default to 200]
**render_form_fields** | **bool** | Specifies whether the form fields of the PDF shall be rendered. | [optional] [default to False]
**keep_raster_pdf_resolution** | **bool** | Specifies whether the initial image resolution must be kept in case of raster-pdf processing. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


