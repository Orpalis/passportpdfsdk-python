# GetDocumentPreviewParameters

Represents the parameters for a get document preview action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | Specifies the identifier of the file to be previewed. | 
**thumbnail_width** | **int** | Specifies, in pixels, the width of the thumbnail to be retrieved. | [optional] [default to 140]
**thumbnail_height** | **int** | Specifies, in pixels, the height of the thumbnail to be retrieved. | [optional] [default to 220]
**thumbnail_background_color** | **str** | Specifies the background color of the thumbnail, using the color name (ie: \&quot;red\&quot;) or its RGBa code (ie: \&quot;rgba(255,0,0,1)\&quot;). | [optional] [default to 'rgba(0,0,0,0)']
**thumbnail_fit_to_page_size** | **bool** | Specifies if the size of the produced thumbnail is automatically adjusted to don&#39;t have any margin. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


