# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Historical_Report(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Historical_Report'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAccountHostUptimeSummary(
        self,
        startDateTime: str,
        endDateTime: str,
        accountId: int
    ) -> 'SoftLayer_Container_Account_Historical_Summary':
        data = self.client.call(
            self.service,
            'getAccountHostUptimeSummary',
            startDateTime,
            endDateTime,
            accountId
        )
        from SoftLayer.datatypes.Container.Account.Historical.Summary import Summary
        return SL_Summary(data)

# This file was automatically generated with tools/generateTypes.py
    def getAccountUrlUptimeSummary(
        self,
        startDateTime: str,
        endDateTime: str,
        accountId: int
    ) -> 'SoftLayer_Container_Account_Historical_Summary':
        data = self.client.call(
            self.service,
            'getAccountUrlUptimeSummary',
            startDateTime,
            endDateTime,
            accountId
        )
        from SoftLayer.datatypes.Container.Account.Historical.Summary import Summary
        return SL_Summary(data)

# This file was automatically generated with tools/generateTypes.py
    def getHostUptimeDetail(
        self,
        configurationValueId: int,
        startDateTime: str,
        endDateTime: str
    ) -> 'SoftLayer_Container_Account_Historical_Summary_Detail':
        data = self.client.call(
            self.service,
            'getHostUptimeDetail',
            configurationValueId,
            startDateTime,
            endDateTime
        )
        from SoftLayer.datatypes.Container.Account.Historical.Summary.Detail import Detail
        return SL_Detail(data)

# This file was automatically generated with tools/generateTypes.py
    def getHostUptimeGraphData(
        self,
        configurationValueId: int,
        startDate: str,
        endDate: str
    ) -> 'SoftLayer_Container_Graph':
        data = self.client.call(
            self.service,
            'getHostUptimeGraphData',
            configurationValueId,
            startDate,
            endDate
        )
        from SoftLayer.datatypes.Container.Graph import Graph
        return SL_Graph(data)

# This file was automatically generated with tools/generateTypes.py
    def getUrlUptimeDetail(
        self,
        configurationValueId: int,
        startDateTime: str,
        endDateTime: str
    ) -> 'SoftLayer_Container_Account_Historical_Summary_Detail':
        data = self.client.call(
            self.service,
            'getUrlUptimeDetail',
            configurationValueId,
            startDateTime,
            endDateTime
        )
        from SoftLayer.datatypes.Container.Account.Historical.Summary.Detail import Detail
        return SL_Detail(data)

# This file was automatically generated with tools/generateTypes.py
    def getUrlUptimeGraphData(
        self,
        configurationValueId: int,
        startDate: str,
        endDate: str
    ) -> 'SoftLayer_Container_Graph':
        data = self.client.call(
            self.service,
            'getUrlUptimeGraphData',
            configurationValueId,
            startDate,
            endDate
        )
        from SoftLayer.datatypes.Container.Graph import Graph
        return SL_Graph(data)


