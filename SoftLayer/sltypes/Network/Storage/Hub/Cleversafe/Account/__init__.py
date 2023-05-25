from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_Hub_Cleversafe_Account(Entity):
    accountId: int
    id_: int
    notes: str
    username: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Hub_Cleversafe_Account'

    def credentialCreate(self, identifier: int) -> list['Network_Storage_Credential']:
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'credentialCreate', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Credential import Network_Storage_Credential
        return data

    def credentialDelete(self, identifier: int, credential: 'Network_Storage_Credential') -> bool:
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'credentialDelete', credential, id=identifier)
        return data

    def getAllObjects(self) -> list['Network_Storage_Hub_Cleversafe_Account']:
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getAllObjects')
        from SoftLayer.sltypes.Network_Storage_Hub_Cleversafe_Account import Network_Storage_Hub_Cleversafe_Account
        return data

    def getBuckets(self, identifier: int) -> list['Container_Network_Storage_Hub_ObjectStorage_Bucket']:
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getBuckets', id=identifier)
        from SoftLayer.sltypes.Container_Network_Storage_Hub_ObjectStorage_Bucket import Container_Network_Storage_Hub_ObjectStorage_Bucket
        return data

    def getCapacityUsage(self, identifier: int) -> int:
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getCapacityUsage', id=identifier)
        return data

    def getCloudObjectStorageMetrics(self, identifier: int, start: str, end: str, storageLocation: str, storageClass: str, metrics: str) -> list[str]:
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getCloudObjectStorageMetrics', start, end, storageLocation, storageClass, metrics, id=identifier)
        return data

    def getCredentialLimit(self, identifier: int) -> int:
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getCredentialLimit', id=identifier)
        return data

    def getEndpoints(self, identifier: int, accountId: int) -> list['Container_Network_Storage_Hub_ObjectStorage_Endpoint']:
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getEndpoints', accountId, id=identifier)
        from SoftLayer.sltypes.Container_Network_Storage_Hub_ObjectStorage_Endpoint import Container_Network_Storage_Hub_ObjectStorage_Endpoint
        return data

    def getEndpointsWithRefetch(self, identifier: int, accountId: int, refetch: bool) -> list['Container_Network_Storage_Hub_ObjectStorage_Endpoint']:
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getEndpointsWithRefetch', accountId, refetch, id=identifier)
        from SoftLayer.sltypes.Container_Network_Storage_Hub_ObjectStorage_Endpoint import Container_Network_Storage_Hub_ObjectStorage_Endpoint
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_Hub_Cleversafe_Account':
        """Retrieve a SoftLayer_Network_Storage_Hub_Cleversafe_Account record."""
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Hub_Cleversafe_Account import Network_Storage_Hub_Cleversafe_Account
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getCancelledBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getCancelledBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getCredentials(self, identifier: int) -> list['Network_Storage_Credential']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getCredentials', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Credential import Network_Storage_Credential
        return data

    def getMetricTrackingObject(self, identifier: int) -> 'Metric_Tracking_Object':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getMetricTrackingObject', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object import Metric_Tracking_Object
        return data

    def getUuid(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Hub_Cleversafe_Account', 'getUuid', id=identifier)
        return data
