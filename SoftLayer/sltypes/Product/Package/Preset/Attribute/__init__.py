from SoftLayer.sltypes.Entity import Entity

class Product_Package_Preset_Attribute(Entity):
    """Package preset attributes contain supplementary information for a package preset."""
    attributeTypeId: int
    id_: int
    presetId: int
    value: str
