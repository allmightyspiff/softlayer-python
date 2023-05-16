# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Item_Cancellation_Reason(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Item_Cancellation_Reason'
        self.client = client

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
        return Reason(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Reason':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Reason import Reason
        return Reason(data)


    def getBillingCancellationReasonCategory(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Reason_Category':

        data = self.client.call(
            self.service,
            'getBillingCancellationReasonCategory',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Reason.Category import Category
        return Category(data)


    def getBillingItems(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getBillingItems',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getTranslatedReason(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getTranslatedReason',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


