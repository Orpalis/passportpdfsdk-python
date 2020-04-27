# BarcodeInfo

Represents information about a read barcode.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BarcodeType**](BarcodeType.md) |  | [optional] 
**barcode1_d_symbology** | [**Barcode1DSymbology**](Barcode1DSymbology.md) |  | [optional] 
**data** | **str** | Specifies the data contained within the barcode. | [optional] [readonly] 
**x1** | **int** | Specifies the horizontal top-left position of the barcode, in pixels. | [optional] [readonly] 
**x2** | **int** | Specifies the horizontal top-right position of the barcode, in pixels. | [optional] [readonly] 
**x3** | **int** | Specifies the horizontal bottom-left position of the barcode, in pixels. | [optional] [readonly] 
**x4** | **int** | Specifies the horizontal bottom-right position of the barcode, in pixels. | [optional] [readonly] 
**y1** | **int** | Specifies the vertical top-left position of the barcode, in pixels. | [optional] [readonly] 
**y2** | **int** | Specifies the vertical top-right position of the barcode, in pixels. | [optional] [readonly] 
**y3** | **int** | Specifies the vertical bottom-left position of the barcode, in pixels. | [optional] [readonly] 
**y4** | **int** | Specifies the vertical bottom-right position of the barcode, in pixels. | [optional] [readonly] 
**bbox_left_inches** | **float** | Specifies the left coordinates of the bounding box of the barcode, in inches. | [optional] [readonly] 
**bbox_top_inches** | **float** | Specifies the top coordinates of the bounding box of the barcode, in inches. | [optional] [readonly] 
**bbox_width_inches** | **float** | Specifies the width of the bounding box of the barcode, in inches. | [optional] [readonly] 
**bbox_height_inches** | **float** | Specifies the height of the bounding box of the barcode, in inches. | [optional] [readonly] 
**page_number** | **int** | Specifies the number of the page on which the barcode was read. | [optional] [readonly] 
**page_pixel_width** | **int** | Specifies the width, in pixels, of the page where the barcode has been decoded. | [optional] [readonly] 
**page_pixel_height** | **int** | Specifies the height, in pixels, of the page where the barcode has been decoded. | [optional] [readonly] 
**page_horizontal_resolution** | **float** | Specifies the horizontal resolution, in pixel per inches, of the page where the barcode has been decoded. | [optional] [readonly] 
**page_vertical_resolution** | **float** | Specifies the vertical resolution, in pixel per inches, of the page where the barcode has been decoded. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


