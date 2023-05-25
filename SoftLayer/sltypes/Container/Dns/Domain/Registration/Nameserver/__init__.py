from SoftLayer.sltypes.Container.Dns.Domain.Registration.Nameserver.List import Container_Dns_Domain_Registration_Nameserver_List
from SoftLayer.sltypes.Entity import Entity

class Container_Dns_Domain_Registration_Nameserver(Entity):
    """Nameserver container for domain registration"""
    nameservers: list[Container_Dns_Domain_Registration_Nameserver_List]
