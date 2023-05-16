# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Security_Scanner_Request(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Security_Scanner_Request'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Network_Security_Scanner_Request,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Security_Scanner_Request':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Security.Scanner.Request import Request
        return Request(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Security_Scanner_Request':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Security.Scanner.Request import Request
        return Request(data)


    def getReport(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getReport',
            
        )
        
        return data


    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getGuest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getGuest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


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


    def getRequestorOwnedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getRequestorOwnedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Security_Scanner_Request_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Security.Scanner.Request.Status import Status
        return Status(data)


