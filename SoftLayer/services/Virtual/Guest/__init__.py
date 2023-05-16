# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_Guest(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_Guest'
        self.client = client

    def activatePrivatePort(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'activatePrivatePort',
            id=identifier
        )
        
        return data


    def activatePublicPort(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'activatePublicPort',
            id=identifier
        )
        
        return data


    def allowAccessToNetworkStorage(
        self,
        networkStorageTemplateObject: 'SoftLayer_Network_Storage',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToNetworkStorage',
            networkStorageTemplateObject,
            id=identifier
        )
        
        return data


    def allowAccessToNetworkStorageList(
        self,
        networkStorageTemplateObjects: 'SoftLayer_Network_Storage',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToNetworkStorageList',
            networkStorageTemplateObjects,
            id=identifier
        )
        
        return data


    def attachDiskImage(
        self,
        imageId: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'attachDiskImage',
            imageId,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def cancelIsolationForDestructiveAction(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'cancelIsolationForDestructiveAction',
            id=identifier
        )
        
        return data


    def captureImage(
        self,
        captureTemplate: 'SoftLayer_Container_Disk_Image_Capture_Template',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':

        data = self.client.call(
            self.service,
            'captureImage',
            captureTemplate,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def checkHostDiskAvailability(
        self,
        diskCapacity: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'checkHostDiskAvailability',
            diskCapacity,
            id=identifier
        )
        
        return data


    def configureMetadataDisk(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'configureMetadataDisk',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def createArchiveTemplate(
        self,
        groupName: str,
        blockDevices: 'SoftLayer_Virtual_Guest_Block_Device',
        note: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':

        data = self.client.call(
            self.service,
            'createArchiveTemplate',
            groupName,
            blockDevices,
            note,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def createArchiveTransaction(
        self,
        groupName: str,
        blockDevices: 'SoftLayer_Virtual_Guest_Block_Device',
        note: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'createArchiveTransaction',
            groupName,
            blockDevices,
            note,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def createObject(
        self,
        templateObject: 'SoftLayer_Virtual_Guest',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def createObjects(
        self,
        templateObjects: 'SoftLayer_Virtual_Guest',
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def createPostSoftwareInstallTransaction(
        self,
        data: str,
        returnBoolean: bool,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createPostSoftwareInstallTransaction',
            data,
            returnBoolean,
            id=identifier
        )
        
        return data


    def deleteObject(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            id=identifier
        )
        
        return data


    def deleteTag(
        self,
        tagName: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteTag',
            tagName,
            id=identifier
        )
        
        return data


    def deleteTransientWebhook(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'deleteTransientWebhook',
            id=identifier
        )
        
        return data


    def detachDiskImage(
        self,
        imageId: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'detachDiskImage',
            imageId,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def editObject(
        self,
        templateObject: 'SoftLayer_Virtual_Guest',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def executeIderaBareMetalRestore(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'executeIderaBareMetalRestore',
            id=identifier
        )
        
        return data


    def executeR1SoftBareMetalRestore(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'executeR1SoftBareMetalRestore',
            id=identifier
        )
        
        return data


    def executeRemoteScript(
        self,
        uri: str,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'executeRemoteScript',
            uri,
            id=identifier
        )
        
        return data


    def executeRescueLayer(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'executeRescueLayer',
            id=identifier
        )
        
        return data


    def findByHostname(
        self,
        hostname: str,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'findByHostname',
            hostname,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def findByIpAddress(
        self,
        ipAddress: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'findByIpAddress',
            ipAddress,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def generateOrderTemplate(
        self,
        templateObject: 'SoftLayer_Virtual_Guest'
    ) -> 'SoftLayer_Container_Product_Order':

        data = self.client.call(
            self.service,
            'generateOrderTemplate',
            templateObject
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return Order(data)


    def getAdditionalRequiredPricesForOsReload(
        self,
        config: 'SoftLayer_Container_Hardware_Server_Configuration',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getAdditionalRequiredPricesForOsReload',
            config,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getAttachedNetworkStorages(
        self,
        nasType: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAttachedNetworkStorages',
            nasType,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getAvailableBlockDevicePositions(
        self,
        identifier: int
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getAvailableBlockDevicePositions',
            id=identifier
        )
        
        return data


    def getAvailableNetworkStorages(
        self,
        nasType: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAvailableNetworkStorages',
            nasType,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getBandwidthDataByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        networkType: str,
        identifier: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getBandwidthDataByDate',
            startDateTime,
            endDateTime,
            networkType,
            id=identifier
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getBandwidthForDateRange(
        self,
        startDate: str,
        endDate: str,
        identifier: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getBandwidthForDateRange',
            startDate,
            endDate,
            id=identifier
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getBandwidthImage(
        self,
        networkType: enum,
        snapshotRange: enum,
        dateSpecified: str,
        dateSpecifiedEnd: str,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getBandwidthImage',
            networkType,
            snapshotRange,
            dateSpecified,
            dateSpecifiedEnd,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getBandwidthImageByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        networkType: str,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getBandwidthImageByDate',
            startDateTime,
            endDateTime,
            networkType,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getBandwidthTotal(
        self,
        startDateTime: str,
        endDateTime: str,
        direction: str,
        side: str,
        identifier: int
    ) -> 'unsignedLong':

        data = self.client.call(
            self.service,
            'getBandwidthTotal',
            startDateTime,
            endDateTime,
            direction,
            side,
            id=identifier
        )
        
        return data


    def getBootMode(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBootMode',
            id=identifier
        )
        
        return data


    def getBootOrder(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBootOrder',
            id=identifier
        )
        
        return data


    def getConsoleAccessLog(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getConsoleAccessLog',
            id=identifier,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getCoreRestrictedOperatingSystemPrice(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Product_Item_Price':

        data = self.client.call(
            self.service,
            'getCoreRestrictedOperatingSystemPrice',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getCpuMetricDataByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        cpuIndexes: int,
        identifier: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getCpuMetricDataByDate',
            startDateTime,
            endDateTime,
            cpuIndexes,
            id=identifier
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getCpuMetricImage(
        self,
        snapshotRange: enum,
        dateSpecified: str,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getCpuMetricImage',
            snapshotRange,
            dateSpecified,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getCpuMetricImageByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        cpuIndexes: int,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getCpuMetricImageByDate',
            startDateTime,
            endDateTime,
            cpuIndexes,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getCreateObjectOptions(
        self,
        
    ) -> 'SoftLayer_Container_Virtual_Guest_Configuration':

        data = self.client.call(
            self.service,
            'getCreateObjectOptions',
            
        )
        from SoftLayer.datatypes.Container.Virtual.Guest.Configuration import Configuration
        return Configuration(data)


    def getCurrentBillingDetail(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getCurrentBillingDetail',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getCurrentBillingTotal(
        self,
        identifier: int
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getCurrentBillingTotal',
            id=identifier
        )
        
        return data


    def getCustomBandwidthDataByDate(
        self,
        graphData: 'SoftLayer_Container_Graph',
        identifier: int
    ) -> 'SoftLayer_Container_Graph':

        data = self.client.call(
            self.service,
            'getCustomBandwidthDataByDate',
            graphData,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Graph import Graph
        return Graph(data)


    def getCustomMetricDataByDate(
        self,
        graphData: 'SoftLayer_Container_Graph',
        identifier: int
    ) -> 'SoftLayer_Container_Graph':

        data = self.client.call(
            self.service,
            'getCustomMetricDataByDate',
            graphData,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Graph import Graph
        return Graph(data)


    def getDriveRetentionItemPrice(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Product_Item_Price':

        data = self.client.call(
            self.service,
            'getDriveRetentionItemPrice',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getFirewallProtectableSubnets(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getFirewallProtectableSubnets',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getFirstAvailableBlockDevicePosition(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFirstAvailableBlockDevicePosition',
            id=identifier
        )
        
        return data


    def getIsoBootImage(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Disk_Image':

        data = self.client.call(
            self.service,
            'getIsoBootImage',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Disk.Image import Image
        return Image(data)


    def getItemPricesFromSoftwareDescriptions(
        self,
        softwareDescriptions: 'SoftLayer_Software_Description',
        includeTranslationsFlag: bool,
        returnAllPricesFlag: bool,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getItemPricesFromSoftwareDescriptions',
            softwareDescriptions,
            includeTranslationsFlag,
            returnAllPricesFlag,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getMemoryMetricDataByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        identifier: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getMemoryMetricDataByDate',
            startDateTime,
            endDateTime,
            id=identifier
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getMemoryMetricImage(
        self,
        snapshotRange: enum,
        dateSpecified: str,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getMemoryMetricImage',
            snapshotRange,
            dateSpecified,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getMemoryMetricImageByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getMemoryMetricImageByDate',
            startDateTime,
            endDateTime,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getNetworkComponentFirewallProtectableIpAddresses(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getNetworkComponentFirewallProtectableIpAddresses',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getOrderTemplate(
        self,
        billingType: enum,
        orderPrices: 'SoftLayer_Product_Item_Price',
        identifier: int
    ) -> 'SoftLayer_Container_Product_Order':

        data = self.client.call(
            self.service,
            'getOrderTemplate',
            billingType,
            orderPrices,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return Order(data)


    def getPendingMaintenanceActions(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Virtual_Guest_PendingMaintenanceAction]':

        data = self.client.call(
            self.service,
            'getPendingMaintenanceActions',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Virtual.Guest.PendingMaintenanceAction import PendingMaintenanceAction
        return PendingMaintenanceAction(data)


    def getProvisionDate(
        self,
        identifier: int
    ) -> 'dateTime':

        data = self.client.call(
            self.service,
            'getProvisionDate',
            id=identifier
        )
        
        return data


    def getRecentMetricData(
        self,
        time: unsignedInt,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Metric_Tracking_Object]':

        data = self.client.call(
            self.service,
            'getRecentMetricData',
            time,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Metric.Tracking.Object import Object
        return Object(data)


    def getReverseDomainRecords(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Dns_Domain]':

        data = self.client.call(
            self.service,
            'getReverseDomainRecords',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return Domain(data)


    def getUpgradeItemPrices(
        self,
        includeDowngradeItemPrices: bool,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getUpgradeItemPrices',
            includeDowngradeItemPrices,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getValidBlockDeviceTemplateGroups(
        self,
        visibility: str,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group]':

        data = self.client.call(
            self.service,
            'getValidBlockDeviceTemplateGroups',
            visibility,
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def isBackendPingable(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isBackendPingable',
            id=identifier
        )
        
        return data


    def isCloudInit(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isCloudInit',
            id=identifier
        )
        
        return data


    def isPingable(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isPingable',
            id=identifier
        )
        
        return data


    def isolateInstanceForDestructiveAction(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'isolateInstanceForDestructiveAction',
            id=identifier
        )
        
        return data


    def migrate(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'migrate',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def migrateDedicatedHost(
        self,
        destinationHostId: int,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'migrateDedicatedHost',
            destinationHostId,
            id=identifier
        )
        
        return data


    def mountIsoImage(
        self,
        diskImageId: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'mountIsoImage',
            diskImageId,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def pause(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'pause',
            id=identifier
        )
        
        return data


    def powerCycle(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'powerCycle',
            id=identifier
        )
        
        return data


    def powerOff(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'powerOff',
            id=identifier
        )
        
        return data


    def powerOffSoft(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'powerOffSoft',
            id=identifier
        )
        
        return data


    def powerOn(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'powerOn',
            id=identifier
        )
        
        return data


    def rebootDefault(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'rebootDefault',
            id=identifier
        )
        
        return data


    def rebootHard(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'rebootHard',
            id=identifier
        )
        
        return data


    def rebootSoft(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'rebootSoft',
            id=identifier
        )
        
        return data


    def reloadCurrentOperatingSystemConfiguration(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'reloadCurrentOperatingSystemConfiguration',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def reloadOperatingSystem(
        self,
        token: str,
        config: 'SoftLayer_Container_Hardware_Server_Configuration',
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'reloadOperatingSystem',
            token,
            config,
            id=identifier
        )
        
        return data


    def removeAccessToNetworkStorage(
        self,
        networkStorageTemplateObject: 'SoftLayer_Network_Storage',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToNetworkStorage',
            networkStorageTemplateObject,
            id=identifier
        )
        
        return data


    def removeAccessToNetworkStorageList(
        self,
        networkStorageTemplateObjects: 'SoftLayer_Network_Storage',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToNetworkStorageList',
            networkStorageTemplateObjects,
            id=identifier
        )
        
        return data


    def removeTags(
        self,
        tags: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeTags',
            tags,
            id=identifier
        )
        
        return data


    def resume(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'resume',
            id=identifier
        )
        
        return data


    def sendTestReclaimScheduledAlert(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'sendTestReclaimScheduledAlert',
            id=identifier
        )
        
        return data


    def setPrivateNetworkInterfaceSpeed(
        self,
        newSpeed: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setPrivateNetworkInterfaceSpeed',
            newSpeed,
            id=identifier
        )
        
        return data


    def setPublicNetworkInterfaceSpeed(
        self,
        newSpeed: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setPublicNetworkInterfaceSpeed',
            newSpeed,
            id=identifier
        )
        
        return data


    def setTags(
        self,
        tags: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setTags',
            tags,
            id=identifier
        )
        
        return data


    def setTransientWebhook(
        self,
        uri: str,
        secret: str,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'setTransientWebhook',
            uri,
            secret,
            id=identifier
        )
        
        return data


    def setUserMetadata(
        self,
        metadata: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setUserMetadata',
            metadata,
            id=identifier
        )
        
        return data


    def shutdownPrivatePort(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'shutdownPrivatePort',
            id=identifier
        )
        
        return data


    def shutdownPublicPort(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'shutdownPublicPort',
            id=identifier
        )
        
        return data


    def unmountIsoImage(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'unmountIsoImage',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def validateImageTemplate(
        self,
        imageTemplateId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'validateImageTemplate',
            imageTemplateId,
            id=identifier
        )
        
        return data


    def verifyReloadOperatingSystem(
        self,
        config: 'SoftLayer_Container_Hardware_Server_Configuration',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'verifyReloadOperatingSystem',
            config,
            id=identifier
        )
        
        return data


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


    def getAccountOwnedPoolFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getAccountOwnedPoolFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getActiveNetworkMonitorIncident(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Incident]':

        data = self.client.call(
            self.service,
            'getActiveNetworkMonitorIncident',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Incident import Incident
        return Incident(data)


    def getActiveTickets(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getActiveTickets',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getActiveTransaction(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'getActiveTransaction',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getActiveTransactions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Provisioning_Version1_Transaction]':

        data = self.client.call(
            self.service,
            'getActiveTransactions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getAllowedHost(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Allowed_Host':

        data = self.client.call(
            self.service,
            'getAllowedHost',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def getAllowedNetworkStorage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAllowedNetworkStorage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getAllowedNetworkStorageReplicas(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAllowedNetworkStorageReplicas',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getAntivirusSpywareSoftwareComponent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component':

        data = self.client.call(
            self.service,
            'getAntivirusSpywareSoftwareComponent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getApplicationDeliveryController(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller':

        data = self.client.call(
            self.service,
            'getApplicationDeliveryController',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller import Controller
        return Controller(data)


    def getAttributes(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Attribute]':

        data = self.client.call(
            self.service,
            'getAttributes',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Attribute import Attribute
        return Attribute(data)


    def getAvailableMonitoring(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Query_Host_Stratum]':

        data = self.client.call(
            self.service,
            'getAvailableMonitoring',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Host.Stratum import Stratum
        return Stratum(data)


    def getAverageDailyPrivateBandwidthUsage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getAverageDailyPrivateBandwidthUsage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAverageDailyPublicBandwidthUsage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getAverageDailyPublicBandwidthUsage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBackendNetworkComponents(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Network_Component]':

        data = self.client.call(
            self.service,
            'getBackendNetworkComponents',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return Component(data)


    def getBackendRouters(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getBackendRouters',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getBandwidthAllocation(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getBandwidthAllocation',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBandwidthAllotmentDetail(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Version1_Allotment_Detail':

        data = self.client.call(
            self.service,
            'getBandwidthAllotmentDetail',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment.Detail import Detail
        return Detail(data)


    def getBillingCycleBandwidthUsage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Usage]':

        data = self.client.call(
            self.service,
            'getBillingCycleBandwidthUsage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Usage import Usage
        return Usage(data)


    def getBillingCyclePrivateBandwidthUsage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Usage':

        data = self.client.call(
            self.service,
            'getBillingCyclePrivateBandwidthUsage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Usage import Usage
        return Usage(data)


    def getBillingCyclePublicBandwidthUsage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Usage':

        data = self.client.call(
            self.service,
            'getBillingCyclePublicBandwidthUsage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Usage import Usage
        return Usage(data)


    def getBillingItem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getBillingItem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Virtual.Guest import Guest
        return Guest(data)


    def getBlockCancelBecauseDisconnectedFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getBlockCancelBecauseDisconnectedFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBlockDeviceTemplateGroup(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':

        data = self.client.call(
            self.service,
            'getBlockDeviceTemplateGroup',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getBlockDevices(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device]':

        data = self.client.call(
            self.service,
            'getBlockDevices',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device import Device
        return Device(data)


    def getBrowserConsoleAccessLogs(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_BrowserConsoleAccessLog]':

        data = self.client.call(
            self.service,
            'getBrowserConsoleAccessLogs',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.BrowserConsoleAccessLog import BrowserConsoleAccessLog
        return BrowserConsoleAccessLog(data)


    def getConsoleData(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Container_Virtual_ConsoleData':

        data = self.client.call(
            self.service,
            'getConsoleData',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Container.Virtual.ConsoleData import ConsoleData
        return ConsoleData(data)


    def getConsoleIpAddressFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getConsoleIpAddressFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getConsoleIpAddressRecord(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Network_Component_IpAddress':

        data = self.client.call(
            self.service,
            'getConsoleIpAddressRecord',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component.IpAddress import IpAddress
        return IpAddress(data)


    def getContinuousDataProtectionSoftwareComponent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component':

        data = self.client.call(
            self.service,
            'getContinuousDataProtectionSoftwareComponent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getControlPanel(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component':

        data = self.client.call(
            self.service,
            'getControlPanel',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getCurrentBandwidthSummary(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object_Bandwidth_Summary':

        data = self.client.call(
            self.service,
            'getCurrentBandwidthSummary',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Bandwidth.Summary import Summary
        return Summary(data)


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


    def getDedicatedHost(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_DedicatedHost':

        data = self.client.call(
            self.service,
            'getDedicatedHost',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.DedicatedHost import DedicatedHost
        return DedicatedHost(data)


    def getDeviceStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Device_Status':

        data = self.client.call(
            self.service,
            'getDeviceStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Device.Status import Status
        return Status(data)


    def getEvaultNetworkStorage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getEvaultNetworkStorage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getFirewallServiceComponent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Component_Firewall':

        data = self.client.call(
            self.service,
            'getFirewallServiceComponent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component.Firewall import Firewall
        return Firewall(data)


    def getFrontendNetworkComponents(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Network_Component]':

        data = self.client.call(
            self.service,
            'getFrontendNetworkComponents',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return Component(data)


    def getFrontendRouters(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getFrontendRouters',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getGlobalIdentifier(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getGlobalIdentifier',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getGpuCount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getGpuCount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getGpuType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getGpuType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getGuestBootParameter(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Boot_Parameter':

        data = self.client.call(
            self.service,
            'getGuestBootParameter',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Boot.Parameter import Parameter
        return Parameter(data)


    def getHardwareFunctionDescription(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getHardwareFunctionDescription',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHost(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Host':

        data = self.client.call(
            self.service,
            'getHost',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Host import Host
        return Host(data)


    def getHostIpsSoftwareComponent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component':

        data = self.client.call(
            self.service,
            'getHostIpsSoftwareComponent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getHourlyBillingFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHourlyBillingFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInboundPrivateBandwidthUsage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInboundPrivateBandwidthUsage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInboundPublicBandwidthUsage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInboundPublicBandwidthUsage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInternalTagReferences(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':

        data = self.client.call(
            self.service,
            'getInternalTagReferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return Reference(data)


    def getLastKnownPowerState(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Power_State':

        data = self.client.call(
            self.service,
            'getLastKnownPowerState',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Power.State import State
        return State(data)


    def getLastOperatingSystemReload(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'getLastOperatingSystemReload',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getLastTransaction(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'getLastTransaction',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getLatestNetworkMonitorIncident(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Monitor_Version1_Incident':

        data = self.client.call(
            self.service,
            'getLatestNetworkMonitorIncident',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Incident import Incident
        return Incident(data)


    def getLocalDiskFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getLocalDiskFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLocation(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getLocation',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getManagedResourceFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getManagedResourceFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


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


    def getMetricTrackingObjectId(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getMetricTrackingObjectId',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMonitoringRobot(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Monitoring_Robot':

        data = self.client.call(
            self.service,
            'getMonitoringRobot',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Monitoring.Robot import Robot
        return Robot(data)


    def getMonitoringServiceComponent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Monitor_Version1_Query_Host_Stratum':

        data = self.client.call(
            self.service,
            'getMonitoringServiceComponent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Host.Stratum import Stratum
        return Stratum(data)


    def getMonitoringServiceEligibilityFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getMonitoringServiceEligibilityFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMonitoringUserNotification(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Notification_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getMonitoringUserNotification',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Notification.Virtual.Guest import Guest
        return Guest(data)


    def getNetworkComponents(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Network_Component]':

        data = self.client.call(
            self.service,
            'getNetworkComponents',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return Component(data)


    def getNetworkMonitorIncidents(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Incident]':

        data = self.client.call(
            self.service,
            'getNetworkMonitorIncidents',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Incident import Incident
        return Incident(data)


    def getNetworkMonitors(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Query_Host]':

        data = self.client.call(
            self.service,
            'getNetworkMonitors',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Host import Host
        return Host(data)


    def getNetworkStorage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getNetworkStorage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getNetworkVlans(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Vlan]':

        data = self.client.call(
            self.service,
            'getNetworkVlans',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getOpenCancellationTicket(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket':

        data = self.client.call(
            self.service,
            'getOpenCancellationTicket',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOperatingSystem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component_OperatingSystem':

        data = self.client.call(
            self.service,
            'getOperatingSystem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component.OperatingSystem import OperatingSystem
        return OperatingSystem(data)


    def getOperatingSystemReferenceCode(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOperatingSystemReferenceCode',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderedPackageId(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOrderedPackageId',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOutboundPrivateBandwidthUsage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOutboundPrivateBandwidthUsage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOutboundPublicBandwidthUsage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOutboundPublicBandwidthUsage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOverBandwidthAllocationFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getOverBandwidthAllocationFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPendingMigrationFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPendingMigrationFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPlacementGroup(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_PlacementGroup':

        data = self.client.call(
            self.service,
            'getPlacementGroup',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.PlacementGroup import PlacementGroup
        return PlacementGroup(data)


    def getPowerState(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Power_State':

        data = self.client.call(
            self.service,
            'getPowerState',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Power.State import State
        return State(data)


    def getPrimaryBackendIpAddress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPrimaryBackendIpAddress',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPrimaryBackendNetworkComponent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Network_Component':

        data = self.client.call(
            self.service,
            'getPrimaryBackendNetworkComponent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return Component(data)


    def getPrimaryIpAddress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPrimaryIpAddress',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPrimaryNetworkComponent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Network_Component':

        data = self.client.call(
            self.service,
            'getPrimaryNetworkComponent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return Component(data)


    def getPrivateNetworkOnlyFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPrivateNetworkOnlyFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getProjectedOverBandwidthAllocationFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getProjectedOverBandwidthAllocationFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getProjectedPublicBandwidthUsage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getProjectedPublicBandwidthUsage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getRecentEvents(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Event]':

        data = self.client.call(
            self.service,
            'getRecentEvents',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event import Event
        return Event(data)


    def getRegionalGroup(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Group_Regional':

        data = self.client.call(
            self.service,
            'getRegionalGroup',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Group.Regional import Regional
        return Regional(data)


    def getRegionalInternetRegistry(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Regional_Internet_Registry':

        data = self.client.call(
            self.service,
            'getRegionalInternetRegistry',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Regional.Internet.Registry import Registry
        return Registry(data)


    def getReservedCapacityGroup(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_ReservedCapacityGroup':

        data = self.client.call(
            self.service,
            'getReservedCapacityGroup',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup import ReservedCapacityGroup
        return ReservedCapacityGroup(data)


    def getReservedCapacityGroupFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getReservedCapacityGroupFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getReservedCapacityGroupInstance(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_ReservedCapacityGroup_Instance':

        data = self.client.call(
            self.service,
            'getReservedCapacityGroupInstance',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup.Instance import Instance
        return Instance(data)


    def getSecurityScanRequests(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Security_Scanner_Request]':

        data = self.client.call(
            self.service,
            'getSecurityScanRequests',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Security.Scanner.Request import Request
        return Request(data)


    def getServerRoom(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getServerRoom',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getSoftwareComponents(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_Component]':

        data = self.client.call(
            self.service,
            'getSoftwareComponents',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getSshKeys(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Security_Ssh_Key]':

        data = self.client.call(
            self.service,
            'getSshKeys',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Security.Ssh.Key import Key
        return Key(data)


    def getStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Status import Status
        return Status(data)


    def getTagReferences(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':

        data = self.client.call(
            self.service,
            'getTagReferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return Reference(data)


    def getTransientGuestFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getTransientGuestFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTransientWebhookURI(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Attribute':

        data = self.client.call(
            self.service,
            'getTransientWebhookURI',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Attribute import Attribute
        return Attribute(data)


    def getType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Type':

        data = self.client.call(
            self.service,
            'getType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Type import Type
        return Type(data)


    def getUpgradeRequest(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Upgrade_Request':

        data = self.client.call(
            self.service,
            'getUpgradeRequest',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Upgrade.Request import Request
        return Request(data)


    def getUserData(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Attribute]':

        data = self.client.call(
            self.service,
            'getUserData',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Attribute import Attribute
        return Attribute(data)


    def getUsers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':

        data = self.client.call(
            self.service,
            'getUsers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getVirtualRack(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Version1_Allotment':

        data = self.client.call(
            self.service,
            'getVirtualRack',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getVirtualRackId(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getVirtualRackId',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getVirtualRackName(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getVirtualRackName',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


