# PdfRotatePageStandardParameters

Represents the parameters for a rotate page standard action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to be rotated.  You can specify different page rotations using such pattern: Page Range &#x3D; \&quot;M:1:90;2:270\&quot;. In this example, a rotation of 90 degrees will be applied to the page 1 and 270 degrees to the page 2. | 
**rotation_angle** | **int** | Specifies the rotation angle, clockwise in degrees, which can be either positive and negative and any multiple of 90.  Use 0 in case of special pattern usage for the PageRange property. | 
**flip_horizontally** | **bool** | Specifies whether the page(s) shall be flipped horizontally.  This parameter is ignored if PageRange start with \&quot;M:\&quot;. | [optional] [default to False]
**flip_vertically** | **bool** | Specifies whether the page(s) shall be flipped vertically.  This parameter is ignored if PageRange start with \&quot;M:\&quot;. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


