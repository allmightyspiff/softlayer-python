# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_Hub_Swift_Metrics(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_Hub_Swift_Metrics'
        self.client = client

    def getMetricData(
        self,
        startDateTime: str,
        endDateTime: str,
        metricKey: str,
        location: str,
        identifier: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getMetricData',
            startDateTime,
            endDateTime,
            metricKey,
            location,
            id=identifier
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


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


