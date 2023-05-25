from SoftLayer.sltypes.Container.Dns.Domain.Registration.Nameserver import Container_Dns_Domain_Registration_Nameserver
from datetime import datetime
from SoftLayer.sltypes.Container.Dns.Domain.Registration.Contact import Container_Dns_Domain_Registration_Contact
from SoftLayer.sltypes.Entity import Entity

class Container_Dns_Domain_Registration_Information(Entity):
    """Information container for domain registration"""
    contacts: list[Container_Dns_Domain_Registration_Contact]
    expireDate: datetime
    nameservers: list[Container_Dns_Domain_Registration_Nameserver]
    registryCreateDate: datetime
    registryExpireDate: datetime
    registryUpdateDate: datetime
