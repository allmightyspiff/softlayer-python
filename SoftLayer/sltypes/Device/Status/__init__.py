from SoftLayer.sltypes.Entity import Entity

class Device_Status(Entity):
    """SoftLayer_Device_Status is used to indicate the current status of a device"""
    id_: int
    keyName: str
    name: str
