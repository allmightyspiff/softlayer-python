from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_Schedule(Entity):
    """Schedules can be created for select Storage services, such as iscsi. These schedules are used to perform
various tasks such as scheduling snapshots or synchronizing replicants."""
    active: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    name: str
    partnershipId: int
    typeId: int
    volumeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Schedule'

    def createObject(self, templateObject: 'Network_Storage_Schedule') -> 'Network_Storage_Schedule':
        """Create a nas volume schedule"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a network storage schedule"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Storage_Schedule') -> bool:
        """Edit a nas volume schedule"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_Schedule':
        """Retrieve a SoftLayer_Network_Storage_Schedule record."""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getObject', id=identifier)
        return data

    def getDay(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getDay', id=identifier)
        return data

    def getDayOfMonth(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getDayOfMonth', id=identifier)
        return data

    def getDayOfWeek(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getDayOfWeek', id=identifier)
        return data

    def getEvents(self, identifier: int) -> list['Network_Storage_Event']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getEvents', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Event import Network_Storage_Event
        return data

    def getHour(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getHour', id=identifier)
        return data

    def getMinute(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getMinute', id=identifier)
        return data

    def getMonthOfYear(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getMonthOfYear', id=identifier)
        return data

    def getPartnership(self, identifier: int) -> 'Network_Storage_Partnership':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getPartnership', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Partnership import Network_Storage_Partnership
        return data

    def getProperties(self, identifier: int) -> list['Network_Storage_Schedule_Property']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getProperties', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Schedule_Property import Network_Storage_Schedule_Property
        return data

    def getReplicaSnapshots(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getReplicaSnapshots', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getRetentionCount(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getRetentionCount', id=identifier)
        return data

    def getSecond(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getSecond', id=identifier)
        return data

    def getSnapshots(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getSnapshots', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getType(self, identifier: int) -> 'Network_Storage_Schedule_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getType', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Schedule_Type import Network_Storage_Schedule_Type
        return data

    def getVolume(self, identifier: int) -> 'Network_Storage':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Schedule', 'getVolume', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data
