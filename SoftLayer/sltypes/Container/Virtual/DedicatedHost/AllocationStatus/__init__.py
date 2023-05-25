from SoftLayer.sltypes.Entity import Entity

class Container_Virtual_DedicatedHost_AllocationStatus(Entity):
    """This data type represents the structure to hold the allocation properties of a
[[SoftLayer_Virtual_DedicatedHost]]."""
    cpuAllocated: int
    cpuAvailable: int
    cpuCount: int
    diskAllocated: int
    diskAvailable: int
    diskCapacity: int
    guestCount: int
    memoryAllocated: int
    memoryAvailable: int
    memoryCapacity: int
