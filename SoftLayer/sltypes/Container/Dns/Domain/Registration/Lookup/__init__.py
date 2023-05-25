from SoftLayer.sltypes.Container.Dns.Domain.Registration.Lookup.Items import Container_Dns_Domain_Registration_Lookup_Items
from SoftLayer.sltypes.Entity import Entity

class Container_Dns_Domain_Registration_Lookup(Entity):
    """Lookup domain container for domain registration"""
    items: list[Container_Dns_Domain_Registration_Lookup_Items]
