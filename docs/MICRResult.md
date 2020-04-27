# MICRResult

Represents the result of a MICR operation run on a document given page.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** | Specifies the number of the page on which the symbols have been detected. | [optional] 
**data** | **str** | The detected data. | [optional] 
**detected_symbols** | [**list[MICRSymbolInfo]**](MICRSymbolInfo.md) | Holds detailed information about every single symbol which has been detected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


