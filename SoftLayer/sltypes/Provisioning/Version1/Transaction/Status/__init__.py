from SoftLayer.sltypes.Entity import Entity

class Provisioning_Version1_Transaction_Status(Entity):
    """The SoftLayer_Provisioning_Version1_Transaction_Status data type contains general information relating to a
single SoftLayer hardware transaction status.   SoftLayer customers are unable to change their hardware
transaction status."""
    averageDuration: float
    friendlyName: str
    name: str
