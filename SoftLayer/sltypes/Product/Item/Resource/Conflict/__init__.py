from SoftLayer.sltypes.Entity import Entity

class Product_Item_Resource_Conflict(Entity):
    itemId: int
    message: str
    packageId: int
    resourceTableId: int
