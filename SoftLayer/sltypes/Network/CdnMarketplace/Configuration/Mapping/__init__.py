from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Configuration_Mapping(Entity):
    """This data type represents the mapping Configuration settings for enabling CDN services. Each instance
contains a reference to a CDN account, and CDN configuration properties such as a domain, an origin host and
its port, a cname we generate, a cname the vendor generates, and a status. Other properties include the type
of content to be cached (static or dynamic), the origin type (a host server or an object storage account),
and the protocol to be used for caching."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Configuration_Mapping'

    def createDomainMapping(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> list['Container_Network_CdnMarketplace_Configuration_Mapping']:
        """SOAP API will create a new CDN domain mapping for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping', 'createDomainMapping', input)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping import Container_Network_CdnMarketplace_Configuration_Mapping
        return data

    def deleteDomainMapping(self, uniqueId: str) -> list['Container_Network_CdnMarketplace_Configuration_Mapping']:
        """SOAP API will delete CDN domain mapping for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping', 'deleteDomainMapping', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping import Container_Network_CdnMarketplace_Configuration_Mapping
        return data

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Configuration_Mapping':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Mapping record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping', 'getObject', id=identifier)
        return data

    def listDomainMappingByUniqueId(self, uniqueId: str) -> list['Container_Network_CdnMarketplace_Configuration_Mapping']:
        """SOAP API will return the domain mapping based on the uniqueId."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping', 'listDomainMappingByUniqueId', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping import Container_Network_CdnMarketplace_Configuration_Mapping
        return data

    def listDomainMappings(self) -> list['Container_Network_CdnMarketplace_Configuration_Mapping']:
        """SOAP API will return all domains for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping', 'listDomainMappings')
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping import Container_Network_CdnMarketplace_Configuration_Mapping
        return data

    def retryHttpsActionRequest(self, uniqueId: str) -> list['Container_Network_CdnMarketplace_Configuration_Mapping']:
        """For specific mappings in HTTPS-related error states, this SOAP API will determine whether it needs to re-
attempt an enable or disable HTTPS."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping', 'retryHttpsActionRequest', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping import Container_Network_CdnMarketplace_Configuration_Mapping
        return data

    def startDomainMapping(self, uniqueId: str) -> list['Container_Network_CdnMarketplace_Configuration_Mapping']:
        """SOAP API will start CDN domain mapping for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping', 'startDomainMapping', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping import Container_Network_CdnMarketplace_Configuration_Mapping
        return data

    def stopDomainMapping(self, uniqueId: str) -> list['Container_Network_CdnMarketplace_Configuration_Mapping']:
        """SOAP API will stop CDN mapping for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping', 'stopDomainMapping', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping import Container_Network_CdnMarketplace_Configuration_Mapping
        return data

    def updateDomainMapping(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> list['Container_Network_CdnMarketplace_Configuration_Mapping']:
        """SOAP API will update the Domain Mapping identified by the Unique Id. Following fields are allowed to be
changed: originHost, HttpPort/HttpsPort, RespectHeaders, ServeStale   Additionally, bucketName and
fileExtension if OriginType is Object Store"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping', 'updateDomainMapping', input)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping import Container_Network_CdnMarketplace_Configuration_Mapping
        return data

    def verifyCname(self, cname: str) -> bool:
        """This method will verify the CNAME given is unique."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping', 'verifyCname', cname)
        return data

    def verifyDomainMapping(self, uniqueId: int) -> list['Container_Network_CdnMarketplace_Configuration_Mapping']:
        """This method will verify the status of a domain mapping"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping', 'verifyDomainMapping', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping import Container_Network_CdnMarketplace_Configuration_Mapping
        return data
