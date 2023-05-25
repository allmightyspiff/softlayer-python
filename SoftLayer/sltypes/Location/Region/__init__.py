from SoftLayer.sltypes.Entity import Entity

class Location_Region(Entity):
    """A region is made up of a keyname and a description of that region. A region keyname can be used as part of an
order. Check the SoftLayer_Product_Order service for more details."""
    description: str
    keyname: str
    sortOrder: int
