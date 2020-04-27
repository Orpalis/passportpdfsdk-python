# PdfSaveAsPNGParameters

Represents the parameters for a save as PNG acion.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to be saved as PNG. | [optional] [default to '*']
**compression** | **int** | Specifies the level of compression to be used for the PNG output, between 0 (no compression - faster encoding) to 9(max compression - slower encoding). | [optional] [default to 6]
**interlaced** | **bool** | Specifies if the produced PNG image must be interlaced. | [optional] [default to False]
**resolution** | **float** | Specifies the resolution to be used for the rendition process. | [optional] [default to 200]
**render_form_fields** | **bool** | Specifies whether the form fields of the PDF shall be rendered. | [optional] [default to False]
**keep_raster_pdf_resolution** | **bool** | Specifies if the initial image resolution must be kept in case of raster-pdf processing. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


