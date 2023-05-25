from SoftLayer.sltypes.Workload.Citrix.Deployment.Type import Workload_Citrix_Deployment_Type
from SoftLayer.sltypes.Workload.Citrix.Deployment.Status import Workload_Citrix_Deployment_Status
from SoftLayer.sltypes.Workload.Citrix.Deployment.Resource.Response import Workload_Citrix_Deployment_Resource_Response
from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Workload_Citrix_Deployment_Response(Entity):
    """The SoftLayer_Workload_Citrix_Deployment_Response constructs a response object for the
[[SoftLayer_Workload_Citrix_Deployment]] that includes all resources, i.e.,
[[SoftLayer_Workload_Citrix_Deployment_Resource]]."""
    accountId: int
    activeDirectoryTopology: str
    createDate: datetime
    dataCenter: str
    id_: int
    modifyDate: datetime
    name: str
    resources: list[Workload_Citrix_Deployment_Resource_Response]
    status: Workload_Citrix_Deployment_Status
    type_: Workload_Citrix_Deployment_Type
    userRecordId: int
    vlanId: int
    vmwareOrderId: str
