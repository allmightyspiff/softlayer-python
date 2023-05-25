from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Product_Package_Inventory(Entity):
    """This is deprecated."""
    availableInventoryCount: int
    itemId: int
    locationId: int
    modifyDate: datetime
    overstockFlag: int
    packageId: int
