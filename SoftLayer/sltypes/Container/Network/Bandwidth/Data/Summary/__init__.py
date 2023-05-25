from SoftLayer.sltypes.Entity import Entity

class Container_Network_Bandwidth_Data_Summary(Entity):
    """SoftLayer_Container_Network_Bandwidth_Data_Summary models an interface's overall bandwidth usage during it's
current billing cycle."""
    allowedUsage: float
    estimatedUsage: float
    projectedUsage: float
    usageUnits: str
