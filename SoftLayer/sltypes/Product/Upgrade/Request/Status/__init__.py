from SoftLayer.sltypes.Entity import Entity

class Product_Upgrade_Request_Status(Entity):
    """The SoftLayer_Product_Upgrade_Request_Status data type contains detailed information relating to an hardware
or software upgrade request."""
    description: str
    id_: int
    name: str
    statusCode: str
