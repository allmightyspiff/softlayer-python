from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_Storage_Repository(Entity):
    """The SoftLayer_Virtual_Storage_Repository represents a web based storage system that can be accessed through
many types of devices, interfaces, and other resources."""
    capacity: float
    description: str
    id_: int
    name: str
    publicFlag: int
    typeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_Storage_Repository'

    def getArchiveDiskUsageRatePerGb(self, identifier: int) -> float:
        """The rate that is charged for archiving every 1 gigabyte of data for a computing instance"""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getArchiveDiskUsageRatePerGb', id=identifier)
        return data

    def getAverageDiskUsageMetricDataFromInfluxByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime) -> float:
        """Returns the average disk usage for the timeframe based on the parameters provided."""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getAverageDiskUsageMetricDataFromInfluxByDate', startDateTime, endDateTime, id=identifier)
        return data

    def getAverageUsageMetricDataByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime) -> float:
        """Returns the average disk usage for the timeframe based on the parameters provided."""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getAverageUsageMetricDataByDate', startDateTime, endDateTime, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Virtual_Storage_Repository':
        """Retrieve a SoftLayer_Virtual_Storage_Repository record."""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getObject', id=identifier)
        return data

    def getPublicImageDiskUsageRatePerGb(self, identifier: int) -> float:
        """The rate that is charged for publishing every 1 gigabyte of data for an image template"""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getPublicImageDiskUsageRatePerGb', id=identifier)
        return data

    def getStorageLocations(self, identifier: int) -> list['Location']:
        """The available locations for public image storage."""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getStorageLocations', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getUsageMetricDataByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime) -> list['Metric_Tracking_Object_Data']:
        """Retrieve the metric data for disk space usage for a storage repository."""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getUsageMetricDataByDate', startDateTime, endDateTime, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getUsageMetricImageByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve an image of the disk usage data on a [[SoftLayer_Virtual_Guest|Cloud Computing Instance]] image for
the time range you provide."""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getUsageMetricImageByDate', startDateTime, endDateTime, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getDatacenter(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getDiskImages(self, identifier: int) -> list['Virtual_Disk_Image']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getDiskImages', id=identifier)
        from SoftLayer.sltypes.Virtual_Disk_Image import Virtual_Disk_Image
        return data

    def getGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getMetricTrackingObject(self, identifier: int) -> 'Metric_Tracking_Object_Virtual_Storage_Repository':
        """"""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getMetricTrackingObject', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Virtual_Storage_Repository import Metric_Tracking_Object_Virtual_Storage_Repository
        return data

    def getPublicImageBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getPublicImageBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getType(self, identifier: int) -> 'Virtual_Storage_Repository_Type':
        """"""
        data = self.client.call('SoftLayer_Virtual_Storage_Repository', 'getType', id=identifier)
        from SoftLayer.sltypes.Virtual_Storage_Repository_Type import Virtual_Storage_Repository_Type
        return data
