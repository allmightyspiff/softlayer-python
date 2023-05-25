from SoftLayer.sltypes.Entity import Entity

class Auxiliary_Shipping_Courier(Entity):
    """The SoftLayer_Auxiliary_Shipping_Courier data type contains general information relating the different
(major) couriers that SoftLayer may use for shipping."""
    id_: int
    keyName: str
    name: str
    url: str
