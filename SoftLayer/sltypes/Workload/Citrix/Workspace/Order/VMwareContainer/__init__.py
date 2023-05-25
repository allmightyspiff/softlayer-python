from SoftLayer.sltypes.Workload.Citrix.Workspace.Order.SharedStorage import Workload_Citrix_Workspace_Order_SharedStorage
from SoftLayer.sltypes.Workload.Citrix.Workspace.Order.LicenseKey import Workload_Citrix_Workspace_Order_LicenseKey
from SoftLayer.sltypes.Entity import Entity

class Workload_Citrix_Workspace_Order_VMwareContainer(Entity):
    """This is the datatype that needs to be populated and sent to
SoftLayer_Workload_Citrix_Workspace_Order::placeWorkspaceOrder to order and provision one or more VMware
server instances to be used with Citrix Virtual Apps and Desktops."""
    disks: list[str]
    domain: str
    licenseKeys: list[Workload_Citrix_Workspace_Order_LicenseKey]
    location: str
    name: str
    nickname: str
    quantity: int
    ram: str
    server: str
    sharedStorage: list[Workload_Citrix_Workspace_Order_SharedStorage]
    subdomain: str
    vSphereVersion: str
    vsanCacheDisks: list[str]
