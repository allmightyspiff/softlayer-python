from SoftLayer.sltypes.Container.Hardware.Pool.Details.Router import Container_Hardware_Pool_Details_Router
from SoftLayer.sltypes.Entity import Entity

class Container_Hardware_Pool_Details(Entity):
    pendingOrders: int
    pendingTransactions: int
    poolDescription: str
    poolKeyName: str
    poolName: str
    routers: list[Container_Hardware_Pool_Details_Router]
    totalHardware: int
    totalInventoryHardware: int
    totalProvisionedHardware: int
    totalTestedHardware: int
    totalTestingHardware: int
