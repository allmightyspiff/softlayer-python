# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_Schedule(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_Schedule'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Network_Storage_Schedule,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Network_Storage_Schedule
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def getDay(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDay',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDayOfMonth(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDayOfMonth',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDayOfWeek(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDayOfWeek',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Event]':

        data = self.client.call(
            self.service,
            'getEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Event import Event
        return Event(data)


    def getHour(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getHour',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMinute(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getMinute',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMonthOfYear(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getMonthOfYear',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPartnership(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Partnership':

        data = self.client.call(
            self.service,
            'getPartnership',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Partnership import Partnership
        return Partnership(data)


    def getProperties(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Schedule_Property]':

        data = self.client.call(
            self.service,
            'getProperties',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Schedule.Property import Property
        return Property(data)


    def getReplicaSnapshots(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getReplicaSnapshots',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getRetentionCount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getRetentionCount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSecond(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSecond',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshots(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getSnapshots',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule.Type import Type
        return Type(data)


    def getVolume(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage':

        data = self.client.call(
            self.service,
            'getVolume',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


