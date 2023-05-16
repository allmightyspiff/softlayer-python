# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_Storage_Repository(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_Storage_Repository'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getArchiveDiskUsageRatePerGb(
        self,
        
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getArchiveDiskUsageRatePerGb',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Repository(data)

# This file was automatically generated with tools/generateTypes.py
    def getPublicImageDiskUsageRatePerGb(
        self,
        
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getPublicImageDiskUsageRatePerGb',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_GraphOutputs(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Image(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Guest(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Repository(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)


