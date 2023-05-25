from SoftLayer.sltypes.Dns.Domain.ResourceRecord.TxtType import Dns_Domain_ResourceRecord_TxtType
from SoftLayer.sltypes.Dns_Domain_ResourceRecord_TxtType import Dns_Domain_ResourceRecord_TxtType

class Dns_Domain_ResourceRecord_SpfType(Dns_Domain_ResourceRecord_TxtType):
    """SoftLayer_Dns_Domain_ResourceRecord_SpfType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type''
property is set to "spf" and defines a DNS SPF record on a SoftLayer hosted domain. An SPF record provides
sender policy framework data for a host. For instance, if defining the SPF record "v=spf1 mx:mail.example.org
~all" for "host.example.org". then the ''host'' property equals "host" and the ''data'' property equals
"v=spf1 mx:mail.example.org ~all".   SPF records are commonly used in email verification methods such as
Sender Policy Framework."""
