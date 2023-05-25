from SoftLayer.sltypes.Network.CdnMarketplace.Configuration.Behavior.HotlinkProtection import Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection
from SoftLayer.sltypes.Network.CdnMarketplace.Configuration.Behavior.Geoblocking import Network_CdnMarketplace_Configuration_Behavior_Geoblocking
from SoftLayer.sltypes.Container.Network.CdnMarketplace.Configuration.Performance.DynamicContentAcceleration import Container_Network_CdnMarketplace_Configuration_Performance_DynamicContentAcceleration
from SoftLayer.sltypes.Entity import Entity

class Container_Network_CdnMarketplace_Configuration_Input(Entity):
    bucketName: str
    cacheKeyQueryRule: str
    certificateType: str
    cname: str
    domain: str
    dynamicContentAcceleration: Container_Network_CdnMarketplace_Configuration_Performance_DynamicContentAcceleration
    fileExtension: str
    geoblockingRule: Network_CdnMarketplace_Configuration_Behavior_Geoblocking
    header: str
    hotlinkProtection: Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection
    httpPort: int
    httpsPort: int
    oldPath: str
    origin: str
    originType: str
    path: str
    performanceConfiguration: str
    protocol: str
    respectHeaders: str
    serveStale: str
    status: str
    uniqueId: str
    vendorName: str
