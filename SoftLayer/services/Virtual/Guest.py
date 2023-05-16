# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_Guest(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_Guest'
        self.client = client

    def activatePrivatePort(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'activatePrivatePort',
            
        )
        
        return data


    def activatePublicPort(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'activatePublicPort',
            
        )
        
        return data


    def allowAccessToNetworkStorage(
        self,
        networkStorageTemplateObject: SoftLayer_Network_Storage
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToNetworkStorage',
            networkStorageTemplateObject
        )
        
        return data


    def allowAccessToNetworkStorageList(
        self,
        networkStorageTemplateObjects: SoftLayer_Network_Storage
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToNetworkStorageList',
            networkStorageTemplateObjects
        )
        
        return data


    def attachDiskImage(
        self,
        imageId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'attachDiskImage',
            imageId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def cancelIsolationForDestructiveAction(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'cancelIsolationForDestructiveAction',
            
        )
        
        return data


    def captureImage(
        self,
        captureTemplate: SoftLayer_Container_Disk_Image_Capture_Template,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':

        data = self.client.call(
            self.service,
            'captureImage',
            captureTemplate,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def checkHostDiskAvailability(
        self,
        diskCapacity: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'checkHostDiskAvailability',
            diskCapacity
        )
        
        return data


    def configureMetadataDisk(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'configureMetadataDisk',
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def createArchiveTemplate(
        self,
        groupName: str,
        blockDevices: SoftLayer_Virtual_Guest_Block_Device,
        note: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':

        data = self.client.call(
            self.service,
            'createArchiveTemplate',
            groupName,
            blockDevices,
            note,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def createArchiveTransaction(
        self,
        groupName: str,
        blockDevices: SoftLayer_Virtual_Guest_Block_Device,
        note: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'createArchiveTransaction',
            groupName,
            blockDevices,
            note,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def createObject(
        self,
        templateObject: SoftLayer_Virtual_Guest,
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
        templateObjects: SoftLayer_Virtual_Guest,
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
        returnBoolean: boolean
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createPostSoftwareInstallTransaction',
            data,
            returnBoolean
        )
        
        return data


    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def deleteTag(
        self,
        tagName: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteTag',
            tagName
        )
        
        return data


    def deleteTransientWebhook(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'deleteTransientWebhook',
            
        )
        
        return data


    def detachDiskImage(
        self,
        imageId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'detachDiskImage',
            imageId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def editObject(
        self,
        templateObject: SoftLayer_Virtual_Guest
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def executeIderaBareMetalRestore(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'executeIderaBareMetalRestore',
            
        )
        
        return data


    def executeR1SoftBareMetalRestore(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'executeR1SoftBareMetalRestore',
            
        )
        
        return data


    def executeRemoteScript(
        self,
        uri: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'executeRemoteScript',
            uri
        )
        
        return data


    def executeRescueLayer(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'executeRescueLayer',
            
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
        templateObject: SoftLayer_Virtual_Guest
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
        config: SoftLayer_Container_Hardware_Server_Configuration,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getAdditionalRequiredPricesForOsReload',
            config,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getAttachedNetworkStorages(
        self,
        nasType: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAttachedNetworkStorages',
            nasType,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getAvailableBlockDevicePositions(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getAvailableBlockDevicePositions',
            
        )
        
        return data


    def getAvailableNetworkStorages(
        self,
        nasType: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAvailableNetworkStorages',
            nasType,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getBandwidthDataByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime,
        networkType: str
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getBandwidthDataByDate',
            startDateTime,
            endDateTime,
            networkType
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getBandwidthForDateRange(
        self,
        startDate: dateTime,
        endDate: dateTime
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getBandwidthForDateRange',
            startDate,
            endDate
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getBandwidthImage(
        self,
        networkType: enum,
        snapshotRange: enum,
        dateSpecified: dateTime,
        dateSpecifiedEnd: dateTime
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getBandwidthImage',
            networkType,
            snapshotRange,
            dateSpecified,
            dateSpecifiedEnd
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getBandwidthImageByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime,
        networkType: str
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getBandwidthImageByDate',
            startDateTime,
            endDateTime,
            networkType
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getBandwidthTotal(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime,
        direction: str,
        side: str
    ) -> 'unsignedLong':

        data = self.client.call(
            self.service,
            'getBandwidthTotal',
            startDateTime,
            endDateTime,
            direction,
            side
        )
        
        return data


    def getBootMode(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBootMode',
            
        )
        
        return data


    def getBootOrder(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBootOrder',
            
        )
        
        return data


    def getConsoleAccessLog(
        self,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getConsoleAccessLog',
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getCoreRestrictedOperatingSystemPrice(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Product_Item_Price':

        data = self.client.call(
            self.service,
            'getCoreRestrictedOperatingSystemPrice',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getCpuMetricDataByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime,
        cpuIndexes: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getCpuMetricDataByDate',
            startDateTime,
            endDateTime,
            cpuIndexes
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getCpuMetricImage(
        self,
        snapshotRange: enum,
        dateSpecified: dateTime
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getCpuMetricImage',
            snapshotRange,
            dateSpecified
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getCpuMetricImageByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime,
        cpuIndexes: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getCpuMetricImageByDate',
            startDateTime,
            endDateTime,
            cpuIndexes
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
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getCurrentBillingDetail',
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getCurrentBillingTotal(
        self,
        
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getCurrentBillingTotal',
            
        )
        
        return data


    def getCustomBandwidthDataByDate(
        self,
        graphData: SoftLayer_Container_Graph
    ) -> 'SoftLayer_Container_Graph':

        data = self.client.call(
            self.service,
            'getCustomBandwidthDataByDate',
            graphData
        )
        from SoftLayer.datatypes.Container.Graph import Graph
        return Graph(data)


    def getCustomMetricDataByDate(
        self,
        graphData: SoftLayer_Container_Graph
    ) -> 'SoftLayer_Container_Graph':

        data = self.client.call(
            self.service,
            'getCustomMetricDataByDate',
            graphData
        )
        from SoftLayer.datatypes.Container.Graph import Graph
        return Graph(data)


    def getDriveRetentionItemPrice(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Product_Item_Price':

        data = self.client.call(
            self.service,
            'getDriveRetentionItemPrice',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getFirewallProtectableSubnets(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getFirewallProtectableSubnets',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getFirstAvailableBlockDevicePosition(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFirstAvailableBlockDevicePosition',
            
        )
        
        return data


    def getIsoBootImage(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Disk_Image':

        data = self.client.call(
            self.service,
            'getIsoBootImage',
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Disk.Image import Image
        return Image(data)


    def getItemPricesFromSoftwareDescriptions(
        self,
        softwareDescriptions: SoftLayer_Software_Description,
        includeTranslationsFlag: boolean,
        returnAllPricesFlag: boolean,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getItemPricesFromSoftwareDescriptions',
            softwareDescriptions,
            includeTranslationsFlag,
            returnAllPricesFlag,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getMemoryMetricDataByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getMemoryMetricDataByDate',
            startDateTime,
            endDateTime
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getMemoryMetricImage(
        self,
        snapshotRange: enum,
        dateSpecified: dateTime
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getMemoryMetricImage',
            snapshotRange,
            dateSpecified
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getMemoryMetricImageByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getMemoryMetricImageByDate',
            startDateTime,
            endDateTime
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getNetworkComponentFirewallProtectableIpAddresses(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getNetworkComponentFirewallProtectableIpAddresses',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getOrderTemplate(
        self,
        billingType: enum,
        orderPrices: SoftLayer_Product_Item_Price
    ) -> 'SoftLayer_Container_Product_Order':

        data = self.client.call(
            self.service,
            'getOrderTemplate',
            billingType,
            orderPrices
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return Order(data)


    def getPendingMaintenanceActions(
        self,
        
    ) -> 'list[SoftLayer_Container_Virtual_Guest_PendingMaintenanceAction]':

        data = self.client.call(
            self.service,
            'getPendingMaintenanceActions',
            
        )
        from SoftLayer.datatypes.Container.Virtual.Guest.PendingMaintenanceAction import PendingMaintenanceAction
        return PendingMaintenanceAction(data)


    def getProvisionDate(
        self,
        
    ) -> 'dateTime':

        data = self.client.call(
            self.service,
            'getProvisionDate',
            
        )
        
        return data


    def getRecentMetricData(
        self,
        time: unsignedInt,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Metric_Tracking_Object]':

        data = self.client.call(
            self.service,
            'getRecentMetricData',
            time,
            mask=objectMask
        )
        from SoftLayer.datatypes.Metric.Tracking.Object import Object
        return Object(data)


    def getReverseDomainRecords(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Dns_Domain]':

        data = self.client.call(
            self.service,
            'getReverseDomainRecords',
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return Domain(data)


    def getUpgradeItemPrices(
        self,
        includeDowngradeItemPrices: boolean,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getUpgradeItemPrices',
            includeDowngradeItemPrices,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getValidBlockDeviceTemplateGroups(
        self,
        visibility: str,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group]':

        data = self.client.call(
            self.service,
            'getValidBlockDeviceTemplateGroups',
            visibility,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def isBackendPingable(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isBackendPingable',
            
        )
        
        return data


    def isCloudInit(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isCloudInit',
            
        )
        
        return data


    def isPingable(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isPingable',
            
        )
        
        return data


    def isolateInstanceForDestructiveAction(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'isolateInstanceForDestructiveAction',
            
        )
        
        return data


    def migrate(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'migrate',
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def migrateDedicatedHost(
        self,
        destinationHostId: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'migrateDedicatedHost',
            destinationHostId
        )
        
        return data


    def mountIsoImage(
        self,
        diskImageId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'mountIsoImage',
            diskImageId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def pause(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'pause',
            
        )
        
        return data


    def powerCycle(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'powerCycle',
            
        )
        
        return data


    def powerOff(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'powerOff',
            
        )
        
        return data


    def powerOffSoft(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'powerOffSoft',
            
        )
        
        return data


    def powerOn(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'powerOn',
            
        )
        
        return data


    def rebootDefault(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'rebootDefault',
            
        )
        
        return data


    def rebootHard(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'rebootHard',
            
        )
        
        return data


    def rebootSoft(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'rebootSoft',
            
        )
        
        return data


    def reloadCurrentOperatingSystemConfiguration(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'reloadCurrentOperatingSystemConfiguration',
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def reloadOperatingSystem(
        self,
        token: str,
        config: SoftLayer_Container_Hardware_Server_Configuration
    ) -> 'string':

        data = self.client.call(
            self.service,
            'reloadOperatingSystem',
            token,
            config
        )
        
        return data


    def removeAccessToNetworkStorage(
        self,
        networkStorageTemplateObject: SoftLayer_Network_Storage
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToNetworkStorage',
            networkStorageTemplateObject
        )
        
        return data


    def removeAccessToNetworkStorageList(
        self,
        networkStorageTemplateObjects: SoftLayer_Network_Storage
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToNetworkStorageList',
            networkStorageTemplateObjects
        )
        
        return data


    def removeTags(
        self,
        tags: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeTags',
            tags
        )
        
        return data


    def resume(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'resume',
            
        )
        
        return data


    def sendTestReclaimScheduledAlert(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'sendTestReclaimScheduledAlert',
            
        )
        
        return data


    def setPrivateNetworkInterfaceSpeed(
        self,
        newSpeed: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setPrivateNetworkInterfaceSpeed',
            newSpeed
        )
        
        return data


    def setPublicNetworkInterfaceSpeed(
        self,
        newSpeed: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setPublicNetworkInterfaceSpeed',
            newSpeed
        )
        
        return data


    def setTags(
        self,
        tags: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setTags',
            tags
        )
        
        return data


    def setTransientWebhook(
        self,
        uri: str,
        secret: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'setTransientWebhook',
            uri,
            secret
        )
        
        return data


    def setUserMetadata(
        self,
        metadata: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setUserMetadata',
            metadata
        )
        
        return data


    def shutdownPrivatePort(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'shutdownPrivatePort',
            
        )
        
        return data


    def shutdownPublicPort(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'shutdownPublicPort',
            
        )
        
        return data


    def unmountIsoImage(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'unmountIsoImage',
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def validateImageTemplate(
        self,
        imageTemplateId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'validateImageTemplate',
            imageTemplateId
        )
        
        return data


    def verifyReloadOperatingSystem(
        self,
        config: SoftLayer_Container_Hardware_Server_Configuration
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'verifyReloadOperatingSystem',
            config
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


    def getAccountOwnedPoolFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getAccountOwnedPoolFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getActiveNetworkMonitorIncident(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Incident]':

        data = self.client.call(
            self.service,
            'getActiveNetworkMonitorIncident',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Incident import Incident
        return Incident(data)


    def getActiveTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getActiveTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getActiveTransaction(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'getActiveTransaction',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getActiveTransactions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Provisioning_Version1_Transaction]':

        data = self.client.call(
            self.service,
            'getActiveTransactions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getAllowedHost(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Allowed_Host':

        data = self.client.call(
            self.service,
            'getAllowedHost',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def getAllowedNetworkStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAllowedNetworkStorage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getAllowedNetworkStorageReplicas(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAllowedNetworkStorageReplicas',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getAntivirusSpywareSoftwareComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component':

        data = self.client.call(
            self.service,
            'getAntivirusSpywareSoftwareComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getApplicationDeliveryController(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller':

        data = self.client.call(
            self.service,
            'getApplicationDeliveryController',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller import Controller
        return Controller(data)


    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Attribute]':

        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Attribute import Attribute
        return Attribute(data)


    def getAvailableMonitoring(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Query_Host_Stratum]':

        data = self.client.call(
            self.service,
            'getAvailableMonitoring',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Host.Stratum import Stratum
        return Stratum(data)


    def getAverageDailyPrivateBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getAverageDailyPrivateBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAverageDailyPublicBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getAverageDailyPublicBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBackendNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Network_Component]':

        data = self.client.call(
            self.service,
            'getBackendNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return Component(data)


    def getBackendRouters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getBackendRouters',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getBandwidthAllocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getBandwidthAllocation',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBandwidthAllotmentDetail(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Version1_Allotment_Detail':

        data = self.client.call(
            self.service,
            'getBandwidthAllotmentDetail',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment.Detail import Detail
        return Detail(data)


    def getBillingCycleBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Usage]':

        data = self.client.call(
            self.service,
            'getBillingCycleBandwidthUsage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Usage import Usage
        return Usage(data)


    def getBillingCyclePrivateBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Usage':

        data = self.client.call(
            self.service,
            'getBillingCyclePrivateBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Usage import Usage
        return Usage(data)


    def getBillingCyclePublicBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Usage':

        data = self.client.call(
            self.service,
            'getBillingCyclePublicBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Usage import Usage
        return Usage(data)


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Virtual.Guest import Guest
        return Guest(data)


    def getBlockCancelBecauseDisconnectedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getBlockCancelBecauseDisconnectedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBlockDeviceTemplateGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':

        data = self.client.call(
            self.service,
            'getBlockDeviceTemplateGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getBlockDevices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device]':

        data = self.client.call(
            self.service,
            'getBlockDevices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device import Device
        return Device(data)


    def getBrowserConsoleAccessLogs(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_BrowserConsoleAccessLog]':

        data = self.client.call(
            self.service,
            'getBrowserConsoleAccessLogs',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.BrowserConsoleAccessLog import BrowserConsoleAccessLog
        return BrowserConsoleAccessLog(data)


    def getConsoleData(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Container_Virtual_ConsoleData':

        data = self.client.call(
            self.service,
            'getConsoleData',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Container.Virtual.ConsoleData import ConsoleData
        return ConsoleData(data)


    def getConsoleIpAddressFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getConsoleIpAddressFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getConsoleIpAddressRecord(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Network_Component_IpAddress':

        data = self.client.call(
            self.service,
            'getConsoleIpAddressRecord',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component.IpAddress import IpAddress
        return IpAddress(data)


    def getContinuousDataProtectionSoftwareComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component':

        data = self.client.call(
            self.service,
            'getContinuousDataProtectionSoftwareComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getControlPanel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component':

        data = self.client.call(
            self.service,
            'getControlPanel',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getCurrentBandwidthSummary(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object_Bandwidth_Summary':

        data = self.client.call(
            self.service,
            'getCurrentBandwidthSummary',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Bandwidth.Summary import Summary
        return Summary(data)


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


    def getDedicatedHost(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_DedicatedHost':

        data = self.client.call(
            self.service,
            'getDedicatedHost',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.DedicatedHost import DedicatedHost
        return DedicatedHost(data)


    def getDeviceStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Device_Status':

        data = self.client.call(
            self.service,
            'getDeviceStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Device.Status import Status
        return Status(data)


    def getEvaultNetworkStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getEvaultNetworkStorage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getFirewallServiceComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Component_Firewall':

        data = self.client.call(
            self.service,
            'getFirewallServiceComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component.Firewall import Firewall
        return Firewall(data)


    def getFrontendNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Network_Component]':

        data = self.client.call(
            self.service,
            'getFrontendNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return Component(data)


    def getFrontendRouters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getFrontendRouters',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getGlobalIdentifier(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getGlobalIdentifier',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getGpuCount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getGpuCount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getGpuType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getGpuType',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getGuestBootParameter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Boot_Parameter':

        data = self.client.call(
            self.service,
            'getGuestBootParameter',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Boot.Parameter import Parameter
        return Parameter(data)


    def getHardwareFunctionDescription(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getHardwareFunctionDescription',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHost(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Host':

        data = self.client.call(
            self.service,
            'getHost',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Host import Host
        return Host(data)


    def getHostIpsSoftwareComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component':

        data = self.client.call(
            self.service,
            'getHostIpsSoftwareComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getHourlyBillingFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHourlyBillingFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInboundPrivateBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInboundPrivateBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInboundPublicBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInboundPublicBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInternalTagReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':

        data = self.client.call(
            self.service,
            'getInternalTagReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return Reference(data)


    def getLastKnownPowerState(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Power_State':

        data = self.client.call(
            self.service,
            'getLastKnownPowerState',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Power.State import State
        return State(data)


    def getLastOperatingSystemReload(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'getLastOperatingSystemReload',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getLastTransaction(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'getLastTransaction',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getLatestNetworkMonitorIncident(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Monitor_Version1_Incident':

        data = self.client.call(
            self.service,
            'getLatestNetworkMonitorIncident',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Incident import Incident
        return Incident(data)


    def getLocalDiskFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getLocalDiskFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getLocation',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


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


    def getMetricTrackingObjectId(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getMetricTrackingObjectId',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMonitoringRobot(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Monitoring_Robot':

        data = self.client.call(
            self.service,
            'getMonitoringRobot',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Monitoring.Robot import Robot
        return Robot(data)


    def getMonitoringServiceComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Monitor_Version1_Query_Host_Stratum':

        data = self.client.call(
            self.service,
            'getMonitoringServiceComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Host.Stratum import Stratum
        return Stratum(data)


    def getMonitoringServiceEligibilityFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getMonitoringServiceEligibilityFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMonitoringUserNotification(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Notification_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getMonitoringUserNotification',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Notification.Virtual.Guest import Guest
        return Guest(data)


    def getNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Network_Component]':

        data = self.client.call(
            self.service,
            'getNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return Component(data)


    def getNetworkMonitorIncidents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Incident]':

        data = self.client.call(
            self.service,
            'getNetworkMonitorIncidents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Incident import Incident
        return Incident(data)


    def getNetworkMonitors(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Query_Host]':

        data = self.client.call(
            self.service,
            'getNetworkMonitors',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Host import Host
        return Host(data)


    def getNetworkStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getNetworkStorage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getNetworkVlans(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Vlan]':

        data = self.client.call(
            self.service,
            'getNetworkVlans',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getOpenCancellationTicket(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket':

        data = self.client.call(
            self.service,
            'getOpenCancellationTicket',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOperatingSystem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component_OperatingSystem':

        data = self.client.call(
            self.service,
            'getOperatingSystem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component.OperatingSystem import OperatingSystem
        return OperatingSystem(data)


    def getOperatingSystemReferenceCode(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOperatingSystemReferenceCode',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderedPackageId(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOrderedPackageId',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOutboundPrivateBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOutboundPrivateBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOutboundPublicBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOutboundPublicBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOverBandwidthAllocationFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getOverBandwidthAllocationFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPendingMigrationFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPendingMigrationFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPlacementGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_PlacementGroup':

        data = self.client.call(
            self.service,
            'getPlacementGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.PlacementGroup import PlacementGroup
        return PlacementGroup(data)


    def getPowerState(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Power_State':

        data = self.client.call(
            self.service,
            'getPowerState',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Power.State import State
        return State(data)


    def getPrimaryBackendIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPrimaryBackendIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPrimaryBackendNetworkComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Network_Component':

        data = self.client.call(
            self.service,
            'getPrimaryBackendNetworkComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return Component(data)


    def getPrimaryIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPrimaryIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPrimaryNetworkComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Network_Component':

        data = self.client.call(
            self.service,
            'getPrimaryNetworkComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return Component(data)


    def getPrivateNetworkOnlyFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPrivateNetworkOnlyFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getProjectedOverBandwidthAllocationFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getProjectedOverBandwidthAllocationFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getProjectedPublicBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getProjectedPublicBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getRecentEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Event]':

        data = self.client.call(
            self.service,
            'getRecentEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event import Event
        return Event(data)


    def getRegionalGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Group_Regional':

        data = self.client.call(
            self.service,
            'getRegionalGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Group.Regional import Regional
        return Regional(data)


    def getRegionalInternetRegistry(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Regional_Internet_Registry':

        data = self.client.call(
            self.service,
            'getRegionalInternetRegistry',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Regional.Internet.Registry import Registry
        return Registry(data)


    def getReservedCapacityGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_ReservedCapacityGroup':

        data = self.client.call(
            self.service,
            'getReservedCapacityGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup import ReservedCapacityGroup
        return ReservedCapacityGroup(data)


    def getReservedCapacityGroupFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getReservedCapacityGroupFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getReservedCapacityGroupInstance(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_ReservedCapacityGroup_Instance':

        data = self.client.call(
            self.service,
            'getReservedCapacityGroupInstance',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup.Instance import Instance
        return Instance(data)


    def getSecurityScanRequests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Security_Scanner_Request]':

        data = self.client.call(
            self.service,
            'getSecurityScanRequests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Security.Scanner.Request import Request
        return Request(data)


    def getServerRoom(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getServerRoom',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getSoftwareComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_Component]':

        data = self.client.call(
            self.service,
            'getSoftwareComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getSshKeys(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Security_Ssh_Key]':

        data = self.client.call(
            self.service,
            'getSshKeys',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Security.Ssh.Key import Key
        return Key(data)


    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Status import Status
        return Status(data)


    def getTagReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':

        data = self.client.call(
            self.service,
            'getTagReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return Reference(data)


    def getTransientGuestFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getTransientGuestFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTransientWebhookURI(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Attribute':

        data = self.client.call(
            self.service,
            'getTransientWebhookURI',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Attribute import Attribute
        return Attribute(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Type import Type
        return Type(data)


    def getUpgradeRequest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Upgrade_Request':

        data = self.client.call(
            self.service,
            'getUpgradeRequest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Upgrade.Request import Request
        return Request(data)


    def getUserData(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Attribute]':

        data = self.client.call(
            self.service,
            'getUserData',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Attribute import Attribute
        return Attribute(data)


    def getUsers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':

        data = self.client.call(
            self.service,
            'getUsers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getVirtualRack(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Version1_Allotment':

        data = self.client.call(
            self.service,
            'getVirtualRack',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getVirtualRackId(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getVirtualRackId',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getVirtualRackName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getVirtualRackName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


