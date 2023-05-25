from SoftLayer.sltypes.Workload.Citrix.Workspace.Order.VMwareContainer import Workload_Citrix_Workspace_Order_VMwareContainer
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Entity import Entity

class Workload_Citrix_Workspace_Order_Container(Entity):
    """This is the datatype that needs to be populated and sent to
SoftLayer_Workload_Citrix_Workspace_Order::placeWorkspaceOrder."""
    activeDirectoryDomainName: str
    activeDirectoryNetbiosName: str
    activeDirectorySafeModePassword: str
    activeDirectoryTopology: str
    citrixAPIClientId: str
    citrixAPIClientSecret: str
    citrixCustomerId: str
    citrixResourceLocationName: str
    domain: str
    location: str
    orderContainers: list[Container_Product_Order]
    vmwareContainer: Workload_Citrix_Workspace_Order_VMwareContainer
