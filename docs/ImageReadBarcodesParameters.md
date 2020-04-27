# ImageReadBarcodesParameters

Represents the parameters for a read barcode action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to read the barcodes from. | 
**roi_left** | **int** | Specifies the left coordinate, in pixel, of the region to process. | [optional] [default to 0]
**roi_top** | **int** | Specifies the top coordinate, in pixel, of the region to process. | [optional] [default to 0]
**roi_width** | **int** | Specifies the width, in pixel, of the region to process. 0 causes the entire image to be processed. | [optional] [default to 0]
**roi_height** | **int** | Specifies the height, in pixel, of the region to process. 0 causes the entire image to be processed. | [optional] [default to 0]
**scan_mode** | [**ScanMode**](ScanMode.md) |  | [optional] 
**scan_barcode1_d** | **bool** | Specifies whether the barcodes of type 1D shall be read. | [optional] [default to True]
**scan_barcode_qr** | **bool** | Specifies whether the barcodes of type QR shall be read. | [optional] [default to True]
**scan_barcode_micro_qr** | **bool** | Specifies whether the barcodes of type Micro QR shall be read. | [optional] [default to True]
**scan_barcode_pdf417** | **bool** | Specifies whether the barcodes of type PDF 147 shall be read. | [optional] [default to True]
**scan_barcode_data_matrix** | **bool** | Specifies whether the barcodes of type Data Matrix shall be read. | [optional] [default to True]
**scan_barcode_aztec** | **bool** | Specifies whether the barcodes of type Aztec shall be read. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


