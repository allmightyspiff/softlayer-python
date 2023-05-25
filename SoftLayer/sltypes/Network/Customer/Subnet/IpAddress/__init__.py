from SoftLayer.sltypes.Entity import Entity

class Network_Customer_Subnet_IpAddress(Entity):
    """The SoftLayer_Network_Customer_Subnet_IpAddress data type contains general information relating to a single
Customer Subnet (Remote) IPv4 address."""
    id_: int
    ipAddress: str
    notes: str
    subnetId: int
