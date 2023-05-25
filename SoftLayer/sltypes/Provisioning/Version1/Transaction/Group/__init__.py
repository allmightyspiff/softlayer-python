from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Provisioning_Version1_Transaction_Group(Entity):
    """The SoftLayer_Provisioning_Version1_Transaction_Group data type contains general information relating to a
single SoftLayer hardware transaction group.   SoftLayer customers are unable to change their hardware
transactions or the hardware transaction group."""
    averageTimeToComplete: float
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Provisioning_Version1_Transaction_Group'

    def getAllObjects(self) -> list['Provisioning_Version1_Transaction_Group']:
        data = self.client.call('SoftLayer_Provisioning_Version1_Transaction_Group', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Provisioning_Version1_Transaction_Group':
        """Retrieve a SoftLayer_Provisioning_Version1_Transaction_Group record."""
        data = self.client.call('SoftLayer_Provisioning_Version1_Transaction_Group', 'getObject', id=identifier)
        return data
