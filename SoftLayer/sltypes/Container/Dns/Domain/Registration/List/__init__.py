from SoftLayer.sltypes.Container.Dns.Domain.Registration.ExtendedAttribute.Configuration import Container_Dns_Domain_Registration_ExtendedAttribute_Configuration
from SoftLayer.sltypes.Entity import Entity

class Container_Dns_Domain_Registration_List(Entity):
    domainName: str
    encodingType: str
    extendedAttributeConfiguration: list[Container_Dns_Domain_Registration_ExtendedAttribute_Configuration]
    registrationPeriod: int
