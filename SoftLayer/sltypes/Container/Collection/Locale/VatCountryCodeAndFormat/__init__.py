from SoftLayer.sltypes.Entity import Entity

class Container_Collection_Locale_VatCountryCodeAndFormat(Entity):
    """This container is used to hold VAT information."""
    countryCode: str
    regex: str
