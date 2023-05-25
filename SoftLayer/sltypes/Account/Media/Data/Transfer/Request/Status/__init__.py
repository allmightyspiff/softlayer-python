from SoftLayer.sltypes.Entity import Entity

class Account_Media_Data_Transfer_Request_Status(Entity):
    """The SoftLayer_Account_Media_Data_Transfer_Request_Status data type contains general information relating to
the statuses to which a Data Transfer Request may be set."""
    description: str
    id_: int
    keyName: str
    name: str
