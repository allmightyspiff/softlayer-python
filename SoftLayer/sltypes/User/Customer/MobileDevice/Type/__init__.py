from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_MobileDevice_Type(Entity):
    """Describes a supported class of mobile device. In this the word class is used in the context of classes of
consumer electronic devices, the two most prominent examples being mobile phones and tablets."""
    createDate: datetime
    description: str
    id_: int
    modifyDate: datetime
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_MobileDevice_Type'

    def getAllObjects(self) -> list['User_Customer_MobileDevice_Type']:
        data = self.client.call('SoftLayer_User_Customer_MobileDevice_Type', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'User_Customer_MobileDevice_Type':
        """Retrieve a SoftLayer_User_Customer_MobileDevice_Type record."""
        data = self.client.call('SoftLayer_User_Customer_MobileDevice_Type', 'getObject', id=identifier)
        return data
