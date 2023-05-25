from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Workload_Citrix_Deployment(Entity):
    accountId: int
    activeDirectoryTopology: str
    createDate: datetime
    dataCenter: str
    id_: int
    modifyDate: datetime
    name: str
    statusId: int
    typeId: int
    userRecordId: int
    vlanId: int
    vmwareOrderId: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Workload_Citrix_Deployment'

    def createObject(self, templateObject: 'Workload_Citrix_Deployment') -> 'Workload_Citrix_Deployment':
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment', 'createObject', templateObject)
        from SoftLayer.sltypes.Workload_Citrix_Deployment import Workload_Citrix_Deployment
        return data

    def getAllObjects(self) -> list['Workload_Citrix_Deployment']:
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment', 'getAllObjects')
        from SoftLayer.sltypes.Workload_Citrix_Deployment import Workload_Citrix_Deployment
        return data

    def getDeployment(self, deploymentId: int) -> 'Workload_Citrix_Deployment_Response':
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment', 'getDeployment', deploymentId)
        from SoftLayer.sltypes.Workload_Citrix_Deployment_Response import Workload_Citrix_Deployment_Response
        return data

    def getObject(self, identifier: int) -> 'Workload_Citrix_Deployment':
        """Retrieve a SoftLayer_Workload_Citrix_Deployment record."""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment', 'getObject', id=identifier)
        from SoftLayer.sltypes.Workload_Citrix_Deployment import Workload_Citrix_Deployment
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getResources(self, identifier: int) -> list['Workload_Citrix_Deployment_Resource']:
        """"""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment', 'getResources', id=identifier)
        from SoftLayer.sltypes.Workload_Citrix_Deployment_Resource import Workload_Citrix_Deployment_Resource
        return data

    def getStatus(self, identifier: int) -> 'Workload_Citrix_Deployment_Status':
        """"""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Workload_Citrix_Deployment_Status import Workload_Citrix_Deployment_Status
        return data

    def getType(self, identifier: int) -> 'Workload_Citrix_Deployment_Type':
        """"""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment', 'getType', id=identifier)
        from SoftLayer.sltypes.Workload_Citrix_Deployment_Type import Workload_Citrix_Deployment_Type
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getVlan(self, identifier: int) -> 'Network_Vlan':
        """"""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment', 'getVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data
