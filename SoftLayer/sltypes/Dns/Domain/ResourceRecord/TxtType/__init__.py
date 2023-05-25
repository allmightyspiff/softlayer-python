from SoftLayer.sltypes.Dns.Domain.ResourceRecord import Dns_Domain_ResourceRecord
from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord

class Dns_Domain_ResourceRecord_TxtType(Dns_Domain_ResourceRecord):
    """SoftLayer_Dns_Domain_ResourceRecord_TxtType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type''
property is set to "txt" and defines a DNS TXT record on a SoftLayer hosted domain. A TXT record provides a
text description for a host. For instance, if defining the TXT record "My test host" for "host.example.org".
then the ''host'' property equals "host" and the ''data'' property equals "My test host".   TXT records are
commonly used in email verification methods such as Sender Policy Framework."""
