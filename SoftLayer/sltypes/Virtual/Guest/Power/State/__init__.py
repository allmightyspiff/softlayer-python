from SoftLayer.sltypes.Entity import Entity

class Virtual_Guest_Power_State(Entity):
    """The power state class provides a common set of values for which a guest's power state will be presented in
the SoftLayer API."""
    description: str
    keyName: str
    name: str
