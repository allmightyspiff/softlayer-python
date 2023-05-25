from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Storage_Group_Partition(Entity):
    """A storage group partition container used for a hardware server order.   This object describes the partitions
for a single storage group that can be added to an order container."""
    isGrow: bool
    name: str
    size: float
