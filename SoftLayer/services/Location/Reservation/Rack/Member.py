# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Location_Reservation_Rack_Member(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Location_Reservation_Rack_Member'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Reservation_Rack_Member':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Reservation.Rack.Member import Member
        return Member(data)


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


