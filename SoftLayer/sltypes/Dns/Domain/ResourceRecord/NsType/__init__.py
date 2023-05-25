from SoftLayer.sltypes.Dns.Domain.ResourceRecord import Dns_Domain_ResourceRecord
from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord

class Dns_Domain_ResourceRecord_NsType(Dns_Domain_ResourceRecord):
    """SoftLayer_Dns_Domain_ResourceRecord_NsType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type''
property is set to "ns" and defines a DNS NS record on a SoftLayer hosted domain. An NS record defines the
authoritative name server for a domain. All SoftLayer hosted domains contain NS records for
"ns1.softlayer.com" and "ns2.softlayer.com" . For instance, if example.org is hosted on ns1.softlayer.com,
then example.org contains an NS record whose ''host'' property equals "@" and whose ''data'' property equals
"ns1.example.org".   NS resource records pointing to ns1.softlayer.com or ns2.softlayer.com many not be
removed from a SoftLayer hosted domain."""
