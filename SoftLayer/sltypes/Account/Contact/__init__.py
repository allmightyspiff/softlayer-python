from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Contact(Entity):
    accountId: int
    address1: str
    address2: str
    alternatePhone: str
    city: str
    companyName: str
    country: str
    createDate: datetime
    email: str
    faxPhone: str
    firstName: str
    id_: int
    jobTitle: str
    lastName: str
    modifyDate: datetime
    officePhone: str
    postalCode: str
    profileName: str
    state: str
    typeId: int
    url: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Contact'

    def createComplianceReportRequestorContact(self, requestorTemplate: 'Account_Contact') -> 'Account_Contact':
        data = self.client.call('SoftLayer_Account_Contact', 'createComplianceReportRequestorContact', requestorTemplate)
        return data

    def createObject(self, templateObject: 'Account_Contact') -> 'Account_Contact':
        """This method creates an account contact."""
        data = self.client.call('SoftLayer_Account_Contact', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete an account contact"""
        data = self.client.call('SoftLayer_Account_Contact', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Account_Contact') -> bool:
        """Edit an existing account contact."""
        data = self.client.call('SoftLayer_Account_Contact', 'editObject', templateObject, id=identifier)
        return data

    def getAllContactTypes(self) -> list['Account_Contact_Type']:
        """This method retrieves available contact types."""
        data = self.client.call('SoftLayer_Account_Contact', 'getAllContactTypes')
        from SoftLayer.sltypes.Account_Contact_Type import Account_Contact_Type
        return data

    def getObject(self, identifier: int) -> 'Account_Contact':
        """Retrieve a SoftLayer_Account_Contact record."""
        data = self.client.call('SoftLayer_Account_Contact', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Contact', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getType(self, identifier: int) -> 'Account_Contact_Type':
        """"""
        data = self.client.call('SoftLayer_Account_Contact', 'getType', id=identifier)
        from SoftLayer.sltypes.Account_Contact_Type import Account_Contact_Type
        return data
