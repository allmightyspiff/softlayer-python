from SoftLayer.sltypes.Entity import Entity

class Location_Region_Location(Entity):
    """The SoftLayer_Location_Region_Location is very specific to the location where services will actually be
provisioned. When accessed through a package, this location is the top priority location for a region. All
new servers and services are provisioned at this location. When a server is ordered and a region is selected,
this is the location within that region where the server will actually exist and have software/services
installed."""
    locationId: int
