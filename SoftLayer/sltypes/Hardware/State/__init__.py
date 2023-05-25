from SoftLayer.sltypes.Entity import Entity

class Hardware_State(Entity):
    """The SoftLayer_Hardware_State type contains general information about the current state of it's associated
hardware, including the current power state (i.e. Running or Stopped), and it's current transitioning state
(e.g. Provisioning, Reloading)."""
    deviceStatusId: int
    hardwareId: int
    id_: int
