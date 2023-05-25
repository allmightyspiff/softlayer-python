from SoftLayer.sltypes.Entity import Entity

class Configuration_Storage_Group_Order(Entity):
    """Single storage group(array) used for a hardware server order.   If a raid configuration is required this
object will describe a single array that will be configured on the server. If the server requires more than
one array, a storage group will need to be created for each array."""
    arrayNumber: int
    arraySize: float
    arrayTypeId: int
    billingOrderItemId: int
    controller: int
    hardDrives: list[str]
    hotSpareDrives: list[int]
    lvmFlag: bool
    partitionData: str
