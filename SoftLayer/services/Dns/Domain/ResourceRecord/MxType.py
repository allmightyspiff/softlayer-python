# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Dns_Domain_ResourceRecord_MxType(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Dns_Domain_ResourceRecord_MxType'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Dns_Domain_ResourceRecord_MxType,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_MxType':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.MxType import MxType
        return SL_MxType(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_ResourceRecord(data)

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
    def deleteObjects(
        self,
        templateObjects: SoftLayer_Dns_Domain_ResourceRecord_MxType
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteObjects',
            templateObjects
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Dns_Domain_ResourceRecord_MxType
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editObjects(
        self,
        templateObjects: SoftLayer_Dns_Domain_ResourceRecord_MxType
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObjects',
            templateObjects
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_ResourceRecord_MxType':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.ResourceRecord.MxType import MxType
        return SL_MxType(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Domain(data)


