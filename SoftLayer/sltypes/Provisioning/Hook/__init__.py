from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Provisioning_Hook(Entity):
    """The SoftLayer_Provisioning_Hook contains all the information needed to add a hook into a server/Virtual
provision and os reload."""
    accountId: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    name: str
    typeId: int
    uri: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Provisioning_Hook'

    def createObject(self, templateObject: 'Provisioning_Hook') -> 'Provisioning_Hook':
        data = self.client.call('SoftLayer_Provisioning_Hook', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Provisioning_Hook', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Provisioning_Hook') -> bool:
        data = self.client.call('SoftLayer_Provisioning_Hook', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Provisioning_Hook':
        """Retrieve a SoftLayer_Provisioning_Hook record."""
        data = self.client.call('SoftLayer_Provisioning_Hook', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Provisioning_Hook', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getHookType(self, identifier: int) -> 'Provisioning_Hook_Type':
        """"""
        data = self.client.call('SoftLayer_Provisioning_Hook', 'getHookType', id=identifier)
        from SoftLayer.sltypes.Provisioning_Hook_Type import Provisioning_Hook_Type
        return data
