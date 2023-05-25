from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Location_Reservation(Entity):
    allotmentId: int
    id_: int
    locationId: int
    name: str
    notes: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Location_Reservation'

    def getAccountReservations(self) -> list['Location_Reservation']:
        data = self.client.call('SoftLayer_Location_Reservation', 'getAccountReservations')
        from SoftLayer.sltypes.Location_Reservation import Location_Reservation
        return data

    def getObject(self, identifier: int) -> 'Location_Reservation':
        """Retrieve a SoftLayer_Location_Reservation record."""
        data = self.client.call('SoftLayer_Location_Reservation', 'getObject', id=identifier)
        from SoftLayer.sltypes.Location_Reservation import Location_Reservation
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Location_Reservation', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAllotment(self, identifier: int) -> 'Network_Bandwidth_Version1_Allotment':
        """"""
        data = self.client.call('SoftLayer_Location_Reservation', 'getAllotment', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Location_Reservation', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Location_Reservation', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getLocationReservationRack(self, identifier: int) -> 'Location_Reservation_Rack':
        """"""
        data = self.client.call('SoftLayer_Location_Reservation', 'getLocationReservationRack', id=identifier)
        from SoftLayer.sltypes.Location_Reservation_Rack import Location_Reservation_Rack
        return data
