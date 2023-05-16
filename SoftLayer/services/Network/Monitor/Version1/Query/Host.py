# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Monitor_Version1_Query_Host(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Monitor_Version1_Query_Host'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Network_Monitor_Version1_Query_Host,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Monitor_Version1_Query_Host':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Host import Host
        return Host(data)


    def createObjects(
        self,
        templateObjects: SoftLayer_Network_Monitor_Version1_Query_Host,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Query_Host]':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Host import Host
        return Host(data)


    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def deleteObjects(
        self,
        templateObjects: SoftLayer_Network_Monitor_Version1_Query_Host
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObjects',
            templateObjects
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Network_Monitor_Version1_Query_Host
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def editObjects(
        self,
        templateObjects: SoftLayer_Network_Monitor_Version1_Query_Host
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObjects',
            templateObjects
        )
        
        return data


    def findByHardwareId(
        self,
        hardwareId: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Query_Host]':

        data = self.client.call(
            self.service,
            'findByHardwareId',
            hardwareId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Host import Host
        return Host(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Monitor_Version1_Query_Host':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Host import Host
        return Host(data)


    def getHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getHardware',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getLastResult(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Monitor_Version1_Query_Result':

        data = self.client.call(
            self.service,
            'getLastResult',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Result import Result
        return Result(data)


    def getQueryType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Monitor_Version1_Query_Type':

        data = self.client.call(
            self.service,
            'getQueryType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Type import Type
        return Type(data)


    def getResponseAction(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Monitor_Version1_Query_ResponseType':

        data = self.client.call(
            self.service,
            'getResponseAction',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.ResponseType import ResponseType
        return ResponseType(data)


