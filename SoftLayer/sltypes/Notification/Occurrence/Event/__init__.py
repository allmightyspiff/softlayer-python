from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Notification_Occurrence_Event(Entity):
    endDate: datetime
    id_: int
    lastImpactedUserCount: int
    modifyDate: datetime
    recoveryTime: int
    startDate: datetime
    subject: str
    summary: str
    systemTicketId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Notification_Occurrence_Event'

    def acknowledgeNotification(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'acknowledgeNotification', id=identifier)
        return data

    def getAllObjects(self) -> list['Notification_Occurrence_Event']:
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getAllObjects')
        return data

    def getAttachedFile(self, identifier: int, attachmentId: int) -> str:
        """Retrieve a file attached to an event."""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getAttachedFile', attachmentId, id=identifier)
        return data

    def getImpactedAccountCount(self, identifier: int) -> int:
        """Get the number of impacted owned accounts for the current user."""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getImpactedAccountCount', id=identifier)
        return data

    def getImpactedDeviceCount(self, identifier: int) -> int:
        """Get the number of impacted devices."""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getImpactedDeviceCount', id=identifier)
        return data

    def getImpactedDevices(self, identifier: int) -> list['Notification_Occurrence_Resource']:
        """Get devices impacted by this event"""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getImpactedDevices', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Resource import Notification_Occurrence_Resource
        return data

    def getObject(self, identifier: int) -> 'Notification_Occurrence_Event':
        """Retrieve a SoftLayer_Notification_Occurrence_Event record."""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getObject', id=identifier)
        return data

    def getAcknowledgedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getAcknowledgedFlag', id=identifier)
        return data

    def getAttachments(self, identifier: int) -> list['Notification_Occurrence_Event_Attachment']:
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getAttachments', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Event_Attachment import Notification_Occurrence_Event_Attachment
        return data

    def getFirstUpdate(self, identifier: int) -> 'Notification_Occurrence_Update':
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getFirstUpdate', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Update import Notification_Occurrence_Update
        return data

    def getImpactedAccounts(self, identifier: int) -> list['Notification_Occurrence_Account']:
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getImpactedAccounts', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Account import Notification_Occurrence_Account
        return data

    def getImpactedResources(self, identifier: int) -> list['Notification_Occurrence_Resource']:
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getImpactedResources', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Resource import Notification_Occurrence_Resource
        return data

    def getImpactedUsers(self, identifier: int) -> list['Notification_Occurrence_User']:
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getImpactedUsers', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_User import Notification_Occurrence_User
        return data

    def getLastUpdate(self, identifier: int) -> 'Notification_Occurrence_Update':
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getLastUpdate', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Update import Notification_Occurrence_Update
        return data

    def getNotificationOccurrenceEventType(self, identifier: int) -> 'Notification_Occurrence_Event_Type':
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getNotificationOccurrenceEventType', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Event_Type import Notification_Occurrence_Event_Type
        return data

    def getStatusCode(self, identifier: int) -> 'Notification_Occurrence_Status_Code':
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getStatusCode', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Status_Code import Notification_Occurrence_Status_Code
        return data

    def getUpdates(self, identifier: int) -> list['Notification_Occurrence_Update']:
        """"""
        data = self.client.call('SoftLayer_Notification_Occurrence_Event', 'getUpdates', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Update import Notification_Occurrence_Update
        return data
