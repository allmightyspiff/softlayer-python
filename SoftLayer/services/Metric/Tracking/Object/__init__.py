# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Metric_Tracking_Object(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Metric_Tracking_Object'
        self.client = client

    def getBackboneBandwidthGraph(
        self,
        graphTitle: str,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getBackboneBandwidthGraph',
            graphTitle,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getBandwidthData(
        self,
        startDateTime: str,
        endDateTime: str,
        type: str,
        rollupSeconds: int,
        identifier: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getBandwidthData',
            startDateTime,
            endDateTime,
            type,
            rollupSeconds,
            id=identifier
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getBandwidthGraph(
        self,
        startDateTime: str,
        endDateTime: str,
        graphType: str,
        fontSize: int,
        graphWidth: int,
        graphHeight: int,
        doNotShowTimeZone: bool,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getBandwidthGraph',
            startDateTime,
            endDateTime,
            graphType,
            fontSize,
            graphWidth,
            graphHeight,
            doNotShowTimeZone,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getBandwidthTotal(
        self,
        startDateTime: str,
        endDateTime: str,
        direction: str,
        type: str,
        identifier: int
    ) -> 'unsignedLong':

        data = self.client.call(
            self.service,
            'getBandwidthTotal',
            startDateTime,
            endDateTime,
            direction,
            type,
            id=identifier
        )
        
        return data


    def getCustomGraphData(
        self,
        graphContainer: 'SoftLayer_Container_Graph',
        identifier: int
    ) -> 'SoftLayer_Container_Graph':

        data = self.client.call(
            self.service,
            'getCustomGraphData',
            graphContainer,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Graph import Graph
        return Graph(data)


    def getDetailsForDateRange(
        self,
        startDate: str,
        endDate: str,
        graphType: str,
        identifier: int
    ) -> 'list[SoftLayer_Container_Metric_Tracking_Object_Details]':

        data = self.client.call(
            self.service,
            'getDetailsForDateRange',
            startDate,
            endDate,
            graphType,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Metric.Tracking.Object.Details import Details
        return Details(data)


    def getGraph(
        self,
        startDateTime: str,
        endDateTime: str,
        graphType: str,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getGraph',
            startDateTime,
            endDateTime,
            graphType,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getMetricDataTypes(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Metric_Data_Type]':

        data = self.client.call(
            self.service,
            'getMetricDataTypes',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Metric.Data.Type import Type
        return Type(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object import Object
        return Object(data)


    def getSummary(
        self,
        graphType: str,
        identifier: int
    ) -> 'SoftLayer_Container_Metric_Tracking_Object_Summary':

        data = self.client.call(
            self.service,
            'getSummary',
            graphType,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Metric.Tracking.Object.Summary import Summary
        return Summary(data)


    def getSummaryData(
        self,
        startDateTime: str,
        endDateTime: str,
        validTypes: 'SoftLayer_Container_Metric_Data_Type',
        summaryPeriod: int,
        identifier: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getSummaryData',
            startDateTime,
            endDateTime,
            validTypes,
            summaryPeriod,
            id=identifier
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object_Type':

        data = self.client.call(
            self.service,
            'getType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Type import Type
        return Type(data)


