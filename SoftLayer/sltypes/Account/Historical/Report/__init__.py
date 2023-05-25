from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Historical_Report(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Historical_Report'

    def getAccountHostUptimeSummary(self, startDateTime: str, endDateTime: str, accountId: int) -> 'Container_Account_Historical_Summary':
        data = self.client.call('SoftLayer_Account_Historical_Report', 'getAccountHostUptimeSummary', startDateTime, endDateTime, accountId)
        from SoftLayer.sltypes.Container_Account_Historical_Summary import Container_Account_Historical_Summary
        return data

    def getAccountUrlUptimeSummary(self, startDateTime: str, endDateTime: str, accountId: int) -> 'Container_Account_Historical_Summary':
        data = self.client.call('SoftLayer_Account_Historical_Report', 'getAccountUrlUptimeSummary', startDateTime, endDateTime, accountId)
        from SoftLayer.sltypes.Container_Account_Historical_Summary import Container_Account_Historical_Summary
        return data

    def getHostUptimeDetail(self, configurationValueId: int, startDateTime: str, endDateTime: str) -> 'Container_Account_Historical_Summary_Detail':
        data = self.client.call('SoftLayer_Account_Historical_Report', 'getHostUptimeDetail', configurationValueId, startDateTime, endDateTime)
        from SoftLayer.sltypes.Container_Account_Historical_Summary_Detail import Container_Account_Historical_Summary_Detail
        return data

    def getHostUptimeGraphData(self, configurationValueId: int, startDate: str, endDate: str) -> 'Container_Graph':
        data = self.client.call('SoftLayer_Account_Historical_Report', 'getHostUptimeGraphData', configurationValueId, startDate, endDate)
        from SoftLayer.sltypes.Container_Graph import Container_Graph
        return data

    def getUrlUptimeDetail(self, configurationValueId: int, startDateTime: str, endDateTime: str) -> 'Container_Account_Historical_Summary_Detail':
        data = self.client.call('SoftLayer_Account_Historical_Report', 'getUrlUptimeDetail', configurationValueId, startDateTime, endDateTime)
        from SoftLayer.sltypes.Container_Account_Historical_Summary_Detail import Container_Account_Historical_Summary_Detail
        return data

    def getUrlUptimeGraphData(self, configurationValueId: int, startDate: str, endDate: str) -> 'Container_Graph':
        data = self.client.call('SoftLayer_Account_Historical_Report', 'getUrlUptimeGraphData', configurationValueId, startDate, endDate)
        from SoftLayer.sltypes.Container_Graph import Container_Graph
        return data
