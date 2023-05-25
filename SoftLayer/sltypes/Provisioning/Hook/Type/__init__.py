from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Provisioning_Hook_Type(Entity):
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Provisioning_Hook_Type'

    def getAllHookTypes(self) -> list['Provisioning_Hook_Type']:
        data = self.client.call('SoftLayer_Provisioning_Hook_Type', 'getAllHookTypes')
        return data

    def getObject(self, identifier: int) -> 'Provisioning_Hook_Type':
        """Retrieve a SoftLayer_Provisioning_Hook_Type record."""
        data = self.client.call('SoftLayer_Provisioning_Hook_Type', 'getObject', id=identifier)
        return data
