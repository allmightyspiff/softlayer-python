from SoftLayer.sltypes.Container.Dns.Domain.Registration.ExtendedAttribute.Option.Require import Container_Dns_Domain_Registration_ExtendedAttribute_Option_Require
from SoftLayer.sltypes.Entity import Entity

class Container_Dns_Domain_Registration_ExtendedAttribute_Option(Entity):
    """This container data type contains extended attribute options information for a domain of country code TLD."""
    description: str
    requireExtendedAttributes: list[Container_Dns_Domain_Registration_ExtendedAttribute_Option_Require]
    title: str
    value: str
