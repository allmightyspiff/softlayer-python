from SoftLayer.sltypes.Product.Item.Price import Product_Item_Price
from SoftLayer.sltypes.Hardware.Component import Hardware_Component
from SoftLayer.sltypes.Entity import Entity

class Container_Hardware_Server_Configuration(Entity):
    """The SoftLayer_Container_Hardware_Server_Configuration data type contains information relating to a server's
item price information, and hard drive partition information."""
    addToSparePoolAfterOsReload: int
    customProvisionScriptUri: str
    driveRetentionFlag: bool
    eraseHardDrives: int
    hardDrives: list[Hardware_Component]
    imageTemplateId: int
    inPlaceFlag: bool
    itemPrices: list[Product_Item_Price]
    lvmFlag: int
    resetIpmiPassword: int
    serviceToken: str
    sshKeyIds: list[int]
    upgradeBios: int
    upgradeHardDriveFirmware: int
