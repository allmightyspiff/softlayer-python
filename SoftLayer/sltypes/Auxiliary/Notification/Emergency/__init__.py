from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Auxiliary_Notification_Emergency(Entity):
    """A SoftLayer_Auxiliary_Notification_Emergency data object represents a notification event being broadcast to
the SoftLayer customer base. It is used to provide information regarding outages or current known issues."""
    createDate: datetime
    device: str
    duration: str
    id_: int
    location: str
    message: str
    modifyDate: datetime
    servicesAffected: str
    startDate: datetime
    statusId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Auxiliary_Notification_Emergency'

    def getAllObjects(self) -> list['Auxiliary_Notification_Emergency']:
        """Retrieve all notification events."""
        data = self.client.call('SoftLayer_Auxiliary_Notification_Emergency', 'getAllObjects')
        return data

    def getCurrentNotifications(self) -> list['Auxiliary_Notification_Emergency']:
        """Retrieve current notification events."""
        data = self.client.call('SoftLayer_Auxiliary_Notification_Emergency', 'getCurrentNotifications')
        return data

    def getObject(self, identifier: int) -> 'Auxiliary_Notification_Emergency':
        """Retrieve a SoftLayer_Auxiliary_Notification_Emergency record."""
        data = self.client.call('SoftLayer_Auxiliary_Notification_Emergency', 'getObject', id=identifier)
        return data

    def getSignature(self, identifier: int) -> 'Auxiliary_Notification_Emergency_Signature':
        """"""
        data = self.client.call('SoftLayer_Auxiliary_Notification_Emergency', 'getSignature', id=identifier)
        from SoftLayer.sltypes.Auxiliary_Notification_Emergency_Signature import Auxiliary_Notification_Emergency_Signature
        return data

    def getStatus(self, identifier: int) -> 'Auxiliary_Notification_Emergency_Status':
        """"""
        data = self.client.call('SoftLayer_Auxiliary_Notification_Emergency', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Auxiliary_Notification_Emergency_Status import Auxiliary_Notification_Emergency_Status
        return data
