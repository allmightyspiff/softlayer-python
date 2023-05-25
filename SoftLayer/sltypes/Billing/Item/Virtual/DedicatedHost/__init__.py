from SoftLayer.sltypes.Billing.Item import Billing_Item
from SoftLayer.sltypes.Billing_Item import Billing_Item
from SoftLayer import BaseClient

class Billing_Item_Virtual_DedicatedHost(Billing_Item):
    resourceTableId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Item_Virtual_DedicatedHost'

    def getObject(self, identifier: int) -> 'Billing_Item_Virtual_DedicatedHost':
        """Retrieve a SoftLayer_Billing_Item_Virtual_DedicatedHost record."""
        data = self.client.call('SoftLayer_Billing_Item_Virtual_DedicatedHost', 'getObject', id=identifier)
        return data

    def getResource(self, identifier: int) -> 'Virtual_DedicatedHost':
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Virtual_DedicatedHost', 'getResource', id=identifier)
        from SoftLayer.sltypes.Virtual_DedicatedHost import Virtual_DedicatedHost
        return data
