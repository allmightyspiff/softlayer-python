from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_RemoteManagement_Command(Entity):
    """The SoftLayer_Network_Storage_Evault_Version6 contains the names of the remote management commands.
Currently, only the reboot and power commands for the remote management card exist."""
    keyName: str
