from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Auxiliary_Network_Status(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Auxiliary_Network_Status'

    def getNetworkStatus(self, target: str) -> list['Container_Auxiliary_Network_Status_Reading']:
        data = self.client.call('SoftLayer_Auxiliary_Network_Status', 'getNetworkStatus', target)
        from SoftLayer.sltypes.Container_Auxiliary_Network_Status_Reading import Container_Auxiliary_Network_Status_Reading
        return data
