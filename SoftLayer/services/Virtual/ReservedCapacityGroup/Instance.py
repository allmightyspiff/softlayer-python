# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_ReservedCapacityGroup_Instance(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_ReservedCapacityGroup_Instance'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_ReservedCapacityGroup_Instance':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup.Instance import Instance
        return Instance(data)


    def getAvailableFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getAvailableFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getGuest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getGuest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getReservedCapacityGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_ReservedCapacityGroup':

        data = self.client.call(
            self.service,
            'getReservedCapacityGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup import ReservedCapacityGroup
        return ReservedCapacityGroup(data)


