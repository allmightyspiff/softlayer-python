# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Provisioning_Version1_Transaction_OrderTracking(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Provisioning_Version1_Transaction_OrderTracking'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction_OrderTracking':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction.OrderTracking import OrderTracking
        return OrderTracking(data)


    def getInvoiceId(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getInvoiceId',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderTrackingState(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction_OrderTrackingState':

        data = self.client.call(
            self.service,
            'getOrderTrackingState',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction.OrderTrackingState import OrderTrackingState
        return OrderTrackingState(data)


    def getTransaction(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'getTransaction',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


