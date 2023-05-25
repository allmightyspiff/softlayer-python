from SoftLayer.sltypes.Entity import Entity

class Network_Tunnel_Module_Context_Address_Translation(Entity):
    """The SoftLayer_Network_Tunnel_Module_Context_Address_Translation data type contains general information
relating to a single address translation. Information such as notes, ip addresses, along with record
information, and network tunnel data may be retrieved."""
    customerIpAddress: str
    customerIpAddressId: int
    id_: int
    internalIpAddress: str
    internalIpAddressId: int
    networkTunnelContextId: int
    notes: str
