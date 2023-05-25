from SoftLayer.sltypes.Container.Product.Order.Storage.Group.Partition import Container_Product_Order_Storage_Group_Partition
from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Storage_Group(Entity):
    """A single storage group container used for a hardware server order.   This object describes a single storage
group that can be added to an order container."""
    arraySize: float
    arrayTypeId: int
    diskControllerIndex: int
    hardDriveCategoryCodes: list[str]
    hardDrives: list[int]
    hotSpareDrives: list[int]
    lvmFlag: bool
    partitionTemplateId: int
    partitions: list[Container_Product_Order_Storage_Group_Partition]
