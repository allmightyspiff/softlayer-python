from SoftLayer.sltypes.Dns.Domain import Dns_Domain
from SoftLayer.sltypes.Dns_Domain import Dns_Domain

class Dns_Domain_Forward(Dns_Domain):
    """The SoftLayer_Dns_Domain_Forward data type represents a single DNS domain record hosted on the SoftLayer
nameservers. Domains contain general information about the domain name such as name and serial. Individual
records such as A, AAAA, CTYPE, and MX records are stored in the domain's associated
[[SoftLayer_Dns_Domain_ResourceRecord (type)|SoftLayer_Dns_Domain_ResourceRecord]] records."""
