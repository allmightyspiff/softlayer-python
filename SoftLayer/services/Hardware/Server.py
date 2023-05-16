# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Hardware_Server(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Hardware_Server'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def activatePrivatePort(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'activatePrivatePort',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def activatePublicPort(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'activatePublicPort',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def bootToRescueLayer(
        self,
        noOsBootEnvironment: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'bootToRescueLayer',
            noOsBootEnvironment
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def createFirmwareReflashTransaction(
        self,
        ipmi: int,
        raidController: int,
        bios: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'createFirmwareReflashTransaction',
            ipmi,
            raidController,
            bios
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def createFirmwareUpdateTransaction(
        self,
        ipmi: int,
        raidController: int,
        bios: int,
        harddrive: int,
        networkCard: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'createFirmwareUpdateTransaction',
            ipmi,
            raidController,
            bios,
            harddrive,
            networkCard
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def createHyperThreadingUpdateTransaction(
        self,
        disableHyperthreading: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'createHyperThreadingUpdateTransaction',
            disableHyperthreading
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Hardware_Server,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Hardware_Server':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Hardware.Server import Server
        return SL_Server(data)

# This file was automatically generated with tools/generateTypes.py
    def createPostSoftwareInstallTransaction(
        self,
        installCodes: str,
        returnBoolean: boolean
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'createPostSoftwareInstallTransaction',
            installCodes,
            returnBoolean
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Hardware_Server
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getBackendBandwidthUsage(
        self,
        startDate: dateTime,
        endDate: dateTime
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':
        data = self.client.call(
            self.service,
            'getBackendBandwidthUsage',
            startDate,
            endDate
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
    def getBandwidthImage(
        self,
        networkType: enum,
        snapshotRange: enum,
        draw: boolean,
        dateSpecified: dateTime,
        dateSpecifiedEnd: dateTime
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':
        data = self.client.call(
            self.service,
            'getBandwidthImage',
            networkType,
            snapshotRange,
            draw,
            dateSpecified,
            dateSpecifiedEnd
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return SL_GraphOutputs(data)

# This file was automatically generated with tools/generateTypes.py
    def getBootModeOptions(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getBootModeOptions',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCurrentBenchmarkCertificationResultFile(
        self,
        
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getCurrentBenchmarkCertificationResultFile',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Graph(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
    def getFrontendBandwidthUsage(
        self,
        startDate: dateTime,
        endDate: dateTime
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':
        data = self.client.call(
            self.service,
            'getFrontendBandwidthUsage',
            startDate,
            endDate
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
    def getHardwareByIpAddress(
        self,
        ipAddress: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Hardware_Server':
        data = self.client.call(
            self.service,
            'getHardwareByIpAddress',
            ipAddress,
            mask=objectMask
        )
        from SoftLayer.datatypes.Hardware.Server import Server
        return SL_Server(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
    def getManagementNetworkComponent(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Component':
        data = self.client.call(
            self.service,
            'getManagementNetworkComponent',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_IpAddress(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Server':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Server import Server
        return SL_Server(data)

# This file was automatically generated with tools/generateTypes.py
    def getPMInfo(
        self,
        
    ) -> 'list[SoftLayer_Container_RemoteManagement_PmInfo]':
        data = self.client.call(
            self.service,
            'getPMInfo',
            
        )
        from SoftLayer.datatypes.Container.RemoteManagement.PmInfo import PmInfo
        return SL_PmInfo(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrimaryDriveSize(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getPrimaryDriveSize',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPrivateBandwidthDataSummary(
        self,
        
    ) -> 'SoftLayer_Container_Network_Bandwidth_Data_Summary':
        data = self.client.call(
            self.service,
            'getPrivateBandwidthDataSummary',
            
        )
        from SoftLayer.datatypes.Container.Network.Bandwidth.Data.Summary import Summary
        return SL_Summary(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrivateBandwidthGraphImage(
        self,
        startTime: str,
        endTime: str
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getPrivateBandwidthGraphImage',
            startTime,
            endTime
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPrivateNetworkComponent(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Component':
        data = self.client.call(
            self.service,
            'getPrivateNetworkComponent',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrivateVlan(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Vlan':
        data = self.client.call(
            self.service,
            'getPrivateVlan',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrivateVlanByIpAddress(
        self,
        ipAddress: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Vlan':
        data = self.client.call(
            self.service,
            'getPrivateVlanByIpAddress',
            ipAddress,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
    def getProvisionDate(
        self,
        
    ) -> 'dateTime':
        data = self.client.call(
            self.service,
            'getProvisionDate',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPublicBandwidthDataSummary(
        self,
        
    ) -> 'SoftLayer_Container_Network_Bandwidth_Data_Summary':
        data = self.client.call(
            self.service,
            'getPublicBandwidthDataSummary',
            
        )
        from SoftLayer.datatypes.Container.Network.Bandwidth.Data.Summary import Summary
        return SL_Summary(data)

# This file was automatically generated with tools/generateTypes.py
    def getPublicBandwidthGraphImage(
        self,
        startTime: dateTime,
        endTime: dateTime
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getPublicBandwidthGraphImage',
            startTime,
            endTime
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPublicBandwidthTotal(
        self,
        startTime: int,
        endTime: int
    ) -> 'unsignedLong':
        data = self.client.call(
            self.service,
            'getPublicBandwidthTotal',
            startTime,
            endTime
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPublicNetworkComponent(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Component':
        data = self.client.call(
            self.service,
            'getPublicNetworkComponent',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getPublicVlan(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Vlan':
        data = self.client.call(
            self.service,
            'getPublicVlan',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
    def getPublicVlanByHostname(
        self,
        hostname: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Vlan':
        data = self.client.call(
            self.service,
            'getPublicVlanByHostname',
            hostname,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Domain(data)

# This file was automatically generated with tools/generateTypes.py
    def getSensorData(
        self,
        
    ) -> 'list[SoftLayer_Container_RemoteManagement_SensorReading]':
        data = self.client.call(
            self.service,
            'getSensorData',
            
        )
        from SoftLayer.datatypes.Container.RemoteManagement.SensorReading import SensorReading
        return SL_SensorReading(data)

# This file was automatically generated with tools/generateTypes.py
    def getSensorDataWithGraphs(
        self,
        
    ) -> 'SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs':
        data = self.client.call(
            self.service,
            'getSensorDataWithGraphs',
            
        )
        from SoftLayer.datatypes.Container.RemoteManagement.SensorReadingsWithGraphs import SensorReadingsWithGraphs
        return SL_SensorReadingsWithGraphs(data)

# This file was automatically generated with tools/generateTypes.py
    def getServerDetails(
        self,
        
    ) -> 'SoftLayer_Container_Hardware_Server_Details':
        data = self.client.call(
            self.service,
            'getServerDetails',
            
        )
        from SoftLayer.datatypes.Container.Hardware.Server.Details import Details
        return SL_Details(data)

# This file was automatically generated with tools/generateTypes.py
    def getServerFanSpeedGraphs(
        self,
        
    ) -> 'list[SoftLayer_Container_RemoteManagement_Graphs_SensorSpeed]':
        data = self.client.call(
            self.service,
            'getServerFanSpeedGraphs',
            
        )
        from SoftLayer.datatypes.Container.RemoteManagement.Graphs.SensorSpeed import SensorSpeed
        return SL_SensorSpeed(data)

# This file was automatically generated with tools/generateTypes.py
    def getServerPowerState(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getServerPowerState',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getServerTemperatureGraphs(
        self,
        
    ) -> 'list[SoftLayer_Container_RemoteManagement_Graphs_SensorTemperature]':
        data = self.client.call(
            self.service,
            'getServerTemperatureGraphs',
            
        )
        from SoftLayer.datatypes.Container.RemoteManagement.Graphs.SensorTemperature import SensorTemperature
        return SL_SensorTemperature(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getWindowsUpdateAvailableUpdates(
        self,
        
    ) -> 'list[SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem]':
        data = self.client.call(
            self.service,
            'getWindowsUpdateAvailableUpdates',
            
        )
        from SoftLayer.datatypes.Container.Utility.Microsoft.Windows.UpdateServices.UpdateItem import UpdateItem
        return SL_UpdateItem(data)

# This file was automatically generated with tools/generateTypes.py
    def getWindowsUpdateInstalledUpdates(
        self,
        
    ) -> 'list[SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem]':
        data = self.client.call(
            self.service,
            'getWindowsUpdateInstalledUpdates',
            
        )
        from SoftLayer.datatypes.Container.Utility.Microsoft.Windows.UpdateServices.UpdateItem import UpdateItem
        return SL_UpdateItem(data)

# This file was automatically generated with tools/generateTypes.py
    def getWindowsUpdateStatus(
        self,
        
    ) -> 'SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status':
        data = self.client.call(
            self.service,
            'getWindowsUpdateStatus',
            
        )
        from SoftLayer.datatypes.Container.Utility.Microsoft.Windows.UpdateServices.Status import Status
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
    def initiateIderaBareMetalRestore(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'initiateIderaBareMetalRestore',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def initiateR1SoftBareMetalRestore(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'initiateR1SoftBareMetalRestore',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def isBackendPingable(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isBackendPingable',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def isPingable(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isPingable',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def isWindowsServer(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isWindowsServer',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def massFirmwareReflash(
        self,
        hardwareIds: int,
        ipmi: boolean,
        raidController: boolean,
        bios: boolean
    ) -> 'list[SoftLayer_Container_Hardware_Server_Request]':
        data = self.client.call(
            self.service,
            'massFirmwareReflash',
            hardwareIds,
            ipmi,
            raidController,
            bios
        )
        from SoftLayer.datatypes.Container.Hardware.Server.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def massFirmwareUpdate(
        self,
        hardwareIds: int,
        ipmi: boolean,
        raidController: boolean,
        bios: boolean,
        harddrive: boolean,
        networkCard: boolean
    ) -> 'list[SoftLayer_Container_Hardware_Server_Request]':
        data = self.client.call(
            self.service,
            'massFirmwareUpdate',
            hardwareIds,
            ipmi,
            raidController,
            bios,
            harddrive,
            networkCard
        )
        from SoftLayer.datatypes.Container.Hardware.Server.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def massHyperThreadingUpdate(
        self,
        hardwareIds: int,
        disableHyperthreading: boolean
    ) -> 'list[SoftLayer_Container_Hardware_Server_Request]':
        data = self.client.call(
            self.service,
            'massHyperThreadingUpdate',
            hardwareIds,
            disableHyperthreading
        )
        from SoftLayer.datatypes.Container.Hardware.Server.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def massReloadOperatingSystem(
        self,
        hardwareIds: str,
        token: str,
        config: SoftLayer_Container_Hardware_Server_Configuration
    ) -> 'string':
        data = self.client.call(
            self.service,
            'massReloadOperatingSystem',
            hardwareIds,
            token,
            config
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def massSparePool(
        self,
        hardwareIds: str,
        action: str,
        newOrder: boolean
    ) -> 'list[SoftLayer_Container_Hardware_Server_Request]':
        data = self.client.call(
            self.service,
            'massSparePool',
            hardwareIds,
            action,
            newOrder
        )
        from SoftLayer.datatypes.Container.Hardware.Server.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def ping(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'ping',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def populateServerRam(
        self,
        ramSerialString: str
    ) -> 'void':
        data = self.client.call(
            self.service,
            'populateServerRam',
            ramSerialString
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def powerCycle(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'powerCycle',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def powerOff(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'powerOff',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def powerOn(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'powerOn',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def rebootDefault(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'rebootDefault',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def rebootHard(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'rebootHard',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def rebootSoft(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'rebootSoft',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def reloadCurrentOperatingSystemConfiguration(
        self,
        token: str
    ) -> 'string':
        data = self.client.call(
            self.service,
            'reloadCurrentOperatingSystemConfiguration',
            token
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def runPassmarkCertificationBenchmark(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'runPassmarkCertificationBenchmark',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def setOperatingSystemPassword(
        self,
        newPassword: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'setOperatingSystemPassword',
            newPassword
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def setPrivateNetworkInterfaceSpeed(
        self,
        newSpeed: int,
        redundancy: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'setPrivateNetworkInterfaceSpeed',
            newSpeed,
            redundancy
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def setPublicNetworkInterfaceSpeed(
        self,
        newSpeed: int,
        redundancy: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'setPublicNetworkInterfaceSpeed',
            newSpeed,
            redundancy
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def setUserMetadata(
        self,
        metadata: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Hardware_Attribute]':
        data = self.client.call(
            self.service,
            'setUserMetadata',
            metadata,
            mask=objectMask
        )
        from SoftLayer.datatypes.Hardware.Attribute import Attribute
        return SL_Attribute(data)

# This file was automatically generated with tools/generateTypes.py
    def shutdownPrivatePort(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'shutdownPrivatePort',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def shutdownPublicPort(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'shutdownPublicPort',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def sparePool(
        self,
        action: str,
        newOrder: boolean
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'sparePool',
            action,
            newOrder
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def testRaidAlertService(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'testRaidAlertService',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def toggleManagementInterface(
        self,
        enabled: boolean
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'toggleManagementInterface',
            enabled
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def updateIpmiPassword(
        self,
        password: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'updateIpmiPassword',
            password
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def validatePartitionsForOperatingSystem(
        self,
        operatingSystem: SoftLayer_Software_Description,
        partitions: SoftLayer_Hardware_Component_Partition
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'validatePartitionsForOperatingSystem',
            operatingSystem,
            partitions
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteObject(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def deleteSoftwareComponentPasswords(
        self,
        softwareComponentPasswords: SoftLayer_Software_Component_Password
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteSoftwareComponentPasswords',
            softwareComponentPasswords
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def editSoftwareComponentPasswords(
        self,
        softwareComponentPasswords: SoftLayer_Software_Component_Password
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editSoftwareComponentPasswords',
            softwareComponentPasswords
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def findByIpAddress(
        self,
        ipAddress: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Hardware':
        data = self.client.call(
            self.service,
            'findByIpAddress',
            ipAddress,
            mask=objectMask
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def generateOrderTemplate(
        self,
        templateObject: SoftLayer_Hardware
    ) -> 'SoftLayer_Container_Product_Order':
        data = self.client.call(
            self.service,
            'generateOrderTemplate',
            templateObject
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return SL_Order(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Storage(data)

# This file was automatically generated with tools/generateTypes.py
    def getAvailableBillingTermChangePrices(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':
        data = self.client.call(
            self.service,
            'getAvailableBillingTermChangePrices',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return SL_Price(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Storage(data)

# This file was automatically generated with tools/generateTypes.py
    def getBackendIncomingBandwidth(
        self,
        startDate: dateTime,
        endDate: dateTime
    ) -> 'float':
        data = self.client.call(
            self.service,
            'getBackendIncomingBandwidth',
            startDate,
            endDate
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getBackendOutgoingBandwidth(
        self,
        startDate: dateTime,
        endDate: dateTime
    ) -> 'float':
        data = self.client.call(
            self.service,
            'getBackendOutgoingBandwidth',
            startDate,
            endDate
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getComponentDetailsXML(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getComponentDetailsXML',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCreateObjectOptions(
        self,
        
    ) -> 'SoftLayer_Container_Hardware_Configuration':
        data = self.client.call(
            self.service,
            'getCreateObjectOptions',
            
        )
        from SoftLayer.datatypes.Container.Hardware.Configuration import Configuration
        return SL_Configuration(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
    def getCurrentBillingTotal(
        self,
        
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getCurrentBillingTotal',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDailyAverage(
        self,
        startDate: dateTime,
        endDate: dateTime
    ) -> 'float':
        data = self.client.call(
            self.service,
            'getDailyAverage',
            startDate,
            endDate
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getFrontendIncomingBandwidth(
        self,
        startDate: dateTime,
        endDate: dateTime
    ) -> 'float':
        data = self.client.call(
            self.service,
            'getFrontendIncomingBandwidth',
            startDate,
            endDate
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getFrontendOutgoingBandwidth(
        self,
        startDate: dateTime,
        endDate: dateTime
    ) -> 'float':
        data = self.client.call(
            self.service,
            'getFrontendOutgoingBandwidth',
            startDate,
            endDate
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getHourlyBandwidth(
        self,
        mode: str,
        day: dateTime
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':
        data = self.client.call(
            self.service,
            'getHourlyBandwidth',
            mode,
            day
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrivateBandwidthData(
        self,
        startTime: int,
        endTime: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':
        data = self.client.call(
            self.service,
            'getPrivateBandwidthData',
            startTime,
            endTime
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
    def getPublicBandwidthData(
        self,
        startTime: int,
        endTime: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':
        data = self.client.call(
            self.service,
            'getPublicBandwidthData',
            startTime,
            endTime
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
    def getTransactionHistory(
        self,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Provisioning_Version1_Transaction_History]':
        data = self.client.call(
            self.service,
            'getTransactionHistory',
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction.History import History
        return SL_History(data)

# This file was automatically generated with tools/generateTypes.py
    def getUpgradeItemPrices(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':
        data = self.client.call(
            self.service,
            'getUpgradeItemPrices',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return SL_Price(data)

# This file was automatically generated with tools/generateTypes.py
    def importVirtualHost(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Host':
        data = self.client.call(
            self.service,
            'importVirtualHost',
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Host import Host
        return SL_Host(data)

# This file was automatically generated with tools/generateTypes.py
    def refreshDeviceStatus(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Hardware_State':
        data = self.client.call(
            self.service,
            'refreshDeviceStatus',
            mask=objectMask
        )
        from SoftLayer.datatypes.Hardware.State import State
        return SL_State(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getActiveNetworkFirewallBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':
        data = self.client.call(
            self.service,
            'getActiveNetworkFirewallBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Transaction(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Transaction(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Stratum(data)

# This file was automatically generated with tools/generateTypes.py
    def getAverageDailyBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':
        data = self.client.call(
            self.service,
            'getAverageDailyBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Usage(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Usage(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Usage(data)

# This file was automatically generated with tools/generateTypes.py
    def getBiosPasswordNullFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getBiosPasswordNullFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCaptureEnabledFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Container_Hardware_CaptureEnabled':
        data = self.client.call(
            self.service,
            'getCaptureEnabledFlag',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Container.Hardware.CaptureEnabled import CaptureEnabled
        return SL_CaptureEnabled(data)

# This file was automatically generated with tools/generateTypes.py
    def getContainsSolidStateDrivesFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getContainsSolidStateDrivesFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getControlPanel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component_ControlPanel':
        data = self.client.call(
            self.service,
            'getControlPanel',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component.ControlPanel import ControlPanel
        return SL_ControlPanel(data)

# This file was automatically generated with tools/generateTypes.py
    def getCost(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':
        data = self.client.call(
            self.service,
            'getCost',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Summary(data)

# This file was automatically generated with tools/generateTypes.py
    def getCustomerInstalledOperatingSystemFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getCustomerInstalledOperatingSystemFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCustomerOwnedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getCustomerOwnedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getHasSingleRootVirtualizationBillingItemFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getHasSingleRootVirtualizationBillingItemFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getIsCloudReadyNodeCertified(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getIsCloudReadyNodeCertified',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getIsIpmiDisabled(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getIsIpmiDisabled',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getIsVirtualPrivateCloudNode(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getIsVirtualPrivateCloudNode',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Transaction(data)

# This file was automatically generated with tools/generateTypes.py
    def getLogicalVolumeStorageGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Storage_Group]':
        data = self.client.call(
            self.service,
            'getLogicalVolumeStorageGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Storage.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getMonitoringUserNotification(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Notification_Hardware]':
        data = self.client.call(
            self.service,
            'getMonitoringUserNotification',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Notification.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getPartitions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Server_Partition]':
        data = self.client.call(
            self.service,
            'getPartitions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Server.Partition import Partition
        return SL_Partition(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrivateBackendNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Component]':
        data = self.client.call(
            self.service,
            'getPrivateBackendNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrivateIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPrivateIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getReadyNodeFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getReadyNodeFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getRecentRemoteManagementCommands(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_RemoteManagement_Command_Request]':
        data = self.client.call(
            self.service,
            'getRecentRemoteManagementCommands',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.RemoteManagement.Command.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Registry(data)

# This file was automatically generated with tools/generateTypes.py
    def getRemoteManagement(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component_RemoteManagement':
        data = self.client.call(
            self.service,
            'getRemoteManagement',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component.RemoteManagement import RemoteManagement
        return SL_RemoteManagement(data)

# This file was automatically generated with tools/generateTypes.py
    def getRemoteManagementUsers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_RemoteManagement_User]':
        data = self.client.call(
            self.service,
            'getRemoteManagementUsers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.RemoteManagement.User import User
        return SL_User(data)

# This file was automatically generated with tools/generateTypes.py
    def getSoftwareGuardExtensionEnabled(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getSoftwareGuardExtensionEnabled',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getStatisticsRemoteManagement(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component_RemoteManagement':
        data = self.client.call(
            self.service,
            'getStatisticsRemoteManagement',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component.RemoteManagement import RemoteManagement
        return SL_RemoteManagement(data)

# This file was automatically generated with tools/generateTypes.py
    def getUefiBootFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getUefiBootFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Customer(data)

# This file was automatically generated with tools/generateTypes.py
    def getVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':
        data = self.client.call(
            self.service,
            'getVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return SL_Guest(data)

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
    def getActiveComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':
        data = self.client.call(
            self.service,
            'getActiveComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Incident(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllPowerComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Power_Component]':
        data = self.client.call(
            self.service,
            'getAllPowerComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Power.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Host(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Storage(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Storage(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Attribute]':
        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Attribute import Attribute
        return SL_Attribute(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getBackendNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Component]':
        data = self.client.call(
            self.service,
            'getBackendNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Detail(data)

# This file was automatically generated with tools/generateTypes.py
    def getBenchmarkCertifications(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Benchmark_Certification]':
        data = self.client.call(
            self.service,
            'getBenchmarkCertifications',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Benchmark.Certification import Certification
        return SL_Certification(data)

# This file was automatically generated with tools/generateTypes.py
    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Hardware':
        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getBillingItemFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getBillingItemFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getBusinessContinuanceInsuranceFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getBusinessContinuanceInsuranceFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getChildrenHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getChildrenHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':
        data = self.client.call(
            self.service,
            'getComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getCurrentBillableBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getCurrentBillableBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

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
    def getDatacenterName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getDatacenterName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDaysInSparePool(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getDaysInSparePool',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDownlinkHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getDownlinkHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getDownlinkNetworkHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getDownlinkNetworkHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getDownlinkServers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getDownlinkServers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getDownlinkVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':
        data = self.client.call(
            self.service,
            'getDownlinkVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return SL_Guest(data)

# This file was automatically generated with tools/generateTypes.py
    def getDownstreamHardwareBindings(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Component_Uplink_Hardware]':
        data = self.client.call(
            self.service,
            'getDownstreamHardwareBindings',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Component.Uplink.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getDownstreamNetworkHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getDownstreamNetworkHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getDownstreamNetworkHardwareWithIncidents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getDownstreamNetworkHardwareWithIncidents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getDownstreamServers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getDownstreamServers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getDownstreamVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':
        data = self.client.call(
            self.service,
            'getDownstreamVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return SL_Guest(data)

# This file was automatically generated with tools/generateTypes.py
    def getDriveControllers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':
        data = self.client.call(
            self.service,
            'getDriveControllers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Storage(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Firewall(data)

# This file was automatically generated with tools/generateTypes.py
    def getFixedConfigurationPreset(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Package_Preset':
        data = self.client.call(
            self.service,
            'getFixedConfigurationPreset',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Package.Preset import Preset
        return SL_Preset(data)

# This file was automatically generated with tools/generateTypes.py
    def getFrontendNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Component]':
        data = self.client.call(
            self.service,
            'getFrontendNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getFrontendRouters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getFrontendRouters',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getFutureBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Hardware':
        data = self.client.call(
            self.service,
            'getFutureBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getHardDrives(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':
        data = self.client.call(
            self.service,
            'getHardDrives',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getHardwareChassis(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Chassis':
        data = self.client.call(
            self.service,
            'getHardwareChassis',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Chassis import Chassis
        return SL_Chassis(data)

# This file was automatically generated with tools/generateTypes.py
    def getHardwareFunction(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Function':
        data = self.client.call(
            self.service,
            'getHardwareFunction',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Function import Function
        return SL_Function(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getHardwareState(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_State':
        data = self.client.call(
            self.service,
            'getHardwareState',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.State import State
        return SL_State(data)

# This file was automatically generated with tools/generateTypes.py
    def getHardwareStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Status':
        data = self.client.call(
            self.service,
            'getHardwareStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Status import Status
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
    def getHasTrustedPlatformModuleBillingItemFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getHasTrustedPlatformModuleBillingItemFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getInboundBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getInboundBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getIsBillingTermChangeAvailableFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getIsBillingTermChangeAvailableFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Transaction(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Incident(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getLocationPathString(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getLocationPathString',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getLockboxNetworkStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage':
        data = self.client.call(
            self.service,
            'getLockboxNetworkStorage',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return SL_Storage(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getMemory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':
        data = self.client.call(
            self.service,
            'getMemory',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getMemoryCapacity(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':
        data = self.client.call(
            self.service,
            'getMemoryCapacity',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Object(data)

# This file was automatically generated with tools/generateTypes.py
    def getModules(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':
        data = self.client.call(
            self.service,
            'getModules',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Robot(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Stratum(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getMotherboard(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component':
        data = self.client.call(
            self.service,
            'getMotherboard',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkCards(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':
        data = self.client.call(
            self.service,
            'getNetworkCards',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Component]':
        data = self.client.call(
            self.service,
            'getNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkGatewayMember(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway_Member':
        data = self.client.call(
            self.service,
            'getNetworkGatewayMember',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway.Member import Member
        return SL_Member(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkGatewayMemberFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getNetworkGatewayMemberFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getNetworkManagementIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getNetworkManagementIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getNetworkMonitorAttachedDownHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getNetworkMonitorAttachedDownHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkMonitorAttachedDownVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':
        data = self.client.call(
            self.service,
            'getNetworkMonitorAttachedDownVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return SL_Guest(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Incident(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Host(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getNetworkStatus',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getNetworkStatusAttribute(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Attribute':
        data = self.client.call(
            self.service,
            'getNetworkStatusAttribute',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Attribute import Attribute
        return SL_Attribute(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Storage(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
    def getNextBillingCycleBandwidthAllocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getNextBillingCycleBandwidthAllocation',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getNotesHistory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Note]':
        data = self.client.call(
            self.service,
            'getNotesHistory',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Note import Note
        return SL_Note(data)

# This file was automatically generated with tools/generateTypes.py
    def getNvRamCapacity(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':
        data = self.client.call(
            self.service,
            'getNvRamCapacity',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getNvRamComponentModels(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Model]':
        data = self.client.call(
            self.service,
            'getNvRamComponentModels',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Model import Model
        return SL_Model(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_OperatingSystem(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getOutboundBandwidthUsage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getOutboundBandwidthUsage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getParentBay(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Blade':
        data = self.client.call(
            self.service,
            'getParentBay',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Blade import Blade
        return SL_Blade(data)

# This file was automatically generated with tools/generateTypes.py
    def getParentHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':
        data = self.client.call(
            self.service,
            'getParentHardware',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getPointOfPresenceLocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':
        data = self.client.call(
            self.service,
            'getPointOfPresenceLocation',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getPowerComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Power_Component]':
        data = self.client.call(
            self.service,
            'getPowerComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Power.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getPowerSupply(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':
        data = self.client.call(
            self.service,
            'getPowerSupply',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getPrimaryBackendNetworkComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Component':
        data = self.client.call(
            self.service,
            'getPrimaryBackendNetworkComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getPrimaryNetworkComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Component':
        data = self.client.call(
            self.service,
            'getPrimaryNetworkComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getProcessorCoreAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':
        data = self.client.call(
            self.service,
            'getProcessorCoreAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getProcessorPhysicalCoreAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':
        data = self.client.call(
            self.service,
            'getProcessorPhysicalCoreAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getProcessors(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':
        data = self.client.call(
            self.service,
            'getProcessors',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getRack(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':
        data = self.client.call(
            self.service,
            'getRack',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getRaidControllers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':
        data = self.client.call(
            self.service,
            'getRaidControllers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Event(data)

# This file was automatically generated with tools/generateTypes.py
    def getRemoteManagementAccounts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_RemoteManagement_User]':
        data = self.client.call(
            self.service,
            'getRemoteManagementAccounts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.RemoteManagement.User import User
        return SL_User(data)

# This file was automatically generated with tools/generateTypes.py
    def getRemoteManagementComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Component':
        data = self.client.call(
            self.service,
            'getRemoteManagementComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getResourceConfigurations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Resource_Configuration]':
        data = self.client.call(
            self.service,
            'getResourceConfigurations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Resource.Configuration import Configuration
        return SL_Configuration(data)

# This file was automatically generated with tools/generateTypes.py
    def getResourceGroupMemberReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group_Member]':
        data = self.client.call(
            self.service,
            'getResourceGroupMemberReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group.Member import Member
        return SL_Member(data)

# This file was automatically generated with tools/generateTypes.py
    def getResourceGroupRoles(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group_Role]':
        data = self.client.call(
            self.service,
            'getResourceGroupRoles',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group.Role import Role
        return SL_Role(data)

# This file was automatically generated with tools/generateTypes.py
    def getResourceGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group]':
        data = self.client.call(
            self.service,
            'getResourceGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getRouters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getRouters',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getServiceProvider(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Service_Provider':
        data = self.client.call(
            self.service,
            'getServiceProvider',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Service.Provider import Provider
        return SL_Provider(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getSparePoolBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Hardware':
        data = self.client.call(
            self.service,
            'getSparePoolBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Key(data)

# This file was automatically generated with tools/generateTypes.py
    def getStorageGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Storage_Group]':
        data = self.client.call(
            self.service,
            'getStorageGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Storage.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getStorageNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Component]':
        data = self.client.call(
            self.service,
            'getStorageNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Reference(data)

# This file was automatically generated with tools/generateTypes.py
    def getTopLevelLocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':
        data = self.client.call(
            self.service,
            'getTopLevelLocation',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def getUpgradeableActiveComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':
        data = self.client.call(
            self.service,
            'getUpgradeableActiveComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getUplinkHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':
        data = self.client.call(
            self.service,
            'getUplinkHardware',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getUplinkNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Component]':
        data = self.client.call(
            self.service,
            'getUplinkNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getUserData(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Attribute]':
        data = self.client.call(
            self.service,
            'getUserData',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Attribute import Attribute
        return SL_Attribute(data)

# This file was automatically generated with tools/generateTypes.py
    def getVirtualChassis(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Group':
        data = self.client.call(
            self.service,
            'getVirtualChassis',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getVirtualChassisSiblings(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getVirtualChassisSiblings',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getVirtualHost(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Host':
        data = self.client.call(
            self.service,
            'getVirtualHost',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Host import Host
        return SL_Host(data)

# This file was automatically generated with tools/generateTypes.py
    def getVirtualLicenses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_VirtualLicense]':
        data = self.client.call(
            self.service,
            'getVirtualLicenses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.VirtualLicense import VirtualLicense
        return SL_VirtualLicense(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Allotment(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getVirtualizationPlatform(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component':
        data = self.client.call(
            self.service,
            'getVirtualizationPlatform',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component import Component
        return SL_Component(data)


