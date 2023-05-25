from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Locale_Timezone(Entity):
    """Each User is assigned a timezone allowing for a precise local timestamp."""
    id_: int
    longName: str
    name: str
    offset: str
    shortName: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Locale_Timezone'

    def getAllObjects(self) -> list['Locale_Timezone']:
        """Retrieve all timezone objects."""
        data = self.client.call('SoftLayer_Locale_Timezone', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Locale_Timezone':
        """Retrieve a SoftLayer_Locale_Timezone record."""
        data = self.client.call('SoftLayer_Locale_Timezone', 'getObject', id=identifier)
        return data
