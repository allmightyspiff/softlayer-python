# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Dns_Domain(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Dns_Domain'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createARecord(
        self,
        host: str,
        data: str,
        ttl: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_AType':
        data = self.client.call(
            self.service,
            'createARecord',
            host,
            data,
            ttl,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.AType import AType
        return SL_AType(data)

# This file was automatically generated with tools/generateTypes.py
    def createAaaaRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_AaaaType':
        data = self.client.call(
            self.service,
            'createAaaaRecord',
            host,
            data,
            ttl,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.AaaaType import AaaaType
        return SL_AaaaType(data)

# This file was automatically generated with tools/generateTypes.py
    def createCnameRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_CnameType':
        data = self.client.call(
            self.service,
            'createCnameRecord',
            host,
            data,
            ttl,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.CnameType import CnameType
        return SL_CnameType(data)

# This file was automatically generated with tools/generateTypes.py
    def createMxRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        mxPriority: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_MxType':
        data = self.client.call(
            self.service,
            'createMxRecord',
            host,
            data,
            ttl,
            mxPriority,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.MxType import MxType
        return SL_MxType(data)

# This file was automatically generated with tools/generateTypes.py
    def createNsRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_NsType':
        data = self.client.call(
            self.service,
            'createNsRecord',
            host,
            data,
            ttl,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.NsType import NsType
        return SL_NsType(data)

# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Dns_Domain,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return SL_Domain(data)

# This file was automatically generated with tools/generateTypes.py
    def createObjects(
        self,
        templateObjects: SoftLayer_Dns_Domain,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Dns_Domain]':
        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return SL_Domain(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_ResourceRecord(data)

# This file was automatically generated with tools/generateTypes.py
    def createSpfRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_SpfType':
        data = self.client.call(
            self.service,
            'createSpfRecord',
            host,
            data,
            ttl,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.SpfType import SpfType
        return SL_SpfType(data)

# This file was automatically generated with tools/generateTypes.py
    def createTxtRecord(
        self,
        host: str,
        data: str,
        ttl: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_TxtType':
        data = self.client.call(
            self.service,
            'createTxtRecord',
            host,
            data,
            ttl,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.TxtType import TxtType
        return SL_TxtType(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteObject(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Domain(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return SL_Domain(data)

# This file was automatically generated with tools/generateTypes.py
    def getZoneFileContents(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getZoneFileContents',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getManagedResourceFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getManagedResourceFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getResourceRecords(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Dns_Domain_ResourceRecord]':
        data = self.client.call(
            self.service,
            'getResourceRecords',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord import ResourceRecord
        return SL_ResourceRecord(data)

# This file was automatically generated with tools/generateTypes.py
    def getSecondary(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Secondary':
        data = self.client.call(
            self.service,
            'getSecondary',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Secondary import Secondary
        return SL_Secondary(data)

# This file was automatically generated with tools/generateTypes.py
    def getSoaResourceRecord(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_SoaType':
        data = self.client.call(
            self.service,
            'getSoaResourceRecord',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.SoaType import SoaType
        return SL_SoaType(data)


