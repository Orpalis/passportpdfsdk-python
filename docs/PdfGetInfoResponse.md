# PdfGetInfoResponse

Represents the response to a get info action request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 
**remaining_tokens** | **int** | Specifies the number of remaining tokens. | [optional] 
**page_count** | **int** | Specifies the number of pages of the PDF. | [optional] [readonly] 
**version** | **str** | Specifies the version of the PDF. | [optional] [readonly] 
**author** | **str** | Specifies the author name specified within the PDF, if any. | [optional] [readonly] 
**title** | **str** | Specifies the document title specified within the PDF, if any. | [optional] [readonly] 
**subject** | **str** | Specifies the document subject specified within the PDF, if any. | [optional] [readonly] 
**producer** | **str** | Specifies the producer name specified within the PDF, if any. | [optional] [readonly] 
**metadata** | **str** | Specifies the metadata contained within the PDF, if any. | [optional] [readonly] 
**keywords** | **str** | Specifies the keywords associated with the PDF, if any. | [optional] [readonly] 
**has_user_password** | **bool** | Specifies if the PDF is protected with a user password. | [optional] [readonly] 
**has_owner_password** | **bool** | Specifies if the PDF is protected with a owner password. | [optional] [readonly] 
**encryption** | [**EncryptionAlgorithm**](EncryptionAlgorithm.md) |  | [optional] 
**can_print** | **bool** | Specifies if the user is allowed to print the document, but possibly not at the highest quality level. | [optional] [readonly] 
**can_copy** | **bool** | Specifies if the user is allowed to copy or extract text and graphics from the document. | [optional] [readonly] 
**can_modify** | **bool** | Specifies if the user is allowed to modify the document. | [optional] [readonly] 
**can_add_notes** | **bool** | Specifies if the user is allowed to add annotations. | [optional] [readonly] 
**can_fill_fields** | **bool** | Specifies if the user is allowed to fill-in form fields. | [optional] [readonly] 
**can_copy_access** | **bool** | Specifies if the user is allowed for copying or extracting for use with accessibility features. | [optional] [readonly] 
**can_assemble** | **bool** | Specifies if the user is allowed to assemble the document. | [optional] [readonly] 
**can_print_full** | **bool** | Specifies if the user is allowed to print the document with high resolution. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


