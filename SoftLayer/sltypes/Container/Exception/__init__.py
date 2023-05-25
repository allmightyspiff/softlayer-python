from SoftLayer.sltypes.Entity import Entity

class Container_Exception(Entity):
    """The SoftLayer_Container_Exception data type represents a SoftLayer_Exception."""
    exceptionClass: str
    exceptionMessage: str
