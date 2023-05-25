from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Workload_Citrix_Deployment_Resource(Entity):
    """The SoftLayer_Workload_Citrix_Deployment_Resource type contains the information of the resource such as the
Deployment ID, resource's Billing Item ID, Order ID and Role of the resource in the CVAD deployment."""
    billingItemId: int
    createDate: datetime
    deploymentId: int
    id_: int
    modifyDate: datetime
    orderId: int
    orderedByCvad: bool
    roleId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Workload_Citrix_Deployment_Resource'

    def createObject(self, templateObject: 'Workload_Citrix_Deployment_Resource') -> 'Workload_Citrix_Deployment_Resource':
        """Add the resource into CVAD deployment resources."""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment_Resource', 'createObject', templateObject)
        return data

    def getAllObjects(self) -> list['Workload_Citrix_Deployment_Resource']:
        """Get all the Citrix deployment resources."""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment_Resource', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Workload_Citrix_Deployment_Resource':
        """Retrieve a SoftLayer_Workload_Citrix_Deployment_Resource record."""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment_Resource', 'getObject', id=identifier)
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment_Resource', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getDeployment(self, identifier: int) -> 'Workload_Citrix_Deployment':
        """"""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment_Resource', 'getDeployment', id=identifier)
        from SoftLayer.sltypes.Workload_Citrix_Deployment import Workload_Citrix_Deployment
        return data

    def getOrder(self, identifier: int) -> 'Billing_Order':
        """"""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment_Resource', 'getOrder', id=identifier)
        from SoftLayer.sltypes.Billing_Order import Billing_Order
        return data

    def getRole(self, identifier: int) -> 'Workload_Citrix_Deployment_Resource_Role':
        """"""
        data = self.client.call('SoftLayer_Workload_Citrix_Deployment_Resource', 'getRole', id=identifier)
        from SoftLayer.sltypes.Workload_Citrix_Deployment_Resource_Role import Workload_Citrix_Deployment_Resource_Role
        return data
