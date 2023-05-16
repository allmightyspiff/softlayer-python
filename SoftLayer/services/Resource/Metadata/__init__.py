# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Resource_Metadata(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Resource_Metadata'
        self.client = client

    def getAccountId(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getAccountId',
            id=identifier
        )
        
        return data


    def getBackendMacAddresses(
        self,
        identifier: int
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getBackendMacAddresses',
            id=identifier
        )
        
        return data


    def getDatacenter(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDatacenter',
            id=identifier
        )
        
        return data


    def getDatacenterId(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getDatacenterId',
            id=identifier
        )
        
        return data


    def getDomain(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDomain',
            id=identifier
        )
        
        return data


    def getFrontendMacAddresses(
        self,
        identifier: int
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getFrontendMacAddresses',
            id=identifier
        )
        
        return data


    def getFullyQualifiedDomainName(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFullyQualifiedDomainName',
            id=identifier
        )
        
        return data


    def getGlobalIdentifier(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getGlobalIdentifier',
            id=identifier
        )
        
        return data


    def getHostname(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getHostname',
            id=identifier
        )
        
        return data


    def getId(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getId',
            id=identifier
        )
        
        return data


    def getPrimaryBackendIpAddress(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPrimaryBackendIpAddress',
            id=identifier
        )
        
        return data


    def getPrimaryIpAddress(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPrimaryIpAddress',
            id=identifier
        )
        
        return data


    def getProvisionState(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getProvisionState',
            id=identifier
        )
        
        return data


    def getRouter(
        self,
        macAddress: str,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getRouter',
            macAddress,
            id=identifier
        )
        
        return data


    def getServiceResource(
        self,
        serviceName: str,
        index: int,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getServiceResource',
            serviceName,
            index,
            id=identifier
        )
        
        return data


    def getServiceResources(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Resource_Metadata_ServiceResource]':

        data = self.client.call(
            self.service,
            'getServiceResources',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Resource.Metadata.ServiceResource import ServiceResource
        return ServiceResource(data)


    def getTags(
        self,
        identifier: int
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getTags',
            id=identifier
        )
        
        return data


    def getUserMetadata(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getUserMetadata',
            id=identifier
        )
        
        return data


    def getVlanIds(
        self,
        macAddress: str,
        identifier: int
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getVlanIds',
            macAddress,
            id=identifier
        )
        
        return data


    def getVlans(
        self,
        macAddress: str,
        identifier: int
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getVlans',
            macAddress,
            id=identifier
        )
        
        return data


