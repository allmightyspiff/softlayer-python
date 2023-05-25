from SoftLayer.sltypes.Container.Dns.Domain.Registration.ExtendedAttribute.Option import Container_Dns_Domain_Registration_ExtendedAttribute_Option
from SoftLayer.sltypes.Entity import Entity

class Container_Dns_Domain_Registration_ExtendedAttribute(Entity):
    """This container data type contains extended attributes information for a domain of country code TLD."""
    childFlag: bool
    description: str
    name: str
    options: list[Container_Dns_Domain_Registration_ExtendedAttribute_Option]
    requiredFlag: int
    userDefinedFlag: bool
