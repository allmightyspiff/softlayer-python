from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_Hub_Swift_Metrics(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Hub_Swift_Metrics'

    def getMetricData(self, identifier: int, startDateTime: datetime, endDateTime: datetime, metricKey: str, location: str) -> list['Metric_Tracking_Object_Data']:
        data = self.client.call('SoftLayer_Network_Storage_Hub_Swift_Metrics', 'getMetricData', startDateTime, endDateTime, metricKey, location, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getSummaryData(self, identifier: int, startDateTime: datetime, endDateTime: datetime, validTypes: 'Container_Metric_Data_Type', summaryPeriod: int) -> list['Metric_Tracking_Object_Data']:
        data = self.client.call('SoftLayer_Network_Storage_Hub_Swift_Metrics', 'getSummaryData', startDateTime, endDateTime, validTypes, summaryPeriod, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data
