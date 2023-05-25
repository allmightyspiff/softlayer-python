from SoftLayer.sltypes.Network.Vlan import Network_Vlan
from SoftLayer.sltypes.Virtual.Guest import Virtual_Guest
from SoftLayer.sltypes.Network.Subnet import Network_Subnet
from SoftLayer.sltypes.Network.Storage import Network_Storage
from SoftLayer.sltypes.Workload.Citrix.Deployment.Resource.Role import Workload_Citrix_Deployment_Resource_Role
from SoftLayer.sltypes.Hardware import Hardware
from SoftLayer.sltypes.Entity import Entity

class Workload_Citrix_Deployment_Resource_Response(Entity):
    """The SoftLayer_Workload_Citrix_Deployment_Resource_Response constructs a response object for
[[SoftLayer_Workload_Citrix_Deployment_Resource_Response]] for the CVAD resource."""
    hardware: Hardware
    isDeploymentOwned: bool
    role: Workload_Citrix_Deployment_Resource_Role
    storage: Network_Storage
    subnet: Network_Subnet
    type_: str
    virtualGuest: Virtual_Guest
    vlan: Network_Vlan
