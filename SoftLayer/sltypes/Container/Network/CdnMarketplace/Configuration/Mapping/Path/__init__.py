from SoftLayer.sltypes.Container.Network.CdnMarketplace.Configuration.Performance.DynamicContentAcceleration import Container_Network_CdnMarketplace_Configuration_Performance_DynamicContentAcceleration
from SoftLayer.sltypes.Entity import Entity

class Container_Network_CdnMarketplace_Configuration_Mapping_Path(Entity):
    bucketName: str
    cacheKeyQueryRule: str
    dynamicContentAcceleration: Container_Network_CdnMarketplace_Configuration_Performance_DynamicContentAcceleration
    fileExtension: str
    header: str
    httpPort: int
    httpsPort: int
    mappingUniqueId: str
    origin: str
    originType: str
    path: str
    performanceConfiguration: str
    status: str
