from SoftLayer.sltypes.Container.Collection.Locale.StateCode import Container_Collection_Locale_StateCode
from SoftLayer.sltypes.Entity import Entity

class Container_Collection_Locale_CountryCode(Entity):
    """This container is used to hold country locale information."""
    longName: str
    shortName: str
    stateCodes: list[Container_Collection_Locale_StateCode]
