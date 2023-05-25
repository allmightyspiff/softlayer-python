from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_Guest_Boot_Parameter(Entity):
    createDate: datetime
    guestBootParameterTypeId: int
    guestId: int
    id_: int
    modifyDate: datetime

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_Guest_Boot_Parameter'

    def createObject(self, templateObject: 'Virtual_Guest_Boot_Parameter') -> bool:
        """Create a boot parameter record to be used at next boot"""
        data = self.client.call('SoftLayer_Virtual_Guest_Boot_Parameter', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Removes a boot parameter"""
        data = self.client.call('SoftLayer_Virtual_Guest_Boot_Parameter', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Virtual_Guest_Boot_Parameter') -> bool:
        """Edits a single boot parameter"""
        data = self.client.call('SoftLayer_Virtual_Guest_Boot_Parameter', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Virtual_Guest_Boot_Parameter':
        """Retrieve a SoftLayer_Virtual_Guest_Boot_Parameter record."""
        data = self.client.call('SoftLayer_Virtual_Guest_Boot_Parameter', 'getObject', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Boot_Parameter import Virtual_Guest_Boot_Parameter
        return data

    def getGuest(self, identifier: int) -> 'Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Boot_Parameter', 'getGuest', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getGuestBootParameterType(self, identifier: int) -> 'Virtual_Guest_Boot_Parameter_Type':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Boot_Parameter', 'getGuestBootParameterType', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Boot_Parameter_Type import Virtual_Guest_Boot_Parameter_Type
        return data
