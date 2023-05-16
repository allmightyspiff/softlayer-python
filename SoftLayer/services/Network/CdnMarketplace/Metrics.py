# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Metrics(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Metrics'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getCustomerInvoicingMetrics(
        self,
        vendorName: str,
        startDate: int,
        endDate: int,
        frequency: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Metrics]':
        data = self.client.call(
            self.service,
            'getCustomerInvoicingMetrics',
            vendorName,
            startDate,
            endDate,
            frequency
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Metrics import Metrics
        return SL_Metrics(data)

# This file was automatically generated with tools/generateTypes.py
    def getCustomerRealTimeMetrics(
        self,
        vendorName: str,
        startTime: int,
        endTime: int,
        timeInterval: int
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Metrics]':
        data = self.client.call(
            self.service,
            'getCustomerRealTimeMetrics',
            vendorName,
            startTime,
            endTime,
            timeInterval
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Metrics import Metrics
        return SL_Metrics(data)

# This file was automatically generated with tools/generateTypes.py
    def getCustomerUsageMetrics(
        self,
        vendorName: str,
        startDate: int,
        endDate: int,
        frequency: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Metrics]':
        data = self.client.call(
            self.service,
            'getCustomerUsageMetrics',
            vendorName,
            startDate,
            endDate,
            frequency
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Metrics import Metrics
        return SL_Metrics(data)

# This file was automatically generated with tools/generateTypes.py
    def getMappingBandwidthByRegionMetrics(
        self,
        mappingUniqueId: str,
        startDate: int,
        endDate: int,
        frequency: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Metrics]':
        data = self.client.call(
            self.service,
            'getMappingBandwidthByRegionMetrics',
            mappingUniqueId,
            startDate,
            endDate,
            frequency
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Metrics import Metrics
        return SL_Metrics(data)

# This file was automatically generated with tools/generateTypes.py
    def getMappingBandwidthMetrics(
        self,
        mappingUniqueId: str,
        startDate: int,
        endDate: int,
        frequency: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Metrics]':
        data = self.client.call(
            self.service,
            'getMappingBandwidthMetrics',
            mappingUniqueId,
            startDate,
            endDate,
            frequency
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Metrics import Metrics
        return SL_Metrics(data)

# This file was automatically generated with tools/generateTypes.py
    def getMappingHitsByTypeMetrics(
        self,
        mappingUniqueId: str,
        startDate: int,
        endDate: int,
        frequency: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Metrics]':
        data = self.client.call(
            self.service,
            'getMappingHitsByTypeMetrics',
            mappingUniqueId,
            startDate,
            endDate,
            frequency
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Metrics import Metrics
        return SL_Metrics(data)

# This file was automatically generated with tools/generateTypes.py
    def getMappingHitsMetrics(
        self,
        mappingUniqueId: str,
        startDate: int,
        endDate: int,
        frequency: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Metrics]':
        data = self.client.call(
            self.service,
            'getMappingHitsMetrics',
            mappingUniqueId,
            startDate,
            endDate,
            frequency
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Metrics import Metrics
        return SL_Metrics(data)

# This file was automatically generated with tools/generateTypes.py
    def getMappingIntegratedMetrics(
        self,
        mappingUniqueId: str,
        startTime: int,
        endTime: int,
        frequency: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Metrics]':
        data = self.client.call(
            self.service,
            'getMappingIntegratedMetrics',
            mappingUniqueId,
            startTime,
            endTime,
            frequency
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Metrics import Metrics
        return SL_Metrics(data)

# This file was automatically generated with tools/generateTypes.py
    def getMappingRealTimeMetrics(
        self,
        mappingUniqueId: str,
        startTime: int,
        endTime: int,
        timeInterval: int
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Metrics]':
        data = self.client.call(
            self.service,
            'getMappingRealTimeMetrics',
            mappingUniqueId,
            startTime,
            endTime,
            timeInterval
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Metrics import Metrics
        return SL_Metrics(data)

# This file was automatically generated with tools/generateTypes.py
    def getMappingUsageMetrics(
        self,
        mappingUniqueId: str,
        startDate: int,
        endDate: int,
        frequency: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Metrics]':
        data = self.client.call(
            self.service,
            'getMappingUsageMetrics',
            mappingUniqueId,
            startDate,
            endDate,
            frequency
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Metrics import Metrics
        return SL_Metrics(data)


