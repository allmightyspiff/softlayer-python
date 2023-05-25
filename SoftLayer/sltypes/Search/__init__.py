from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Search(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Search'

    def advancedSearch(self, searchString: str) -> list['Container_Search_Result']:
        """Search for SoftLayer Resources by simple terms."""
        data = self.client.call('SoftLayer_Search', 'advancedSearch', searchString)
        from SoftLayer.sltypes.Container_Search_Result import Container_Search_Result
        return data

    def getObjectTypes(self) -> list['Container_Search_ObjectType']:
        """Return a collection of indexed object types."""
        data = self.client.call('SoftLayer_Search', 'getObjectTypes')
        from SoftLayer.sltypes.Container_Search_ObjectType import Container_Search_ObjectType
        return data

    def search(self, searchString: str) -> list['Container_Search_Result']:
        """Search for SoftLayer Resources by simple phrase."""
        data = self.client.call('SoftLayer_Search', 'search', searchString)
        from SoftLayer.sltypes.Container_Search_Result import Container_Search_Result
        return data
