from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Item_Cancellation_Reason(Entity):
    """The SoftLayer_Billing_Item_Cancellation_Reason data type contains cancellation reasons."""
    billingCancelReasonCategoryId: int
    id_: int
    keyName: str
    reason: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Item_Cancellation_Reason'

    def getAllCancellationReasons(self) -> list['Billing_Item_Cancellation_Reason']:
        """Retrieve all available cancellation reasons."""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Reason', 'getAllCancellationReasons')
        from SoftLayer.sltypes.Billing_Item_Cancellation_Reason import Billing_Item_Cancellation_Reason
        return data

    def getObject(self, identifier: int) -> 'Billing_Item_Cancellation_Reason':
        """Retrieve a SoftLayer_Billing_Item_Cancellation_Reason record."""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Reason', 'getObject', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Cancellation_Reason import Billing_Item_Cancellation_Reason
        return data

    def getBillingCancellationReasonCategory(self, identifier: int) -> 'Billing_Item_Cancellation_Reason_Category':
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Reason', 'getBillingCancellationReasonCategory', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Cancellation_Reason_Category import Billing_Item_Cancellation_Reason_Category
        return data

    def getBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Reason', 'getBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getTranslatedReason(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Reason', 'getTranslatedReason', id=identifier)
        return data
