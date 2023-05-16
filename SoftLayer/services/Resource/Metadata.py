# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Resource_Metadata(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Resource_Metadata'
        self.client = client

    def getAccountId(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getAccountId',
            
        )
        
        return data


    def getBackendMacAddresses(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getBackendMacAddresses',
            
        )
        
        return data


    def getDatacenter(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDatacenter',
            
        )
        
        return data


    def getDatacenterId(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getDatacenterId',
            
        )
        
        return data


    def getDomain(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDomain',
            
        )
        
        return data


    def getFrontendMacAddresses(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getFrontendMacAddresses',
            
        )
        
        return data


    def getFullyQualifiedDomainName(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFullyQualifiedDomainName',
            
        )
        
        return data


    def getGlobalIdentifier(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getGlobalIdentifier',
            
        )
        
        return data


    def getHostname(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getHostname',
            
        )
        
        return data


    def getId(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getId',
            
        )
        
        return data


    def getPrimaryBackendIpAddress(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPrimaryBackendIpAddress',
            
        )
        
        return data


    def getPrimaryIpAddress(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPrimaryIpAddress',
            
        )
        
        return data


    def getProvisionState(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getProvisionState',
            
        )
        
        return data


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


    def getServiceResources(
        self,
        
    ) -> 'list[SoftLayer_Container_Resource_Metadata_ServiceResource]':

        data = self.client.call(
            self.service,
            'getServiceResources',
            
        )
        from SoftLayer.datatypes.Container.Resource.Metadata.ServiceResource import ServiceResource
        return ServiceResource(data)


    def getTags(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getTags',
            
        )
        
        return data


    def getUserMetadata(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getUserMetadata',
            
        )
        
        return data


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


