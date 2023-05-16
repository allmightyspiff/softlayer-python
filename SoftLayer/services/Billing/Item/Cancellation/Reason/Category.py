# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Item_Cancellation_Reason_Category(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Item_Cancellation_Reason_Category'
        self.client = client

    def getAllCancellationReasonCategories(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Billing_Item_Cancellation_Reason_Category]':

        data = self.client.call(
            self.service,
            'getAllCancellationReasonCategories',
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Reason.Category import Category
        return Category(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Reason_Category':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Reason.Category import Category
        return Category(data)


    def getBillingCancellationReasons(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item_Cancellation_Reason]':

        data = self.client.call(
            self.service,
            'getBillingCancellationReasons',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Reason import Reason
        return Reason(data)


