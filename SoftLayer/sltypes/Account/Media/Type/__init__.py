from SoftLayer.sltypes.Entity import Entity

class Account_Media_Type(Entity):
    """The SoftLayer_Account_Media_Type data type contains general information relating to the different types of
media devices that SoftLayer currently supports, as part of the Data Transfer Request Service. Such devices
as USB hard drives and flash drives, as well as optical media such as CD and DVD are currently supported."""
    description: str
    id_: int
    keyName: str
    name: str
