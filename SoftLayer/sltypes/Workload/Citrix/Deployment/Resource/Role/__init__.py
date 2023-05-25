from SoftLayer.sltypes.Entity import Entity

class Workload_Citrix_Deployment_Resource_Role(Entity):
    """SoftLayer_Workload_Citrix_Deployment_Resource_Role contains the role and its description of any resource of
Citrix Virtual Apps & Desktops deployment."""
    description: str
    id_: int
    keyName: str
    name: str
