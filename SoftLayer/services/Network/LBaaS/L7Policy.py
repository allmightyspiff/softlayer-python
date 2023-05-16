# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LBaaS_L7Policy(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LBaaS_L7Policy'
        self.client = client

    def addL7Policies(
        self,
        listenerUuid: str,
        policiesRules: SoftLayer_Network_LBaaS_PolicyRule,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':

        data = self.client.call(
            self.service,
            'addL7Policies',
            listenerUuid,
            policiesRules,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return LoadBalancer(data)


    def deleteObject(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':

        data = self.client.call(
            self.service,
            'deleteObject',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return LoadBalancer(data)


    def editObject(
        self,
        templateObject: SoftLayer_Network_LBaaS_L7Policy,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return LoadBalancer(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LBaaS_L7Policy':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LBaaS.L7Policy import L7Policy
        return L7Policy(data)


    def getL7Rules(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_L7Rule]':

        data = self.client.call(
            self.service,
            'getL7Rules',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.L7Rule import L7Rule
        return L7Rule(data)


