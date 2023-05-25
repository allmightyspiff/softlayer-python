from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Note(Entity):
    accountId: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    note: str
    noteTypeId: int
    userId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Note'

    def createObject(self, templateObject: 'Account_Note') -> 'Account_Note':
        data = self.client.call('SoftLayer_Account_Note', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Account_Note', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Account_Note') -> bool:
        data = self.client.call('SoftLayer_Account_Note', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Account_Note':
        """Retrieve a SoftLayer_Account_Note record."""
        data = self.client.call('SoftLayer_Account_Note', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Note', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getCustomer(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Note', 'getCustomer', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getNoteHistory(self, identifier: int) -> list['Account_Note_History']:
        """"""
        data = self.client.call('SoftLayer_Account_Note', 'getNoteHistory', id=identifier)
        from SoftLayer.sltypes.Account_Note_History import Account_Note_History
        return data
