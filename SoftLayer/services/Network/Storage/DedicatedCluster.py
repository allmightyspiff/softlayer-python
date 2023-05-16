# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_DedicatedCluster(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_DedicatedCluster'
        self.client = client

    def getDedicatedClusterList(
        self,
        
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getDedicatedClusterList',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_DedicatedCluster':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.DedicatedCluster import DedicatedCluster
        return DedicatedCluster(data)


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


    def getServiceResource(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Service_Resource':

        data = self.client.call(
            self.service,
            'getServiceResource',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Service.Resource import Resource
        return Resource(data)


