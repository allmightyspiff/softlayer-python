# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LBaaS_L7Rule(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LBaaS_L7Rule'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def addL7Rules(
        self,
        policyUuid: str,
        rules: SoftLayer_Network_LBaaS_L7Rule,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'addL7Rules',
            policyUuid,
            rules,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteL7Rules(
        self,
        policyUuid: str,
        ruleUuids: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'deleteL7Rules',
            policyUuid,
            ruleUuids,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LBaaS_L7Rule':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LBaaS.L7Rule import L7Rule
        return SL_L7Rule(data)

# This file was automatically generated with tools/generateTypes.py
    def updateL7Rules(
        self,
        policyUuid: str,
        rules: SoftLayer_Network_LBaaS_L7Rule,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'updateL7Rules',
            policyUuid,
            rules,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)


