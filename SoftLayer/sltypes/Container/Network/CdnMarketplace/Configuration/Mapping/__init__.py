from SoftLayer.sltypes.Container.Network.CdnMarketplace.Configuration.Performance.DynamicContentAcceleration import Container_Network_CdnMarketplace_Configuration_Performance_DynamicContentAcceleration
from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Network_CdnMarketplace_Configuration_Mapping(Entity):
    akamaiCname: str
    bucketName: str
    cacheKeyQueryRule: str
    certificateType: str
    cname: str
    createDate: datetime
    domain: str
    dynamicContentAcceleration: Container_Network_CdnMarketplace_Configuration_Performance_DynamicContentAcceleration
    fileExtension: str
    header: str
    httpPort: int
    httpsChallengeRedirectUrl: str
    httpsChallengeResponse: str
    httpsChallengeUrl: str
    httpsPort: int
    modifyDate: datetime
    originHost: str
    originType: str
    path: str
    performanceConfiguration: str
    protocol: str
    respectHeaders: bool
    serveStale: bool
    status: str
    uniqueId: str
    vendorName: str
