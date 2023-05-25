from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Workload_Citrix_Workspace_Response(Entity):
    messageId: str
    status: str
    statusMessage: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Workload_Citrix_Workspace_Response'
