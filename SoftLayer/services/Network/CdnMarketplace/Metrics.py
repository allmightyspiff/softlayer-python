# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Metrics(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Metrics'
        self.client = client

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
        return Metrics(data)


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
        return Metrics(data)


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
        return Metrics(data)


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
        return Metrics(data)


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
        return Metrics(data)


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
        return Metrics(data)


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
        return Metrics(data)


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
        return Metrics(data)


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
        return Metrics(data)


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
        return Metrics(data)


