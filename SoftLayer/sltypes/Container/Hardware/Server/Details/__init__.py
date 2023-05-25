from SoftLayer.sltypes.Software.Component import Software_Component
from SoftLayer.sltypes.Network.Component import Network_Component
from SoftLayer.sltypes.Hardware.Component import Hardware_Component
from SoftLayer.sltypes.Entity import Entity

class Container_Hardware_Server_Details(Entity):
    """The SoftLayer_Container_Hardware_Server_Details data type contains information relating to a server's
component information, network information, and software information."""
    components: list[Hardware_Component]
    networkComponents: list[Network_Component]
    software: list[Software_Component]
