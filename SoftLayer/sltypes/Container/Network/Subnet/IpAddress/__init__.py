from SoftLayer.sltypes.Hardware import Hardware
from SoftLayer.sltypes.Entity import Entity

class Container_Network_Subnet_IpAddress(Entity):
    """SoftLayer_Container_Subnet_IPAddress models an IP v4 address as it exists as a member of it's subnet, letting
the user know if it is a network identifier, gateway, broadcast, or useable address. Addresses that are
neither the network identifier nor the gateway nor the broadcast addresses are usable by SoftLayer servers."""
    hardware: Hardware
    ipAddress: str
    isBroadcastAddress: bool
    isGatewayAddress: bool
    isNetworkAddress: bool
