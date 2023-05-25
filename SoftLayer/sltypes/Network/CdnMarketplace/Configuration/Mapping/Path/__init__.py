from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Configuration_Mapping_Path(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path'

    def createOriginPath(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> list['Container_Network_CdnMarketplace_Configuration_Mapping_Path']:
        """SOAP API will create Origin Path for an existing CDN mapping and for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path', 'createOriginPath', input)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping_Path import Container_Network_CdnMarketplace_Configuration_Mapping_Path
        return data

    def deleteOriginPath(self, uniqueId: str, path: str) -> str:
        """SOAP API will delete Origin Path for an existing mapping and for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path', 'deleteOriginPath', uniqueId, path)
        return data

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Configuration_Mapping_Path':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path', 'getObject', id=identifier)
        return data

    def listOriginPath(self, uniqueId: str) -> list['Container_Network_CdnMarketplace_Configuration_Mapping_Path']:
        """SOAP API will list origin path for an existing mapping and for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path', 'listOriginPath', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping_Path import Container_Network_CdnMarketplace_Configuration_Mapping_Path
        return data

    def updateOriginPath(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> list['Container_Network_CdnMarketplace_Configuration_Mapping_Path']:
        """SOAP API will update Origin Path for an existing mapping and for a particular customer.   When passing the
$input object as a parameter, it will expect the following properties to be set: $oldPath $uniqueId
$originType, $path, $origin, $httpPort, $httpsPort, and if the path's origin type is object storage, the
$bucketName and the $fileExtension.   Out of the properties listed above only the following path properties
are allowed to be changed: $path, $origin, $httpPort, $httpsPort These properties may not be changed:
$originType"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path', 'updateOriginPath', input)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Mapping_Path import Container_Network_CdnMarketplace_Configuration_Mapping_Path
        return data
