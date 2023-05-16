# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Item_Cancellation_Reason(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Item_Cancellation_Reason'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAllCancellationReasons(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Billing_Item_Cancellation_Reason]':
        data = self.client.call(
            self.service,
            'getAllCancellationReasons',
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Reason import Reason
        return SL_Reason(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Reason':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Reason import Reason
        return SL_Reason(data)

# This file was automatically generated with tools/generateTypes.py
    def getBillingCancellationReasonCategory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Reason_Category':
        data = self.client.call(
            self.service,
            'getBillingCancellationReasonCategory',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Reason.Category import Category
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
    def getBillingItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':
        data = self.client.call(
            self.service,
            'getBillingItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
    def getTranslatedReason(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getTranslatedReason',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


