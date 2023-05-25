from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_PlacementGroup(Entity):
    """This data type presents the structure for a virtual guest placement group. The data type contains relational
properties to the virtual guest placement group rule class."""
    accountId: int
    backendRouterId: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    name: str
    ruleId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_PlacementGroup'

    def createObject(self, templateObject: 'Virtual_PlacementGroup') -> 'Virtual_PlacementGroup':
        data = self.client.call('SoftLayer_Virtual_PlacementGroup', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_PlacementGroup', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Virtual_PlacementGroup') -> bool:
        data = self.client.call('SoftLayer_Virtual_PlacementGroup', 'editObject', templateObject, id=identifier)
        return data

    def getAvailableRouters(self, datacenterId: int) -> list['Hardware']:
        data = self.client.call('SoftLayer_Virtual_PlacementGroup', 'getAvailableRouters', datacenterId)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getObject(self, identifier: int) -> 'Virtual_PlacementGroup':
        """Retrieve a SoftLayer_Virtual_PlacementGroup record."""
        data = self.client.call('SoftLayer_Virtual_PlacementGroup', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Virtual_PlacementGroup', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getBackendRouter(self, identifier: int) -> 'Hardware_Router_Backend':
        """"""
        data = self.client.call('SoftLayer_Virtual_PlacementGroup', 'getBackendRouter', id=identifier)
        from SoftLayer.sltypes.Hardware_Router_Backend import Hardware_Router_Backend
        return data

    def getGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Virtual_PlacementGroup', 'getGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getRule(self, identifier: int) -> 'Virtual_PlacementGroup_Rule':
        """"""
        data = self.client.call('SoftLayer_Virtual_PlacementGroup', 'getRule', id=identifier)
        from SoftLayer.sltypes.Virtual_PlacementGroup_Rule import Virtual_PlacementGroup_Rule
        return data
