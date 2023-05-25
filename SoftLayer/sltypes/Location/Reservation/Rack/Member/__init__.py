from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Location_Reservation_Rack_Member(Entity):
    id_: int
    locationId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Location_Reservation_Rack_Member'

    def getObject(self, identifier: int) -> 'Location_Reservation_Rack_Member':
        """Retrieve a SoftLayer_Location_Reservation_Rack_Member record."""
        data = self.client.call('SoftLayer_Location_Reservation_Rack_Member', 'getObject', id=identifier)
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Location_Reservation_Rack_Member', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getLocationReservationRack(self, identifier: int) -> 'Location_Reservation_Rack':
        """"""
        data = self.client.call('SoftLayer_Location_Reservation_Rack_Member', 'getLocationReservationRack', id=identifier)
        from SoftLayer.sltypes.Location_Reservation_Rack import Location_Reservation_Rack
        return data
