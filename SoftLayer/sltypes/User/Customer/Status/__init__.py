from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_Status(Entity):
    """Each SoftLayer User Customer instance is assigned a status code that determines how it's treated in the
customer portal. This status is reflected in the SoftLayer_User_Customer_Status data type. Status differs
from user permissions in that user status applies globally to the portal while user permissions are applied
to specific portal functions.   Note that a status of "PENDING" also has been added. This status is specific
to users that are configured to use IBMid authentication. This would include some (not all) users on accounts
that are linked to Platform Services (PaaS, formerly Bluemix) accounts, but is not limited to users in such
accounts. Using IBMid authentication is optional for active users even if it is not required by the account
type. PENDING status indicates that a relationship between an IBMid and a user is being set up but is not
complete. To be complete, PENDING users need to perform an action ("accepting the invitation") before
becoming an active user within IBM Cloud and/or IMS. PENDING is a system state, and can not be administered
by users (including the account master user). SoftLayer Commercial is the only environment where IBMid and/or
account linking are used."""
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_Status'

    def getAllObjects(self) -> list['User_Customer_Status']:
        """Retrieve all user status objects."""
        data = self.client.call('SoftLayer_User_Customer_Status', 'getAllObjects')
        from SoftLayer.sltypes.User_Customer_Status import User_Customer_Status
        return data

    def getObject(self, identifier: int) -> 'User_Customer_Status':
        """Retrieve a SoftLayer_User_Customer_Status record."""
        data = self.client.call('SoftLayer_User_Customer_Status', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Customer_Status import User_Customer_Status
        return data
