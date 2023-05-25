from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Locale(Entity):
    friendlyName: str
    id_: int
    languageTag: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Locale'

    def getClosestToLanguageTag(self, languageTag: str) -> 'Locale':
        """Get the closest locale for the language tag (ISO 639-1 & 3166-1) format."""
        data = self.client.call('SoftLayer_Locale', 'getClosestToLanguageTag', languageTag)
        from SoftLayer.sltypes.Locale import Locale
        return data

    def getObject(self, identifier: int) -> 'Locale':
        """Retrieve a SoftLayer_Locale record."""
        data = self.client.call('SoftLayer_Locale', 'getObject', id=identifier)
        from SoftLayer.sltypes.Locale import Locale
        return data
