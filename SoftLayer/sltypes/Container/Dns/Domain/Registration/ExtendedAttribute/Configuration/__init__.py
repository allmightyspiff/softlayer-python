from SoftLayer.sltypes.Entity import Entity

class Container_Dns_Domain_Registration_ExtendedAttribute_Configuration(Entity):
    """This is the data type that may need to be populated to complete registraton for domains that are country code
TLD's."""
    name: str
    value: str
