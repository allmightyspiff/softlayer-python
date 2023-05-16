# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Resource_Metadata(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Resource_Metadata'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAccountId(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getAccountId',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getBackendMacAddresses(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getBackendMacAddresses',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDatacenter(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getDatacenter',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDatacenterId(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getDatacenterId',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDomain(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getDomain',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getFrontendMacAddresses(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getFrontendMacAddresses',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getFullyQualifiedDomainName(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getFullyQualifiedDomainName',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getGlobalIdentifier(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getGlobalIdentifier',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getHostname(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getHostname',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getId(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getId',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPrimaryBackendIpAddress(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPrimaryBackendIpAddress',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPrimaryIpAddress(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPrimaryIpAddress',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getProvisionState(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getProvisionState',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getRouter(
        self,
        macAddress: str
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getRouter',
            macAddress
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getServiceResource(
        self,
        serviceName: str,
        index: int
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getServiceResource',
            serviceName,
            index
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getServiceResources(
        self,
        
    ) -> 'list[SoftLayer_Container_Resource_Metadata_ServiceResource]':
        data = self.client.call(
            self.service,
            'getServiceResources',
            
        )
        from SoftLayer.datatypes.Container.Resource.Metadata.ServiceResource import ServiceResource
        return SL_ServiceResource(data)

# This file was automatically generated with tools/generateTypes.py
    def getTags(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getTags',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getUserMetadata(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getUserMetadata',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getVlanIds(
        self,
        macAddress: str
    ) -> 'list[int]':
        data = self.client.call(
            self.service,
            'getVlanIds',
            macAddress
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getVlans(
        self,
        macAddress: str
    ) -> 'list[int]':
        data = self.client.call(
            self.service,
            'getVlans',
            macAddress
        )
        
        return data


