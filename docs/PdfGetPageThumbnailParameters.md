# PdfGetPageThumbnailParameters

Represents the parameters for a get page thumbnail action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the page or the range of pages to get a thumbnail from. | 
**thumbnail_width** | **int** | Specifies the width, in points, of the thumbnail(s). | [optional] [default to 140]
**thumbnail_height** | **int** | Specifies the height, in points, of the thumbnail(s). | [optional] [default to 220]
**background_color** | **str** | Specifies the background color of the thumbnail(s), using the color name (ie: \&quot;red\&quot;) or its RGBa code (ie: \&quot;rgba(255,0,0,1)\&quot;). | [optional] [default to 'rgba(0,0,0,0)']
**thumbnail_fit_to_page_size** | **bool** | Specifies if the size of the produced thumbnail is automatically adjusted to don&#39;t have any margin. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


