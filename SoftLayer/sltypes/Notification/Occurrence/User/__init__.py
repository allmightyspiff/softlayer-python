from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Notification_Occurrence_User(Entity):
    """This type contains general information relating to a user that may be impacted by a
[[SoftLayer_Notification_Occurrence_Event]]."""
    acknowledgedFlag: int
    active: int
    id_: int
    usrRecordId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Notification_Occurrence_User'

    def acknowledge(self, identifier: int) -> bool:
        """Acknowledge the associated [[SoftLayer_Notification_Occurrence_Event]] for this impacted user."""
        data = self.client.call('SoftLayer_Notification_Occurrence_User', 'acknowledge', id=identifier)
        return data

    def getAllObjects(self) -> list['Notification_Occurrence_User']:
        """Returns a collection of impacted users, an account master user has the ability to see all impacted users
under the account."""
        data = self.client.call('SoftLayer_Notification_Occurrence_User', 'getAllObjects')
        return data

    def getImpactedDeviceCount(self, identifier: int) -> int:
        """A count representing the number of the user's devices currently impacted by the associated event will be
returned."""
        data = self.client.call('SoftLayer_Notification_Occurrence_User', 'getImpactedDeviceCount', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Notification_Occurrence_User':
        """Retrieve a SoftLayer_Notification_Occurrence_User record."""
        data = self.client.call('SoftLayer_Notification_Occurrence_User', 'getObject', id=identifier)
        return data

    def getImpactedResources(self, identifier: int) -> list['Notification_Occurrence_Resource']:
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_User', 'getImpactedResources', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Resource import Notification_Occurrence_Resource
        return data

    def getNotificationOccurrenceEvent(self, identifier: int) -> 'Notification_Occurrence_Event':
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_User', 'getNotificationOccurrenceEvent', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Event import Notification_Occurrence_Event
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_User', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
