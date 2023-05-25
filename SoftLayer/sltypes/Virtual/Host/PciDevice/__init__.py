from SoftLayer.sltypes.Entity import Entity

class Virtual_Host_PciDevice(Entity):
    """This type represents a PCI device on a host."""
    id_: int
    uuid: str
    xenPciId: str
