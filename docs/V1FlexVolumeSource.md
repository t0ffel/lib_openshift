# V1FlexVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | Driver is the name of the driver to use for this volume. | 
**fs_type** | **str** | Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. The default filesystem depends on FlexVolume script. | [optional] 
**secret_ref** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | Optional: SecretRef is reference to the authentication secret for User, default is empty. | [optional] 
**read_only** | **bool** | Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**options** | **object** | Optional: Extra command options if any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


