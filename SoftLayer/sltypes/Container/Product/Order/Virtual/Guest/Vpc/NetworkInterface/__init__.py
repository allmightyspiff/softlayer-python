from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Virtual_Guest_Vpc_NetworkInterface(Entity):
    cidr: str
    dns: list[str]
    gateway: str
    interfaceId: str
    ipAddress: str
    ipAllocationId: str
    securityGroupIds: list[int]
    subnetId: str
    vpcId: str
