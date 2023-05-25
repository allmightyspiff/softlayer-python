from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class BluePages_Search(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'BluePages_Search'

    def findBluePagesProfile(self, emailAddress: str) -> 'BluePages_Container_EmployeeProfile':
        data = self.client.call('BluePages_Search', 'findBluePagesProfile', emailAddress)
        return data
