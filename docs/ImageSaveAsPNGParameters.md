# ImageSaveAsPNGParameters

Represents the parameters for a save as PNG action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The identifier of the previously uploaded file to be processed. | 
**page_range** | **str** | Specifies the number of the page, or the range of pages to be saved as PNG. | [optional] [default to '*']
**compression** | **int** | Specifies the level of compression to be used for the PNG output, between 0 (no compression - faster encoding) to 9(max compression - slower encoding). | [optional] [default to 6]
**interlaced** | **bool** | Specifies if the produced PNG image must be interlaced. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


