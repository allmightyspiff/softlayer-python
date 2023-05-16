# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_Storage_Repository(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_Storage_Repository'
        self.client = client

    def getArchiveDiskUsageRatePerGb(
        self,
        
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getArchiveDiskUsageRatePerGb',
            
        )
        
        return data


    def getAverageDiskUsageMetricDataFromInfluxByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getAverageDiskUsageMetricDataFromInfluxByDate',
            startDateTime,
            endDateTime
        )
        
        return data


    def getAverageUsageMetricDataByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getAverageUsageMetricDataByDate',
            startDateTime,
            endDateTime
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Storage_Repository':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Storage.Repository import Repository
        return Repository(data)


    def getPublicImageDiskUsageRatePerGb(
        self,
        
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getPublicImageDiskUsageRatePerGb',
            
        )
        
        return data


    def getStorageLocations(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getStorageLocations',
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getUsageMetricDataByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getUsageMetricDataByDate',
            startDateTime,
            endDateTime
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getUsageMetricImageByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getUsageMetricImageByDate',
            startDateTime,
            endDateTime
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


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


    def getDatacenter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getDatacenter',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getDiskImages(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Disk_Image]':

        data = self.client.call(
            self.service,
            'getDiskImages',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Disk.Image import Image
        return Image(data)


    def getGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getMetricTrackingObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object_Virtual_Storage_Repository':

        data = self.client.call(
            self.service,
            'getMetricTrackingObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Virtual.Storage.Repository import Repository
        return Repository(data)


    def getPublicImageBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getPublicImageBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Storage_Repository_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Storage.Repository.Type import Type
        return Type(data)


