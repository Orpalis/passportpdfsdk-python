# PdfLoadDocumentFromByteArrayParameters

Represents the parameters for a load document action request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Specifies the data of the document. | 
**file_name** | **str** | Specifies the name of the document. | [optional] 
**password** | **str** | Specifies the password of the document. | [optional] 
**conformance** | [**PdfConformance**](PdfConformance.md) |  | [optional] 
**content_encoding** | [**ContentEncoding**](ContentEncoding.md) |  | [optional] 
**enable_color_detection** | **bool** | Specifies whether color detection must be used while importing a raster format to PDF. | [optional] [default to False]
**get_preview** | **bool** | Specifies whether the response must contain a thumbnail of the first page of the document. | [optional] [default to False]
**thumbnail_width** | **int** | Specifies, in pixels, the width of the thumbnail to be retrieved. Only applicable if GetPreview has been set to true. | [optional] [default to 140]
**thumbnail_height** | **int** | Specifies, in pixels, the height of the thumbnail to be retrieved.  Only applicable if GetPreview has been set to true. | [optional] [default to 220]
**thumbnail_background_color** | **str** | Specifies the background color of the thumbnail, using the color name (ie: \&quot;red\&quot;) or its RGBa code (ie: \&quot;rgba(255,0,0,1)\&quot;).   Only applicable if GetPreview has been set to true. | [optional] [default to 'rgba(0,0,0,0)']
**thumbnail_fit_to_page_size** | **bool** | Specifies if the size of the produced thumbnail is automatically adjusted to don&#39;t have any margin.  Only applicable if GetPreview has been set to true. | [optional] [default to True]
**txt_page_width** | **float** | Specifies the page width, in points, of produced documents from txt files. | [optional] [default to 595]
**txt_page_height** | **float** | Specifies the page height, in points, of produced documents from txt files. | [optional] [default to 842]
**txt_page_margin_left** | **float** | Specifies the page margin left, in points, of produced documents from txt files. | [optional] [default to 10]
**txt_page_margin_top** | **float** | Specifies the page margin top, in points, of produced documents from txt files. | [optional] [default to 10]
**txt_page_margin_right** | **float** | Specifies the page margin right, in points, of produced documents from txt files. | [optional] [default to 10]
**txt_page_margin_bottom** | **float** | Specifies the page margin bottom, in points, of produced documents from txt files. | [optional] [default to 10]
**txt_horizontal_text_alignment** | [**TextAlignment**](TextAlignment.md) |  | [optional] 
**txt_font_size** | **float** | Specifies the text size, in points, to be used for producing documents from txt files. | [optional] [default to 12]
**txt_font_family** | **str** | Specifies the name of the font to be used for producing documents from txt files. | [optional] [default to 'Arial Unicode MS']
**txt_font_bold** | **bool** | Specifies whether the font to be used for producing documents from txt files must have a bold style. | [optional] [default to False]
**txt_font_italic** | **bool** | Specifies whether the font to be used for producing documents from txt files must have an italic style. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


