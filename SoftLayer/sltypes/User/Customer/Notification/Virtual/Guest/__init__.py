from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_Notification_Virtual_Guest(Entity):
    """The SoftLayer_User_Customer_Notification_Virtual_Guest object stores links between customers and the virtual
guests they wish to monitor.  This link is not enough, the user must be sure to also create
SoftLayer_Network_Monitor_Version1_Query_Host instance with the response action set to "notify users" in
order for the users linked to that Virtual Guest object to be notified on failure."""
    guestId: int
    id_: int
    userId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_Notification_Virtual_Guest'

    def createObject(self, templateObject: 'User_Customer_Notification_Virtual_Guest') -> 'User_Customer_Notification_Virtual_Guest':
        """Create a user virtual guest notification entry"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Virtual_Guest', 'createObject', templateObject)
        return data

    def createObjects(self, templateObjects: 'User_Customer_Notification_Virtual_Guest') -> list['User_Customer_Notification_Virtual_Guest']:
        """Create multiple user Virtual Guest notification entries at once"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Virtual_Guest', 'createObjects', templateObjects)
        return data

    def deleteObjects(self, templateObjects: 'User_Customer_Notification_Virtual_Guest') -> bool:
        """Delete a group of SoftLayer_Customer_Notification_Virtual_Guest objects by passing in a collection of them"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Virtual_Guest', 'deleteObjects', templateObjects)
        return data

    def findByGuestId(self, id_: int) -> list['User_Customer_Notification_Virtual_Guest']:
        """Return all CloudLayer computing instance notifications associated with the passed ID"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Virtual_Guest', 'findByGuestId', id)
        return data

    def getObject(self, identifier: int) -> 'User_Customer_Notification_Virtual_Guest':
        """Retrieve a SoftLayer_User_Customer_Notification_Virtual_Guest record."""
        data = self.client.call('SoftLayer_User_Customer_Notification_Virtual_Guest', 'getObject', id=identifier)
        return data

    def getGuest(self, identifier: int) -> 'Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Virtual_Guest', 'getGuest', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_User_Customer_Notification_Virtual_Guest', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
