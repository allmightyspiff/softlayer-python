from SoftLayer.sltypes.Entity import Entity

class Container_Hardware_Pool_Details_Router(Entity):
    poolThreshold: int
    routerId: int
    routerName: str
    totalHardware: int
    totalInventoryHardware: int
    totalProvisionedHardware: int
    totalTestedHardware: int
    totalTestingHardware: int
