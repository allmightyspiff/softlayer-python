# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LBaaS_Member(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LBaaS_Member'
        self.client = client

    def addLoadBalancerMembers(
        self,
        loadBalancerUuid: str,
        serverInstances: 'SoftLayer_Network_LBaaS_LoadBalancerServerInstanceInfo',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':

        data = self.client.call(
            self.service,
            'addLoadBalancerMembers',
            loadBalancerUuid,
            serverInstances,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return LoadBalancer(data)


    def deleteLoadBalancerMembers(
        self,
        loadBalancerUuid: str,
        memberUuids: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':

        data = self.client.call(
            self.service,
            'deleteLoadBalancerMembers',
            loadBalancerUuid,
            memberUuids,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return LoadBalancer(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LBaaS_Member':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LBaaS.Member import Member
        return Member(data)


    def updateLoadBalancerMembers(
        self,
        loadBalancerUuid: str,
        members: 'SoftLayer_Network_LBaaS_Member',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':

        data = self.client.call(
            self.service,
            'updateLoadBalancerMembers',
            loadBalancerUuid,
            members,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return LoadBalancer(data)


