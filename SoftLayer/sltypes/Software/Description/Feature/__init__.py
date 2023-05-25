from SoftLayer.sltypes.Entity import Entity

class Software_Description_Feature(Entity):
    """The SoftLayer_Software_Description_Feature data type represents a single software description feature. A
feature may show up on more than one software description and can not be created, modified, or removed."""
    id_: int
    keyName: str
    name: str
    vendor: str
