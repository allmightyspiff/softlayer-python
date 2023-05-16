# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Dns_Domain_ResourceRecord(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Dns_Domain_ResourceRecord'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Dns_Domain_ResourceRecord,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord import ResourceRecord
        return ResourceRecord(data)


    def createObjects(
        self,
        templateObjects: SoftLayer_Dns_Domain_ResourceRecord,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Dns_Domain_ResourceRecord]':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord import ResourceRecord
        return ResourceRecord(data)


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
        templateObjects: SoftLayer_Dns_Domain_ResourceRecord
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObjects',
            templateObjects
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Dns_Domain_ResourceRecord
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def editObjects(
        self,
        templateObjects: SoftLayer_Dns_Domain_ResourceRecord
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObjects',
            templateObjects
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord import ResourceRecord
        return ResourceRecord(data)


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


