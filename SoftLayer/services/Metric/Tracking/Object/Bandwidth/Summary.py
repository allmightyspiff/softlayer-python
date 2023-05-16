# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Metric_Tracking_Object_Bandwidth_Summary(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Metric_Tracking_Object_Bandwidth_Summary'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object_Bandwidth_Summary':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Bandwidth.Summary import Summary
        return Summary(data)


