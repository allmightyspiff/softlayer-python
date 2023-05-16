# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_Hub_Swift_Metrics(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_Hub_Swift_Metrics'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getMetricData(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime,
        metricKey: str,
        location: str
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':
        data = self.client.call(
            self.service,
            'getMetricData',
            startDateTime,
            endDateTime,
            metricKey,
            location
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return SL_Data(data)

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


