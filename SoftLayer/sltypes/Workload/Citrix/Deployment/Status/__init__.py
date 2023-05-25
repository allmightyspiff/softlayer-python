from SoftLayer.sltypes.Entity import Entity

class Workload_Citrix_Deployment_Status(Entity):
    """The SoftLayer_Workload_Citrix_Deployment_Status shows the status of Citrix Virtual Apps and Desktop
deployment. The deployment can be in one of the following statuses at a given point in time: - PROVISIONING:
The resources are being provisioned for the deployment. - ACTIVE: All the resources for the deployment are
ready. - CANCELLING: Resources of the deployment are being cancelled. - CANCELLED: All the resources of the
deployment are cancelled."""
    description: str
    id_: int
    keyName: str
    name: str
