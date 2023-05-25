from SoftLayer.sltypes.Dns.Domain.ResourceRecord import Dns_Domain_ResourceRecord
from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord

class Dns_Domain_ResourceRecord_SoaType(Dns_Domain_ResourceRecord):
    """SoftLayer_Dns_Domain_ResourceRecord_SoaType defines a domains' Start of Authority (or SOA) resource record. A
domain's SOA record contains a domain's general and propagation information. Every domain must have one SOA
record, and it is not possible to remove a domain's SOA record.   SOA records typically contain a domain's
serial number, but the SoftLayer API associates a domain's serial number directly with it's
SoftLayer_Dns_Domain record."""
