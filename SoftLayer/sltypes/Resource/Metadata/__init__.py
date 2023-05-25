from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Resource_Metadata(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Resource_Metadata'

    def getAccountId(self, identifier: int) -> int:
        """The id for the account which the resource is in"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getAccountId', id=identifier)
        return data

    def getBackendMacAddresses(self, identifier: int) -> list[str]:
        """A list of backend MAC addresses"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getBackendMacAddresses', id=identifier)
        return data

    def getDatacenter(self, identifier: int) -> str:
        """The name for the datacenter which the resource is in"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getDatacenter', id=identifier)
        return data

    def getDatacenterId(self, identifier: int) -> int:
        """The id for the datacenter which the resource is in"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getDatacenterId', id=identifier)
        return data

    def getDomain(self, identifier: int) -> str:
        """A resource's domain"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getDomain', id=identifier)
        return data

    def getFrontendMacAddresses(self, identifier: int) -> list[str]:
        """A list of frontend MAC addresses"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getFrontendMacAddresses', id=identifier)
        return data

    def getFullyQualifiedDomainName(self, identifier: int) -> str:
        """A resource's fully qualified domain name"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getFullyQualifiedDomainName', id=identifier)
        return data

    def getGlobalIdentifier(self, identifier: int) -> str:
        """A resource's globalIdentifier"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getGlobalIdentifier', id=identifier)
        return data

    def getHostname(self, identifier: int) -> str:
        """A resource's hostname"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getHostname', id=identifier)
        return data

    def getId(self, identifier: int) -> int:
        """A resource's id"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getId', id=identifier)
        return data

    def getPrimaryBackendIpAddress(self, identifier: int) -> str:
        """The primary backend IP address for the resource"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getPrimaryBackendIpAddress', id=identifier)
        return data

    def getPrimaryIpAddress(self, identifier: int) -> str:
        """The primary IP address for the resource"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getPrimaryIpAddress', id=identifier)
        return data

    def getProvisionState(self, identifier: int) -> str:
        """Obtain the provision state for a resource"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getProvisionState', id=identifier)
        return data

    def getRouter(self, identifier: int, macAddress: str) -> str:
        """The router associated with a network component"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getRouter', macAddress, id=identifier)
        return data

    def getServiceResource(self, identifier: int, serviceName: str, index: int) -> str:
        """Obtain a specific service resource associated with the resource"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getServiceResource', serviceName, index, id=identifier)
        return data

    def getServiceResources(self, identifier: int) -> list['Container_Resource_Metadata_ServiceResource']:
        """Obtain service resources associated with the resource"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getServiceResources', id=identifier)
        from SoftLayer.sltypes.Container_Resource_Metadata_ServiceResource import Container_Resource_Metadata_ServiceResource
        return data

    def getTags(self, identifier: int) -> list[str]:
        """Obtain tags associated with the resource"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getTags', id=identifier)
        return data

    def getUserMetadata(self, identifier: int) -> str:
        """Obtain user data associated with the resource"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getUserMetadata', id=identifier)
        return data

    def getVlanIds(self, identifier: int, macAddress: str) -> list[int]:
        """A list of VLAN ids for a network component"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getVlanIds', macAddress, id=identifier)
        return data

    def getVlans(self, identifier: int, macAddress: str) -> list[int]:
        """A list of VLAN numbers for a network component"""
        data = self.client.call('SoftLayer_Resource_Metadata', 'getVlans', macAddress, id=identifier)
        return data
