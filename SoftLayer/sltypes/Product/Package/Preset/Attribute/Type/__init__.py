from SoftLayer.sltypes.Entity import Entity

class Product_Package_Preset_Attribute_Type(Entity):
    """SoftLayer_Product_Package_Preset_Attribute_Type models the type of attribute that can be assigned to a
package preset."""
    description: str
    id_: int
    keyName: str
    name: str
