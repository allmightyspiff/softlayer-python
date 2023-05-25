from SoftLayer.sltypes.Dns.Domain import Dns_Domain
from SoftLayer.sltypes.Dns_Domain import Dns_Domain

class Dns_Domain_Reverse(Dns_Domain):
    """The SoftLayer_Dns_Domain_Reverse data type represents a reverse IP address record."""
    networkAddress: str
