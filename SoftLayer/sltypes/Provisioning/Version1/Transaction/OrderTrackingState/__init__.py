from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Provisioning_Version1_Transaction_OrderTrackingState(Entity):
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Provisioning_Version1_Transaction_OrderTrackingState'

    def getObject(self, identifier: int) -> 'Provisioning_Version1_Transaction_OrderTrackingState':
        """Retrieve a SoftLayer_Provisioning_Version1_Transaction_OrderTrackingState record."""
        data = self.client.call('SoftLayer_Provisioning_Version1_Transaction_OrderTrackingState', 'getObject', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction_OrderTrackingState import Provisioning_Version1_Transaction_OrderTrackingState
        return data
