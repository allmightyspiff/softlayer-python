from datetime import datetime
from SoftLayer.sltypes.Metric.Tracking.Object.Data import Metric_Tracking_Object_Data
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Metric_Tracking_Object(Entity):
    """Metric tracking objects provides a common interface to all metrics provided by SoftLayer. These metrics range
from network component traffic for a server to aggregated Bandwidth Pooling traffic and more. Every object
within SoftLayer's range of objects that has data that can be tracked over time has an associated tracking
object. Use the [[SoftLayer_Metric_Tracking_Object]] service to retrieve raw and graph data from a tracking
object."""
    data: list[Metric_Tracking_Object_Data]
    id_: int
    label: str
    resourceTableId: int
    startDate: datetime

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Metric_Tracking_Object'

    def getBackboneBandwidthGraph(self, identifier: int, graphTitle: str) -> 'Container_Bandwidth_GraphOutputs':
        """[DEPRECATED] Retrieve a graph of a SoftLayer backbone's recent traffic activity."""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getBackboneBandwidthGraph', graphTitle, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getBandwidthData(self, identifier: int, startDateTime: datetime, endDateTime: datetime, type_: str, rollupSeconds: int) -> list['Metric_Tracking_Object_Data']:
        """Retrieve raw bandwidth data from a tracking object."""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getBandwidthData', startDateTime, endDateTime, type, rollupSeconds, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getBandwidthGraph(self, identifier: int, startDateTime: datetime, endDateTime: datetime, graphType: str, fontSize: int, graphWidth: int, graphHeight: int, doNotShowTimeZone: bool) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve a bandwidth graph."""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getBandwidthGraph', startDateTime, endDateTime, graphType, fontSize, graphWidth, graphHeight, doNotShowTimeZone, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getBandwidthTotal(self, identifier: int, startDateTime: datetime, endDateTime: datetime, direction: str, type_: str) -> int:
        """Retrieve the total bandwidth used within a given time frame."""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getBandwidthTotal', startDateTime, endDateTime, direction, type, id=identifier)
        return data

    def getCustomGraphData(self, identifier: int, graphContainer: 'Container_Graph') -> 'Container_Graph':
        """Fetch metric data using the graph container class."""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getCustomGraphData', graphContainer, id=identifier)
        from SoftLayer.sltypes.Container_Graph import Container_Graph
        return data

    def getDetailsForDateRange(self, identifier: int, startDate: datetime, endDate: datetime, graphType: str) -> list['Container_Metric_Tracking_Object_Details']:
        """Retrieve metric detail data over a date range."""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getDetailsForDateRange', startDate, endDate, graphType, id=identifier)
        from SoftLayer.sltypes.Container_Metric_Tracking_Object_Details import Container_Metric_Tracking_Object_Details
        return data

    def getGraph(self, identifier: int, startDateTime: datetime, endDateTime: datetime, graphType: str) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve a graph of a virtual hosting platform's per instance use."""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getGraph', startDateTime, endDateTime, graphType, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getMetricDataTypes(self, identifier: int) -> list['Container_Metric_Data_Type']:
        """Returns valid metric data types for a tracking object"""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getMetricDataTypes', id=identifier)
        from SoftLayer.sltypes.Container_Metric_Data_Type import Container_Metric_Data_Type
        return data

    def getObject(self, identifier: int) -> 'Metric_Tracking_Object':
        """Retrieve a SoftLayer_Metric_Tracking_Object record."""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getObject', id=identifier)
        return data

    def getSummary(self, identifier: int, graphType: str) -> 'Container_Metric_Tracking_Object_Summary':
        """Retrieve metric summary."""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getSummary', graphType, id=identifier)
        from SoftLayer.sltypes.Container_Metric_Tracking_Object_Summary import Container_Metric_Tracking_Object_Summary
        return data

    def getSummaryData(self, identifier: int, startDateTime: datetime, endDateTime: datetime, validTypes: 'Container_Metric_Data_Type', summaryPeriod: int) -> list['Metric_Tracking_Object_Data']:
        """Returns the metric data for the date range provided"""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getSummaryData', startDateTime, endDateTime, validTypes, summaryPeriod, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getType(self, identifier: int) -> 'Metric_Tracking_Object_Type':
        """"""
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getType', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Type import Metric_Tracking_Object_Type
        return data
