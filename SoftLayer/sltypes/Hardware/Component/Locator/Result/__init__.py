from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Locator_Result(Entity):
    """This object holds a generic component model id and the list of datacenter names where it is available."""
    datacenters: list[str]
    genericComponentModelId: int
    serverPackageId: int
