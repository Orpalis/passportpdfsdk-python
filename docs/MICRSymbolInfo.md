# MICRSymbolInfo

Holds detailed information about a magnetic ink symbol detected by a MICR process.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol_value** | **str** | Specifies the best candidate for the character representation of the detected symbol. | [optional] 
**symbol_value2** | **str** | Specifies the second best candidate for the character representation of the detected symbol. | [optional] 
**top** | **int** | Specifies the top coordinate of the symbol, in pixels. | [optional] 
**left** | **int** | Specifies the left coordinate of the symbol, in pixels. | [optional] 
**bottom** | **int** | Specifies the bottom coordinate of the symbol, in pixels. | [optional] 
**right** | **int** | Specifies the right coordinate of the symbol, in pixels. | [optional] 
**line** | **int** | Specifies the number of the line on which the symbol has been detected. | [optional] 
**confidence** | **float** | Specifies the level of confidence of the best detected symbol candidate. | [optional] 
**confidence2** | **float** | Specifies the level of confidence of the second best detected symbol candidate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


