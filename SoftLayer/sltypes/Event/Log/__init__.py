from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Event_Log(Entity):
    """The SoftLayer_Event_Log data type contains an event detail occurred upon various SoftLayer resources."""
    accountId: int
    eventCreateDate: datetime
    eventName: str
    ipAddress: str
    label: str
    metaData: str
    objectId: int
    objectName: str
    openIdConnectUserName: str
    resource: Entity
    traceId: str
    userId: int
    userType: str
    username: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Event_Log'

    def getAllEventNames(self, objectName: str) -> list[str]:
        """Return all indexed event names."""
        data = self.client.call('SoftLayer_Event_Log', 'getAllEventNames', objectName)
        return data

    def getAllEventObjectNames(self) -> list[str]:
        """Return all indexed event object names."""
        data = self.client.call('SoftLayer_Event_Log', 'getAllEventObjectNames')
        return data

    def getAllObjects(self) -> list['Event_Log']:
        """Return the event log data"""
        data = self.client.call('SoftLayer_Event_Log', 'getAllObjects')
        from SoftLayer.sltypes.Event_Log import Event_Log
        return data

    def getAllUserTypes(self) -> list[str]:
        """Returns all possible event log user types"""
        data = self.client.call('SoftLayer_Event_Log', 'getAllUserTypes')
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Event_Log', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
