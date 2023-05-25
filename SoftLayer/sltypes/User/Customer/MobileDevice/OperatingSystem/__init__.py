from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_MobileDevice_OperatingSystem(Entity):
    """This class represents the mobile operating system installed on a user's registered mobile device. It assists
us when determining the how to get a push notification to the user."""
    buildVersion: int
    createDate: datetime
    description: str
    id_: int
    majorVersion: int
    minorVersion: int
    modifyDate: datetime
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_MobileDevice_OperatingSystem'

    def getAllObjects(self) -> list['User_Customer_MobileDevice_OperatingSystem']:
        data = self.client.call('SoftLayer_User_Customer_MobileDevice_OperatingSystem', 'getAllObjects')
        from SoftLayer.sltypes.User_Customer_MobileDevice_OperatingSystem import User_Customer_MobileDevice_OperatingSystem
        return data

    def getObject(self, identifier: int) -> 'User_Customer_MobileDevice_OperatingSystem':
        """Retrieve a SoftLayer_User_Customer_MobileDevice_OperatingSystem record."""
        data = self.client.call('SoftLayer_User_Customer_MobileDevice_OperatingSystem', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Customer_MobileDevice_OperatingSystem import User_Customer_MobileDevice_OperatingSystem
        return data
