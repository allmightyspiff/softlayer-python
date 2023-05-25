from SoftLayer.sltypes.Entity import Entity

class Product_Item_Server_Group(Entity):
    """The SoftLayer_Product_Item_Server_Group data type details the type of compute service a
[[SoftLayer_Product_Item (type)|SoftLayer_Product_Item]] or [[SoftLayer_Product_Package_Preset
(type)|SoftLayer_Product_Package_Preset]] belongs to."""
    keyName: str
    name: str
