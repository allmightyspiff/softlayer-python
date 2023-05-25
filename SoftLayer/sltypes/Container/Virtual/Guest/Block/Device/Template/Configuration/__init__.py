from SoftLayer.sltypes.Entity import Entity

class Container_Virtual_Guest_Block_Device_Template_Configuration(Entity):
    """The SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration data type contains information
relating to a template's external location for importing and exporting"""
    bootMode: str
    byol: bool
    cloudInit: bool
    crkCrn: str
    environmentType: list[str]
    ibmAccessKey: str
    ibmApiKey: str
    ibmSecretKey: str
    isEncrypted: bool
    name: str
    note: str
    operatingSystemReferenceCode: str
    rootKeyId: str
    supportedBootModes: list[str]
    uri: str
    wrappedDek: str
