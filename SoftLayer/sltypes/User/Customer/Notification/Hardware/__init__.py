from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_Notification_Hardware(Entity):
    """The Customer_Notification_Hardware object stores links between customers and the hardware devices they wish
to monitor.  This link is not enough, the user must be sure to also create
SoftLayer_Network_Monitor_Version1_Query_Host instance with the response action set to "notify users" in
order for the users linked to that hardware object to be notified on failure."""
    hardwareId: int
    id_: int
    userId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_Notification_Hardware'

    def createObject(self, templateObject: 'User_Customer_Notification_Hardware') -> 'User_Customer_Notification_Hardware':
        """Create a user hardware notification entry"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Hardware', 'createObject', templateObject)
        return data

    def createObjects(self, templateObjects: 'User_Customer_Notification_Hardware') -> list['User_Customer_Notification_Hardware']:
        """Create multiple user hardware notification entries at once"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Hardware', 'createObjects', templateObjects)
        return data

    def deleteObjects(self, templateObjects: 'User_Customer_Notification_Hardware') -> bool:
        """Delete a group of Customer_Notification_Hardware objects by passing in a collection of them"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Hardware', 'deleteObjects', templateObjects)
        return data

    def findByHardwareId(self, hardwareId: int) -> list['User_Customer_Notification_Hardware']:
        """Return all hardware notifications associated with the passed hardware ID"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Hardware', 'findByHardwareId', hardwareId)
        return data

    def getObject(self, identifier: int) -> 'User_Customer_Notification_Hardware':
        """Retrieve a SoftLayer_User_Customer_Notification_Hardware record."""
        data = self.client.call('SoftLayer_User_Customer_Notification_Hardware', 'getObject', id=identifier)
        return data

    def getHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Hardware', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Hardware', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
