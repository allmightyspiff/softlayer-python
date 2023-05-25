from SoftLayer.sltypes.Entity import Entity

class Product_Package_Locations(Entity):
    """Most packages are available in many locations. This object describes that availability for each package."""
    deliveryTimeInformation: str
    isAvailable: int
    locationId: int
    packageId: int
