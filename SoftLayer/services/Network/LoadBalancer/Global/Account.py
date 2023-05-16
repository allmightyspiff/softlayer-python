# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LoadBalancer_Global_Account(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LoadBalancer_Global_Account'
        self.client = client

    def addNsRecord(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addNsRecord',
            
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Network_LoadBalancer_Global_Account
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LoadBalancer_Global_Account':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LoadBalancer.Global.Account import Account
        return Account(data)


    def removeNsRecord(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeNsRecord',
            
        )
        
        return data


    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getHosts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LoadBalancer_Global_Host]':

        data = self.client.call(
            self.service,
            'getHosts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LoadBalancer.Global.Host import Host
        return Host(data)


    def getLoadBalanceType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LoadBalancer_Global_Type':

        data = self.client.call(
            self.service,
            'getLoadBalanceType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LoadBalancer.Global.Type import Type
        return Type(data)


    def getManagedResourceFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getManagedResourceFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


