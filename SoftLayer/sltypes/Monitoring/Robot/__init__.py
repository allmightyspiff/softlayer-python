from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Monitoring_Robot(Entity):
    """DEPRECATED. The SoftLayer_Monitoring_Robot data type contains general information relating to a monitoring
robot."""
    accountId: int
    id_: int
    name: str
    statusId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Monitoring_Robot'

    def checkConnection(self, identifier: int) -> bool:
        """DEPRECATED. Checks if a monitoring robot can communicate with SoftLayer monitoring management system"""
        data = self.client.call('SoftLayer_Monitoring_Robot', 'checkConnection', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Monitoring_Robot':
        """Retrieve a SoftLayer_Monitoring_Robot record."""
        data = self.client.call('SoftLayer_Monitoring_Robot', 'getObject', id=identifier)
        return data
