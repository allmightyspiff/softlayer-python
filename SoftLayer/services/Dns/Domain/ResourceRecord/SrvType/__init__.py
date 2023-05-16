# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Dns_Domain_ResourceRecord_SrvType(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Dns_Domain_ResourceRecord_SrvType'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Dns_Domain_ResourceRecord_SrvType',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_SrvType':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.SrvType import SrvType
        return SrvType(data)


    def createObjects(
        self,
        templateObjects: 'SoftLayer_Dns_Domain_ResourceRecord',
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
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            id=identifier
        )
        
        return data


    def deleteObjects(
        self,
        templateObjects: 'SoftLayer_Dns_Domain_ResourceRecord_SrvType'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObjects',
            templateObjects
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_Dns_Domain_ResourceRecord_SrvType',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def editObjects(
        self,
        templateObjects: 'SoftLayer_Dns_Domain_ResourceRecord_SrvType'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObjects',
            templateObjects
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_SrvType':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.SrvType import SrvType
        return SrvType(data)


    def getDomain(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain':

        data = self.client.call(
            self.service,
            'getDomain',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return Domain(data)


