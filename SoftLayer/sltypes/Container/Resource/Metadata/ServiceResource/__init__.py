from SoftLayer.sltypes.Network.Service.Resource.Type import Network_Service_Resource_Type
from SoftLayer.sltypes.Entity import Entity

class Container_Resource_Metadata_ServiceResource(Entity):
    """The metadata service resource container is used to store information about a single service resource."""
    backendIpAddress: str
    type_: Network_Service_Resource_Type
