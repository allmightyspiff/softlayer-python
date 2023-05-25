from SoftLayer.sltypes.Dns.Domain.ResourceRecord import Dns_Domain_ResourceRecord
from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord

class Dns_Domain_ResourceRecord_AType(Dns_Domain_ResourceRecord):
    """SoftLayer_Dns_Domain_ResourceRecord_AType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type''
property is set to "a" and defines a DNS A record on a SoftLayer hosted domain. An A record directs a host
name to an IP address. For instance if the A record for "host.example.org" points to the IP address 10.0.0.1
then the ''host'' property for the A record equals "host" and the ''data'' property equals "10.0.0.1"."""
