from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_ReservedCapacityGroup(Entity):
    """This data type presents the structure for a virtual reserved capacity group."""
    accountId: int
    backendRouterId: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_ReservedCapacityGroup'

    def editObject(self, identifier: int, templateObject: 'Virtual_ReservedCapacityGroup') -> bool:
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Virtual_ReservedCapacityGroup':
        """Retrieve a SoftLayer_Virtual_ReservedCapacityGroup record."""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup', 'getObject', id=identifier)
        from SoftLayer.sltypes.Virtual_ReservedCapacityGroup import Virtual_ReservedCapacityGroup
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAvailableInstances(self, identifier: int) -> list['Virtual_ReservedCapacityGroup_Instance']:
        """"""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup', 'getAvailableInstances', id=identifier)
        from SoftLayer.sltypes.Virtual_ReservedCapacityGroup_Instance import Virtual_ReservedCapacityGroup_Instance
        return data

    def getBackendRouter(self, identifier: int) -> 'Hardware_Router_Backend':
        """"""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup', 'getBackendRouter', id=identifier)
        from SoftLayer.sltypes.Hardware_Router_Backend import Hardware_Router_Backend
        return data

    def getInstances(self, identifier: int) -> list['Virtual_ReservedCapacityGroup_Instance']:
        """"""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup', 'getInstances', id=identifier)
        from SoftLayer.sltypes.Virtual_ReservedCapacityGroup_Instance import Virtual_ReservedCapacityGroup_Instance
        return data

    def getInstancesCount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup', 'getInstancesCount', id=identifier)
        return data

    def getOccupiedInstances(self, identifier: int) -> list['Virtual_ReservedCapacityGroup_Instance']:
        """"""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup', 'getOccupiedInstances', id=identifier)
        from SoftLayer.sltypes.Virtual_ReservedCapacityGroup_Instance import Virtual_ReservedCapacityGroup_Instance
        return data
