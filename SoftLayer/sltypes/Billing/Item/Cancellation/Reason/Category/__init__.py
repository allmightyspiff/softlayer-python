from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Item_Cancellation_Reason_Category(Entity):
    """The SoftLayer_Billing_Item_Cancellation_Reason_Category data type contains cancellation reason categories."""
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Item_Cancellation_Reason_Category'

    def getAllCancellationReasonCategories(self) -> list['Billing_Item_Cancellation_Reason_Category']:
        """Retrieve all available cancellation reason categories."""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Reason_Category', 'getAllCancellationReasonCategories')
        return data

    def getObject(self, identifier: int) -> 'Billing_Item_Cancellation_Reason_Category':
        """Retrieve a SoftLayer_Billing_Item_Cancellation_Reason_Category record."""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Reason_Category', 'getObject', id=identifier)
        return data

    def getBillingCancellationReasons(self, identifier: int) -> list['Billing_Item_Cancellation_Reason']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Reason_Category', 'getBillingCancellationReasons', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Cancellation_Reason import Billing_Item_Cancellation_Reason
        return data
