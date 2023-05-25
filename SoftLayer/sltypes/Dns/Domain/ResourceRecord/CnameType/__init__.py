from SoftLayer.sltypes.Dns.Domain.ResourceRecord import Dns_Domain_ResourceRecord
from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord

class Dns_Domain_ResourceRecord_CnameType(Dns_Domain_ResourceRecord):
    """SoftLayer_Dns_Domain_ResourceRecord_CnameType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type''
property is set to "cname" and defines a DNS CNAME record on a SoftLayer hosted domain. A CNAME record
directs a host name to another host. For instance, if the CNAME record for "alias.example.org" points to the
host "host.example.org" then the ''host'' property equals "alias" and the ''data'' property equals
"host.example.org.".   DNS entries defined by CNAME should not be used as the data field for an MX record."""
