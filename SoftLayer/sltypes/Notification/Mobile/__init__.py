from SoftLayer.sltypes.Notification import Notification
from SoftLayer import BaseClient

class Notification_Mobile(Notification):
    """This is an extension of the SoftLayer_Notification class.  These are implementation details specific to those
notifications which can be subscribed to and received on a mobile device."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Notification_Mobile'

    def createSubscriberForMobileDevice(self, keyName: str, resourceTableId: int, userRecordId: int) -> bool:
        """Create a new subscriber for a given resource."""
        data = self.client.call('SoftLayer_Notification_Mobile', 'createSubscriberForMobileDevice', keyName, resourceTableId, userRecordId)
        return data

    def getObject(self, identifier: int) -> 'Notification_Mobile':
        """Retrieve a SoftLayer_Notification_Mobile record."""
        data = self.client.call('SoftLayer_Notification_Mobile', 'getObject', id=identifier)
        return data
