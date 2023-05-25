from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Provisioning_Version1_Transaction_OrderTracking(Entity):
    id_: int
    orderStateId: int
    transactionId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Provisioning_Version1_Transaction_OrderTracking'

    def getObject(self, identifier: int) -> 'Provisioning_Version1_Transaction_OrderTracking':
        """Retrieve a SoftLayer_Provisioning_Version1_Transaction_OrderTracking record."""
        data = self.client.call('SoftLayer_Provisioning_Version1_Transaction_OrderTracking', 'getObject', id=identifier)
        return data

    def getInvoiceId(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Provisioning_Version1_Transaction_OrderTracking', 'getInvoiceId', id=identifier)
        return data

    def getOrderTrackingState(self, identifier: int) -> 'Provisioning_Version1_Transaction_OrderTrackingState':
        """"""
        data = self.client.call('SoftLayer_Provisioning_Version1_Transaction_OrderTracking', 'getOrderTrackingState', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction_OrderTrackingState import Provisioning_Version1_Transaction_OrderTrackingState
        return data

    def getTransaction(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Provisioning_Version1_Transaction_OrderTracking', 'getTransaction', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data
