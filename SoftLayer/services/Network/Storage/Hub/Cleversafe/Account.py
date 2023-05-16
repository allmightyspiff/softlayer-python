# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_Hub_Cleversafe_Account(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_Hub_Cleversafe_Account'
        self.client = client

    def credentialCreate(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage_Credential]':

        data = self.client.call(
            self.service,
            'credentialCreate',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Credential import Credential
        return Credential(data)


    def credentialDelete(
        self,
        credential: SoftLayer_Network_Storage_Credential
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'credentialDelete',
            credential
        )
        
        return data


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Hub_Cleversafe_Account]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Hub.Cleversafe.Account import Account
        return Account(data)


    def getBuckets(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_Storage_Hub_ObjectStorage_Bucket]':

        data = self.client.call(
            self.service,
            'getBuckets',
            
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.Bucket import Bucket
        return Bucket(data)


    def getCapacityUsage(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getCapacityUsage',
            
        )
        
        return data


    def getCloudObjectStorageMetrics(
        self,
        start: str,
        end: str,
        storageLocation: str,
        storageClass: str,
        metrics: str
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getCloudObjectStorageMetrics',
            start,
            end,
            storageLocation,
            storageClass,
            metrics
        )
        
        return data


    def getCredentialLimit(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getCredentialLimit',
            
        )
        
        return data


    def getEndpoints(
        self,
        accountId: int
    ) -> 'list[SoftLayer_Container_Network_Storage_Hub_ObjectStorage_Endpoint]':

        data = self.client.call(
            self.service,
            'getEndpoints',
            accountId
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.Endpoint import Endpoint
        return Endpoint(data)


    def getEndpointsWithRefetch(
        self,
        accountId: int,
        refetch: boolean
    ) -> 'list[SoftLayer_Container_Network_Storage_Hub_ObjectStorage_Endpoint]':

        data = self.client.call(
            self.service,
            'getEndpointsWithRefetch',
            accountId,
            refetch
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.Endpoint import Endpoint
        return Endpoint(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Hub_Cleversafe_Account':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Hub.Cleversafe.Account import Account
        return Account(data)


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


    def getCancelledBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getCancelledBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getCredentials(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Credential]':

        data = self.client.call(
            self.service,
            'getCredentials',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Credential import Credential
        return Credential(data)


    def getMetricTrackingObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object':

        data = self.client.call(
            self.service,
            'getMetricTrackingObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object import Object
        return Object(data)


    def getUuid(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getUuid',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


