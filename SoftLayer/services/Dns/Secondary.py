# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Dns_Secondary(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Dns_Secondary'
        self.client = client

    def convertToPrimary(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'convertToPrimary',
            
        )
        
        return data


    def createObject(
        self,
        templateObject: SoftLayer_Dns_Secondary,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Secondary':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Secondary import Secondary
        return Secondary(data)


    def createObjects(
        self,
        templateObjects: SoftLayer_Dns_Secondary,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Dns_Secondary]':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Secondary import Secondary
        return Secondary(data)


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
        templateObject: SoftLayer_Dns_Secondary
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getByDomainName(
        self,
        name: str,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Dns_Secondary]':

        data = self.client.call(
            self.service,
            'getByDomainName',
            name,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Secondary import Secondary
        return Secondary(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Secondary':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Secondary import Secondary
        return Secondary(data)


    def transferNow(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'transferNow',
            
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


    def getDomain(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain':

        data = self.client.call(
            self.service,
            'getDomain',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return Domain(data)


    def getErrorMessages(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Dns_Message]':

        data = self.client.call(
            self.service,
            'getErrorMessages',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Dns.Message import Message
        return Message(data)


    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Status import Status
        return Status(data)


