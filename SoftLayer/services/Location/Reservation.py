# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Location_Reservation(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Location_Reservation'
        self.client = client

    def getAccountReservations(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location_Reservation]':

        data = self.client.call(
            self.service,
            'getAccountReservations',
            mask=objectMask
        )
        from SoftLayer.datatypes.Location.Reservation import Reservation
        return Reservation(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Reservation':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Reservation import Reservation
        return Reservation(data)


    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getAllotment(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Version1_Allotment':

        data = self.client.call(
            self.service,
            'getAllotment',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


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


    def getLocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getLocation',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getLocationReservationRack(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Reservation_Rack':

        data = self.client.call(
            self.service,
            'getLocationReservationRack',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Reservation.Rack import Rack
        return Rack(data)


