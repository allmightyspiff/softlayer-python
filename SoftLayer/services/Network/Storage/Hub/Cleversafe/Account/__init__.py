# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_Hub_Cleversafe_Account(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_Hub_Cleversafe_Account'
        self.client = client

    def credentialCreate(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage_Credential]':

        data = self.client.call(
            self.service,
            'credentialCreate',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Credential import Credential
        return Credential(data)


    def credentialDelete(
        self,
        credential: 'SoftLayer_Network_Storage_Credential',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'credentialDelete',
            credential,
            id=identifier
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
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Storage_Hub_ObjectStorage_Bucket]':

        data = self.client.call(
            self.service,
            'getBuckets',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.Bucket import Bucket
        return Bucket(data)


    def getCapacityUsage(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getCapacityUsage',
            id=identifier
        )
        
        return data


    def getCloudObjectStorageMetrics(
        self,
        start: str,
        end: str,
        storageLocation: str,
        storageClass: str,
        metrics: str,
        identifier: int
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getCloudObjectStorageMetrics',
            start,
            end,
            storageLocation,
            storageClass,
            metrics,
            id=identifier
        )
        
        return data


    def getCredentialLimit(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getCredentialLimit',
            id=identifier
        )
        
        return data


    def getEndpoints(
        self,
        accountId: int,
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Storage_Hub_ObjectStorage_Endpoint]':

        data = self.client.call(
            self.service,
            'getEndpoints',
            accountId,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.Endpoint import Endpoint
        return Endpoint(data)


    def getEndpointsWithRefetch(
        self,
        accountId: int,
        refetch: bool,
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Storage_Hub_ObjectStorage_Endpoint]':

        data = self.client.call(
            self.service,
            'getEndpointsWithRefetch',
            accountId,
            refetch,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.Endpoint import Endpoint
        return Endpoint(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Hub_Cleversafe_Account':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Hub.Cleversafe.Account import Account
        return Account(data)


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getBillingItem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getCancelledBillingItem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getCancelledBillingItem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getCredentials(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Credential]':

        data = self.client.call(
            self.service,
            'getCredentials',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Credential import Credential
        return Credential(data)


    def getMetricTrackingObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object':

        data = self.client.call(
            self.service,
            'getMetricTrackingObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object import Object
        return Object(data)


    def getUuid(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getUuid',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


