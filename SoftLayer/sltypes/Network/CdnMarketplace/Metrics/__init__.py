from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Metrics(Entity):
    """This Metrics class provides methods to get CDN metrics based on account or mapping unique id."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Metrics'

    def getCustomerInvoicingMetrics(self, vendorName: str, startDate: int, endDate: int, frequency: str) -> list['Container_Network_CdnMarketplace_Metrics']:
        """Get the static & dynamic bandwidth and mapping hits of predetermined statistics for direct display (no graph)
for a customer's account over a given period of time. Frequency can be 'day', 'aggregate'. If the value 'day'
is specified for Frequency, return data will be ordered based on startDate to endDate, and if the value
'aggregate' is specified for Frequency, aggregated data from startDate to endDate will be returned. There is
a delay within 3 days(including today) for fetching the metrics data."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Metrics', 'getCustomerInvoicingMetrics', vendorName, startDate, endDate, frequency)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Metrics import Container_Network_CdnMarketplace_Metrics
        return data

    def getCustomerRealTimeMetrics(self, vendorName: str, startTime: int, endTime: int, timeInterval: int) -> list['Container_Network_CdnMarketplace_Metrics']:
        """Get the realtime metrics data for the current account. Takes the startTime and endTime and returns the total
metrics data and line graph metrics data divided by the timeInterval."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Metrics', 'getCustomerRealTimeMetrics', vendorName, startTime, endTime, timeInterval)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Metrics import Container_Network_CdnMarketplace_Metrics
        return data

    def getCustomerUsageMetrics(self, vendorName: str, startDate: int, endDate: int, frequency: str) -> list['Container_Network_CdnMarketplace_Metrics']:
        """Get the total number of predetermined statistics for direct display (no graph) for a customer's account over
a given period of time"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Metrics', 'getCustomerUsageMetrics', vendorName, startDate, endDate, frequency)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Metrics import Container_Network_CdnMarketplace_Metrics
        return data

    def getMappingBandwidthByRegionMetrics(self, mappingUniqueId: str, startDate: int, endDate: int, frequency: str) -> list['Container_Network_CdnMarketplace_Metrics']:
        """Get the total number of predetermined statistics for direct display (no graph) for a customer's account over
a given period of time"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Metrics', 'getMappingBandwidthByRegionMetrics', mappingUniqueId, startDate, endDate, frequency)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Metrics import Container_Network_CdnMarketplace_Metrics
        return data

    def getMappingBandwidthMetrics(self, mappingUniqueId: str, startDate: int, endDate: int, frequency: str) -> list['Container_Network_CdnMarketplace_Metrics']:
        """Get the amount of edge hits for an individual mapping."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Metrics', 'getMappingBandwidthMetrics', mappingUniqueId, startDate, endDate, frequency)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Metrics import Container_Network_CdnMarketplace_Metrics
        return data

    def getMappingHitsByTypeMetrics(self, mappingUniqueId: str, startDate: int, endDate: int, frequency: str) -> list['Container_Network_CdnMarketplace_Metrics']:
        """Get the total number of hits at a certain frequency over a given range of time. Frequency can be day, week,
and month where each interval is one plot point for a graph. Return Data must be ordered based on startDate,
endDate and frequency"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Metrics', 'getMappingHitsByTypeMetrics', mappingUniqueId, startDate, endDate, frequency)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Metrics import Container_Network_CdnMarketplace_Metrics
        return data

    def getMappingHitsMetrics(self, mappingUniqueId: str, startDate: int, endDate: int, frequency: str) -> list['Container_Network_CdnMarketplace_Metrics']:
        """Get the total number of hits at a certain frequency over a given range of time per domain mapping. Frequency
can be day, week, and month where each interval is one plot point for a graph. Return Data will be ordered
based on startDate, endDate and frequency."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Metrics', 'getMappingHitsMetrics', mappingUniqueId, startDate, endDate, frequency)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Metrics import Container_Network_CdnMarketplace_Metrics
        return data

    def getMappingIntegratedMetrics(self, mappingUniqueId: str, startTime: int, endTime: int, frequency: str) -> list['Container_Network_CdnMarketplace_Metrics']:
        """Get the integrated metrics data for the given mapping. You can get the the hits, bandwidth, hits by type and
bandwidth by region. It will return both the total data and the detail data."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Metrics', 'getMappingIntegratedMetrics', mappingUniqueId, startTime, endTime, frequency)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Metrics import Container_Network_CdnMarketplace_Metrics
        return data

    def getMappingRealTimeMetrics(self, mappingUniqueId: str, startTime: int, endTime: int, timeInterval: int) -> list['Container_Network_CdnMarketplace_Metrics']:
        """Get the real time metrics data for the given mapping"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Metrics', 'getMappingRealTimeMetrics', mappingUniqueId, startTime, endTime, timeInterval)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Metrics import Container_Network_CdnMarketplace_Metrics
        return data

    def getMappingUsageMetrics(self, mappingUniqueId: str, startDate: int, endDate: int, frequency: str) -> list['Container_Network_CdnMarketplace_Metrics']:
        """Get the total number of predetermined statistics for direct display for the given mapping"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Metrics', 'getMappingUsageMetrics', mappingUniqueId, startDate, endDate, frequency)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Metrics import Container_Network_CdnMarketplace_Metrics
        return data
