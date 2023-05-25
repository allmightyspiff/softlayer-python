from SoftLayer.sltypes.Entity import Entity

class Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus(Entity):
    """This data type represents PCI device allocation properties of a [[SoftLayer_Virtual_DedicatedHost]]."""
    deviceCount: int
    deviceName: str
    devicesAllocated: int
    devicesAvailable: int
    hardwareComponentModelGenericId: int
    hostId: int
