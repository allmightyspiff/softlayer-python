from SoftLayer.sltypes.Entity import Entity

class Network_SecurityGroup_OrderBinding(Entity):
    """The SoftLayer_Network_SecurityGroup_OrderBinding data type contains links between security groups and product
orders."""
    guestId: int
    id_: int
    orderId: int
    securityGroupId: int
