from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_Invitation(Entity):
    code: str
    createDate: datetime
    creatorId: int
    creatorType: str
    email: str
    existingBlueIdFlag: int
    expirationDate: datetime
    ibmIdUsername: str
    id_: int
    isFederatedEmailDomainFlag: int
    modifyDate: datetime
    responseDate: datetime
    statusId: int
    userId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_Invitation'

    def getObject(self, identifier: int) -> 'User_Customer_Invitation':
        """Retrieve a SoftLayer_User_Customer_Invitation record."""
        data = self.client.call('SoftLayer_User_Customer_Invitation', 'getObject', id=identifier)
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_User_Customer_Invitation', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
