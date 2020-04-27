# PdfExtractTextParameters

Represents the parameters for an extract text action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to extract text from. | 
**text_extraction_mode** | [**PdfExtractTextMode**](PdfExtractTextMode.md) |  | [optional] 
**text_extraction_area_left** | **float** | Specifies the left coordinate of the text extraction area for the PageAreaFormated extract mode. | [optional] [default to 0]
**text_extraction_area_top** | **float** | Specifies the top coordinate of the text extraction area for the PageAreaFormated extract mode. | [optional] [default to 0]
**text_extraction_area_width** | **float** | Specifies the width of the text extraction area for the PageAreaFormated extract mode. | [optional] [default to 0]
**text_extraction_area_height** | **float** | Specifies the height of the text extraction area for the PageAreaFormated extract mode. | [optional] [default to 0]
**include_header** | **bool** | Specifies whether the CSV output should include header information. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


