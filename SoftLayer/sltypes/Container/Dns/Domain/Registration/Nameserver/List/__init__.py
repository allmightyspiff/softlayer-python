from SoftLayer.sltypes.Entity import Entity

class Container_Dns_Domain_Registration_Nameserver_List(Entity):
    """Nameservers list container for domain registration"""
    ipv4Address: str
    ipv6Address: str
    name: str
    sortOrder: int
