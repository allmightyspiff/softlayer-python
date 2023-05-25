from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Location_Reservation_Rack(Entity):
    locationId: int
    locationReservationId: int
    networkConnectionCapacity: int
    networkConnectionReservation: int
    powerConnectionCapacity: int
    powerConnectionReservation: int
    slotCapacity: int
    slotReservation: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Location_Reservation_Rack'

    def getObject(self, identifier: int) -> 'Location_Reservation_Rack':
        """Retrieve a SoftLayer_Location_Reservation_Rack record."""
        data = self.client.call('SoftLayer_Location_Reservation_Rack', 'getObject', id=identifier)
        return data

    def getAllotment(self, identifier: int) -> 'Network_Bandwidth_Version1_Allotment':
        """"""
        data = self.client.call('SoftLayer_Location_Reservation_Rack', 'getAllotment', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getChildren(self, identifier: int) -> list['Location_Reservation_Rack_Member']:
        """"""
        data = self.client.call('SoftLayer_Location_Reservation_Rack', 'getChildren', id=identifier)
        from SoftLayer.sltypes.Location_Reservation_Rack_Member import Location_Reservation_Rack_Member
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Location_Reservation_Rack', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getLocationReservation(self, identifier: int) -> 'Location_Reservation':
        """"""
        data = self.client.call('SoftLayer_Location_Reservation_Rack', 'getLocationReservation', id=identifier)
        from SoftLayer.sltypes.Location_Reservation import Location_Reservation
        return data
