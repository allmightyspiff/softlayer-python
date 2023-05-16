# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Metric_Tracking_Object(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Metric_Tracking_Object'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getBackboneBandwidthGraph(
        self,
        graphTitle: str
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':
        data = self.client.call(
            self.service,
            'getBackboneBandwidthGraph',
            graphTitle
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return SL_GraphOutputs(data)

# This file was automatically generated with tools/generateTypes.py
    def getBandwidthData(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime,
        type: str,
        rollupSeconds: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':
        data = self.client.call(
            self.service,
            'getBandwidthData',
            startDateTime,
            endDateTime,
            type,
            rollupSeconds
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
    def getBandwidthGraph(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime,
        graphType: str,
        fontSize: int,
        graphWidth: int,
        graphHeight: int,
        doNotShowTimeZone: boolean
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
            doNotShowTimeZone
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return SL_GraphOutputs(data)

# This file was automatically generated with tools/generateTypes.py
    def getBandwidthTotal(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime,
        direction: str,
        type: str
    ) -> 'unsignedLong':
        data = self.client.call(
            self.service,
            'getBandwidthTotal',
            startDateTime,
            endDateTime,
            direction,
            type
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCustomGraphData(
        self,
        graphContainer: SoftLayer_Container_Graph
    ) -> 'SoftLayer_Container_Graph':
        data = self.client.call(
            self.service,
            'getCustomGraphData',
            graphContainer
        )
        from SoftLayer.datatypes.Container.Graph import Graph
        return SL_Graph(data)

# This file was automatically generated with tools/generateTypes.py
    def getDetailsForDateRange(
        self,
        startDate: dateTime,
        endDate: dateTime,
        graphType: str
    ) -> 'list[SoftLayer_Container_Metric_Tracking_Object_Details]':
        data = self.client.call(
            self.service,
            'getDetailsForDateRange',
            startDate,
            endDate,
            graphType
        )
        from SoftLayer.datatypes.Container.Metric.Tracking.Object.Details import Details
        return SL_Details(data)

# This file was automatically generated with tools/generateTypes.py
    def getGraph(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime,
        graphType: str
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':
        data = self.client.call(
            self.service,
            'getGraph',
            startDateTime,
            endDateTime,
            graphType
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return SL_GraphOutputs(data)

# This file was automatically generated with tools/generateTypes.py
    def getMetricDataTypes(
        self,
        
    ) -> 'list[SoftLayer_Container_Metric_Data_Type]':
        data = self.client.call(
            self.service,
            'getMetricDataTypes',
            
        )
        from SoftLayer.datatypes.Container.Metric.Data.Type import Type
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object import Object
        return SL_Object(data)

# This file was automatically generated with tools/generateTypes.py
    def getSummary(
        self,
        graphType: str
    ) -> 'SoftLayer_Container_Metric_Tracking_Object_Summary':
        data = self.client.call(
            self.service,
            'getSummary',
            graphType
        )
        from SoftLayer.datatypes.Container.Metric.Tracking.Object.Summary import Summary
        return SL_Summary(data)

# This file was automatically generated with tools/generateTypes.py
    def getSummaryData(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime,
        validTypes: SoftLayer_Container_Metric_Data_Type,
        summaryPeriod: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':
        data = self.client.call(
            self.service,
            'getSummaryData',
            startDateTime,
            endDateTime,
            validTypes,
            summaryPeriod
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object_Type':
        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Type import Type
        return SL_Type(data)


