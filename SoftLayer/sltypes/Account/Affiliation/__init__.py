from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Affiliation(Entity):
    """This service allows for a unique identifier to be associated to an existing customer account."""
    accountId: int
    affiliateId: str
    createDate: datetime
    id_: int
    modifyDate: datetime

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Affiliation'

    def createObject(self, templateObject: 'Account_Affiliation') -> 'Account_Affiliation':
        """Create a new affiliation."""
        data = self.client.call('SoftLayer_Account_Affiliation', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete an account affiliation"""
        data = self.client.call('SoftLayer_Account_Affiliation', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Account_Affiliation') -> bool:
        """Update an account affiliation information."""
        data = self.client.call('SoftLayer_Account_Affiliation', 'editObject', templateObject, id=identifier)
        return data

    def getAccountAffiliationsByAffiliateId(self, affiliateId: str) -> list['Account_Affiliation']:
        """Get account affiliation information associated with affiliate id."""
        data = self.client.call('SoftLayer_Account_Affiliation', 'getAccountAffiliationsByAffiliateId', affiliateId)
        return data

    def getObject(self, identifier: int) -> 'Account_Affiliation':
        """Retrieve a SoftLayer_Account_Affiliation record."""
        data = self.client.call('SoftLayer_Account_Affiliation', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Affiliation', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data
