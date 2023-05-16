# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_Storage_Repository(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_Storage_Repository'
        self.client = client

    def getArchiveDiskUsageRatePerGb(
        self,
        identifier: int
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getArchiveDiskUsageRatePerGb',
            id=identifier
        )
        
        return data


    def getAverageDiskUsageMetricDataFromInfluxByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        identifier: int
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getAverageDiskUsageMetricDataFromInfluxByDate',
            startDateTime,
            endDateTime,
            id=identifier
        )
        
        return data


    def getAverageUsageMetricDataByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        identifier: int
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getAverageUsageMetricDataByDate',
            startDateTime,
            endDateTime,
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Storage_Repository':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Storage.Repository import Repository
        return Repository(data)


    def getPublicImageDiskUsageRatePerGb(
        self,
        identifier: int
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getPublicImageDiskUsageRatePerGb',
            id=identifier
        )
        
        return data


    def getStorageLocations(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getStorageLocations',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getUsageMetricDataByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        identifier: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getUsageMetricDataByDate',
            startDateTime,
            endDateTime,
            id=identifier
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getUsageMetricImageByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getUsageMetricImageByDate',
            startDateTime,
            endDateTime,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


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


    def getDatacenter(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getDatacenter',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getDiskImages(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Disk_Image]':

        data = self.client.call(
            self.service,
            'getDiskImages',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Disk.Image import Image
        return Image(data)


    def getGuests(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getGuests',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getMetricTrackingObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object_Virtual_Storage_Repository':

        data = self.client.call(
            self.service,
            'getMetricTrackingObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Virtual.Storage.Repository import Repository
        return Repository(data)


    def getPublicImageBillingItem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getPublicImageBillingItem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Storage_Repository_Type':

        data = self.client.call(
            self.service,
            'getType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Storage.Repository.Type import Type
        return Type(data)


