from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Workload_Citrix_Deployment_Type(Entity):
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Workload_Citrix_Deployment_Type'

    def getObject(self, identifier: int) -> 'Workload_Citrix_Deployment_Type':
        """Retrieve a SoftLayer_Workload_Citrix_Deployment_Type record."""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment_Type', 'getObject', id=identifier)
        return data
