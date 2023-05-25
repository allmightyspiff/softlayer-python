from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_ReservedCapacityGroup_Instance(Entity):
    """This data type presents the structure for a virtual reserved capacity group instance."""
    createDate: datetime
    guestId: int
    id_: int
    modifyDate: datetime
    reservedCapacityGroupId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_ReservedCapacityGroup_Instance'

    def getObject(self, identifier: int) -> 'Virtual_ReservedCapacityGroup_Instance':
        """Retrieve a SoftLayer_Virtual_ReservedCapacityGroup_Instance record."""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup_Instance', 'getObject', id=identifier)
        return data

    def getAvailableFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup_Instance', 'getAvailableFlag', id=identifier)
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup_Instance', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getGuest(self, identifier: int) -> 'Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup_Instance', 'getGuest', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getReservedCapacityGroup(self, identifier: int) -> 'Virtual_ReservedCapacityGroup':
        """"""
        data = self.client.call('SoftLayer_Virtual_ReservedCapacityGroup_Instance', 'getReservedCapacityGroup', id=identifier)
        from SoftLayer.sltypes.Virtual_ReservedCapacityGroup import Virtual_ReservedCapacityGroup
        return data
