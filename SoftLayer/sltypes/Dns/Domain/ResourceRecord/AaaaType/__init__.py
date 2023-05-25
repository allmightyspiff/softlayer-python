from SoftLayer.sltypes.Dns.Domain.ResourceRecord import Dns_Domain_ResourceRecord
from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord

class Dns_Domain_ResourceRecord_AaaaType(Dns_Domain_ResourceRecord):
    """SoftLayer_Dns_Domain_ResourceRecord_AaaaType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type''
property is set to "aaaa" and defines a DNS AAAA record on a SoftLayer hosted domain. An AAAA record directs
a host name to an IPv6 address. For instance if the AAAA record for "host.example.org" points to the IPv6
address "fe80:0:0:0:0:0:a00:0" then the ''host'' property for the AAAA record equals "host" and the ''data''
property equals "fe80:0:0:0:0:0:a00:0"."""
