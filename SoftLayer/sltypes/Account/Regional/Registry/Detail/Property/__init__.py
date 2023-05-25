from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Regional_Registry_Detail_Property(Entity):
    """Subnet registration properties are used to define various attributes of the
[[SoftLayer_Account_Regional_Registry_Detail|detail objects]]. These properties are defined by the
[[SoftLayer_Account_Regional_Registry_Detail_Property_Type]] objects, which describe the available value
formats."""
    createDate: datetime
    id_: int
    modifyDate: datetime
    propertyTypeId: int
    registrationDetailId: int
    sequencePosition: int
    value: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Regional_Registry_Detail_Property'

    def createObject(self, templateObject: 'Account_Regional_Registry_Detail_Property') -> 'Account_Regional_Registry_Detail_Property':
        """Create a new property object"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Property', 'createObject', templateObject)
        return data

    def createObjects(self, templateObjects: 'Account_Regional_Registry_Detail_Property') -> list['Account_Regional_Registry_Detail_Property']:
        """Create multiple property objects."""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Property', 'createObjects', templateObjects)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete an existing property object"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Property', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Account_Regional_Registry_Detail_Property') -> bool:
        """Edit an existing property object"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Property', 'editObject', templateObject, id=identifier)
        return data

    def editObjects(self, templateObjects: 'Account_Regional_Registry_Detail_Property') -> bool:
        """Edit multiple property objects."""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Property', 'editObjects', templateObjects)
        return data

    def getObject(self, identifier: int) -> 'Account_Regional_Registry_Detail_Property':
        """Retrieve a SoftLayer_Account_Regional_Registry_Detail_Property record."""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Property', 'getObject', id=identifier)
        return data

    def getDetail(self, identifier: int) -> 'Account_Regional_Registry_Detail':
        """"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Property', 'getDetail', id=identifier)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail import Account_Regional_Registry_Detail
        return data

    def getPropertyType(self, identifier: int) -> 'Account_Regional_Registry_Detail_Property_Type':
        """"""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Property', 'getPropertyType', id=identifier)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail_Property_Type import Account_Regional_Registry_Detail_Property_Type
        return data
