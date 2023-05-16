# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Dns_Domain(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Dns_Domain'
        self.client = client

    def createARecord(
        self,
        host: str,
        data: str,
        ttl: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_AType':

        data = self.client.call(
            self.service,
            'createARecord',
            host,
            data,
            ttl,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.AType import AType
        return AType(data)


    def createAaaaRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_AaaaType':

        data = self.client.call(
            self.service,
            'createAaaaRecord',
            host,
            data,
            ttl,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.AaaaType import AaaaType
        return AaaaType(data)


    def createCnameRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_CnameType':

        data = self.client.call(
            self.service,
            'createCnameRecord',
            host,
            data,
            ttl,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.CnameType import CnameType
        return CnameType(data)


    def createMxRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        mxPriority: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_MxType':

        data = self.client.call(
            self.service,
            'createMxRecord',
            host,
            data,
            ttl,
            mxPriority,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.MxType import MxType
        return MxType(data)


    def createNsRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_NsType':

        data = self.client.call(
            self.service,
            'createNsRecord',
            host,
            data,
            ttl,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.NsType import NsType
        return NsType(data)


    def createObject(
        self,
        templateObject: 'SoftLayer_Dns_Domain',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return Domain(data)


    def createObjects(
        self,
        templateObjects: 'SoftLayer_Dns_Domain',
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Dns_Domain]':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return Domain(data)


    def createPtrRecord(
        self,
        ipAddress: str,
        ptrRecord: str,
        ttl: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord':

        data = self.client.call(
            self.service,
            'createPtrRecord',
            ipAddress,
            ptrRecord,
            ttl,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord import ResourceRecord
        return ResourceRecord(data)


    def createSpfRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_SpfType':

        data = self.client.call(
            self.service,
            'createSpfRecord',
            host,
            data,
            ttl,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.SpfType import SpfType
        return SpfType(data)


    def createTxtRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_TxtType':

        data = self.client.call(
            self.service,
            'createTxtRecord',
            host,
            data,
            ttl,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.TxtType import TxtType
        return TxtType(data)


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


    def getByDomainName(
        self,
        name: str,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Dns_Domain]':

        data = self.client.call(
            self.service,
            'getByDomainName',
            name,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return Domain(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return Domain(data)


    def getZoneFileContents(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getZoneFileContents',
            id=identifier
        )
        
        return data


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getManagedResourceFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getManagedResourceFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getResourceRecords(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Dns_Domain_ResourceRecord]':

        data = self.client.call(
            self.service,
            'getResourceRecords',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord import ResourceRecord
        return ResourceRecord(data)


    def getSecondary(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Secondary':

        data = self.client.call(
            self.service,
            'getSecondary',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Secondary import Secondary
        return Secondary(data)


    def getSoaResourceRecord(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_SoaType':

        data = self.client.call(
            self.service,
            'getSoaResourceRecord',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.SoaType import SoaType
        return SoaType(data)


