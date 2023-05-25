from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_MobileDevice(Entity):
    """This class represents a mobile device belonging to a user.  The device can be a phone, tablet, or possibly
even some Android based net books.  The purpose is to tie just enough info with the device and the user to
enable push notifications through non-softlayer entities (Google, Apple, RIM)."""
    createDate: datetime
    displayResolutionXxY: str
    id_: int
    mobileDeviceTypeId: int
    mobileOperatingSystemId: int
    modelNumber: str
    modifyDate: datetime
    name: str
    phoneNumber: str
    serialNumber: str
    token: str
    userId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_MobileDevice'

    def createObject(self, templateObject: 'User_Customer_MobileDevice') -> 'User_Customer_MobileDevice':
        """Create a new mobile device association for a user."""
        data = self.client.call('SoftLayer_User_Customer_MobileDevice', 'createObject', templateObject)
        from SoftLayer.sltypes.User_Customer_MobileDevice import User_Customer_MobileDevice
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a mobile device association for a user."""
        data = self.client.call('SoftLayer_User_Customer_MobileDevice', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'User_Customer_MobileDevice') -> bool:
        """Edit the object by passing in a modified instance of the object."""
        data = self.client.call('SoftLayer_User_Customer_MobileDevice', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'User_Customer_MobileDevice':
        """Retrieve a SoftLayer_User_Customer_MobileDevice record."""
        data = self.client.call('SoftLayer_User_Customer_MobileDevice', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Customer_MobileDevice import User_Customer_MobileDevice
        return data

    def getAvailablePushNotificationSubscriptions(self, identifier: int) -> list['Notification']:
        """"""
        data = self.client.call('SoftLayer_User_Customer_MobileDevice', 'getAvailablePushNotificationSubscriptions', id=identifier)
        from SoftLayer.sltypes.Notification import Notification
        return data

    def getCustomer(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_User_Customer_MobileDevice', 'getCustomer', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getOperatingSystem(self, identifier: int) -> 'User_Customer_MobileDevice_OperatingSystem':
        """"""
        data = self.client.call('SoftLayer_User_Customer_MobileDevice', 'getOperatingSystem', id=identifier)
        from SoftLayer.sltypes.User_Customer_MobileDevice_OperatingSystem import User_Customer_MobileDevice_OperatingSystem
        return data

    def getPushNotificationSubscriptions(self, identifier: int) -> list['Notification_User_Subscriber']:
        """"""
        data = self.client.call('SoftLayer_User_Customer_MobileDevice', 'getPushNotificationSubscriptions', id=identifier)
        from SoftLayer.sltypes.Notification_User_Subscriber import Notification_User_Subscriber
        return data

    def getType(self, identifier: int) -> 'User_Customer_MobileDevice_Type':
        """"""
        data = self.client.call('SoftLayer_User_Customer_MobileDevice', 'getType', id=identifier)
        from SoftLayer.sltypes.User_Customer_MobileDevice_Type import User_Customer_MobileDevice_Type
        return data
