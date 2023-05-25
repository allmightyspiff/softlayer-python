from datetime import datetime
from SoftLayer.sltypes.Hardware import Hardware
from SoftLayer import BaseClient

class Hardware_Server(Hardware):
    """The SoftLayer_Hardware_Server data type contains general information relating to a single SoftLayer server."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Hardware_Server'

    def activatePrivatePort(self, identifier: int) -> bool:
        """Activate a server's private network interface."""
        data = self.client.call('SoftLayer_Hardware_Server', 'activatePrivatePort', id=identifier)
        return data

    def activatePublicPort(self, identifier: int) -> bool:
        """Activate a server's public network interface."""
        data = self.client.call('SoftLayer_Hardware_Server', 'activatePublicPort', id=identifier)
        return data

    def bootToRescueLayer(self, identifier: int, noOsBootEnvironment: str) -> bool:
        """Initiates the Rescue Kernel to bring a server online to troubleshoot system problems."""
        data = self.client.call('SoftLayer_Hardware_Server', 'bootToRescueLayer', noOsBootEnvironment, id=identifier)
        return data

    def createFirmwareReflashTransaction(self, identifier: int, ipmi: int, raidController: int, bios: int) -> bool:
        """Runs firmware reflash on the servers components."""
        data = self.client.call('SoftLayer_Hardware_Server', 'createFirmwareReflashTransaction', ipmi, raidController, bios, id=identifier)
        return data

    def createFirmwareUpdateTransaction(self, identifier: int, ipmi: int, raidController: int, bios: int, harddrive: int, networkCard: int) -> bool:
        """Runs firmware updates on the servers components."""
        data = self.client.call('SoftLayer_Hardware_Server', 'createFirmwareUpdateTransaction', ipmi, raidController, bios, harddrive, networkCard, id=identifier)
        return data

    def createHyperThreadingUpdateTransaction(self, identifier: int, disableHyperthreading: int) -> bool:
        """Runs BIOS update on the server to change the hyper-threading configuration."""
        data = self.client.call('SoftLayer_Hardware_Server', 'createHyperThreadingUpdateTransaction', disableHyperthreading, id=identifier)
        return data

    def createObject(self, templateObject: 'Hardware_Server') -> 'Hardware_Server':
        """Create a new server"""
        data = self.client.call('SoftLayer_Hardware_Server', 'createObject', templateObject)
        return data

    def createPostSoftwareInstallTransaction(self, identifier: int, installCodes: str, returnBoolean: bool) -> bool:
        data = self.client.call('SoftLayer_Hardware_Server', 'createPostSoftwareInstallTransaction', installCodes, returnBoolean, id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Hardware_Server') -> bool:
        """Edit a server's properties"""
        data = self.client.call('SoftLayer_Hardware_Server', 'editObject', templateObject, id=identifier)
        return data

    def getBackendBandwidthUsage(self, identifier: int, startDate: datetime, endDate: datetime) -> list['Metric_Tracking_Object_Data']:
        """Retrieves public bandwidth usage records."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getBackendBandwidthUsage', startDate, endDate, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getBandwidthForDateRange(self, identifier: int, startDate: datetime, endDate: datetime) -> list['Metric_Tracking_Object_Data']:
        """Retrieve bandwidth data from a tracking object."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getBandwidthForDateRange', startDate, endDate, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getBandwidthImage(self, identifier: int, networkType: str, snapshotRange: str, draw: bool, dateSpecified: datetime, dateSpecifiedEnd: datetime) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve a bandwidth image and textual description of that image for this server."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getBandwidthImage', networkType, snapshotRange, draw, dateSpecified, dateSpecifiedEnd, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getBootModeOptions(self, identifier: int) -> list[str]:
        """Retrieve the valid boot modes for this server."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getBootModeOptions', id=identifier)
        return data

    def getCurrentBenchmarkCertificationResultFile(self, identifier: int) -> str:
        """Get the file for the current benchmark certification result, if it exists."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getCurrentBenchmarkCertificationResultFile', id=identifier)
        return data

    def getCustomBandwidthDataByDate(self, identifier: int, graphData: 'Container_Graph') -> 'Container_Graph':
        """Retrieve bandwidth graph by date."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getCustomBandwidthDataByDate', graphData, id=identifier)
        from SoftLayer.sltypes.Container_Graph import Container_Graph
        return data

    def getFirewallProtectableSubnets(self, identifier: int) -> list['Network_Subnet']:
        """Get the subnets associated with this server that are protectable by a network component firewall."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getFirewallProtectableSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getFrontendBandwidthUsage(self, identifier: int, startDate: datetime, endDate: datetime) -> list['Metric_Tracking_Object_Data']:
        """Retrieves public bandwidth usage records."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getFrontendBandwidthUsage', startDate, endDate, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getHardwareByIpAddress(self, ipAddress: str) -> 'Hardware_Server':
        """Retrieve a SoftLayer_Hardware_Server object by IP address."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getHardwareByIpAddress', ipAddress)
        return data

    def getItemPricesFromSoftwareDescriptions(self, identifier: int, softwareDescriptions: 'Software_Description', includeTranslationsFlag: bool, returnAllPricesFlag: bool) -> list['Product_Item']:
        """Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getItemPricesFromSoftwareDescriptions', softwareDescriptions, includeTranslationsFlag, returnAllPricesFlag, id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getManagementNetworkComponent(self, identifier: int) -> 'Network_Component':
        """Retrieve a server's management network component."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getManagementNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getNetworkComponentFirewallProtectableIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """Get the IP addresses associated with this server that are protectable by a network component firewall."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getNetworkComponentFirewallProtectableIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getObject(self, identifier: int) -> 'Hardware_Server':
        """Retrieve a SoftLayer_Hardware_Server record."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getObject', id=identifier)
        return data

    def getPMInfo(self, identifier: int) -> list['Container_RemoteManagement_PmInfo']:
        """Retrieve a server's hardware state via its internal sensors."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPMInfo', id=identifier)
        from SoftLayer.sltypes.Container_RemoteManagement_PmInfo import Container_RemoteManagement_PmInfo
        return data

    def getPrimaryDriveSize(self, identifier: int) -> int:
        data = self.client.call('SoftLayer_Hardware_Server', 'getPrimaryDriveSize', id=identifier)
        return data

    def getPrivateBandwidthDataSummary(self, identifier: int) -> 'Container_Network_Bandwidth_Data_Summary':
        """Retrieve a server's private bandwidth usage summary"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPrivateBandwidthDataSummary', id=identifier)
        from SoftLayer.sltypes.Container_Network_Bandwidth_Data_Summary import Container_Network_Bandwidth_Data_Summary
        return data

    def getPrivateBandwidthGraphImage(self, identifier: int, startTime: str, endTime: str) -> str:
        """Retrieve a graph of a server's private network usage."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPrivateBandwidthGraphImage', startTime, endTime, id=identifier)
        return data

    def getPrivateNetworkComponent(self, identifier: int) -> 'Network_Component':
        """Retrieve a server's private network component."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPrivateNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getPrivateVlan(self, identifier: int) -> 'Network_Vlan':
        """Retrieve the backend VLAN for the primary IP address of the server."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPrivateVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getPrivateVlanByIpAddress(self, ipAddress: str) -> 'Network_Vlan':
        """Retrieve a backend network VLAN by searching for an IP address."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPrivateVlanByIpAddress', ipAddress)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getProvisionDate(self, identifier: int) -> datetime:
        data = self.client.call('SoftLayer_Hardware_Server', 'getProvisionDate', id=identifier)
        return data

    def getPublicBandwidthDataSummary(self, identifier: int) -> 'Container_Network_Bandwidth_Data_Summary':
        """Retrieve a server's public bandwidth usage summary"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPublicBandwidthDataSummary', id=identifier)
        from SoftLayer.sltypes.Container_Network_Bandwidth_Data_Summary import Container_Network_Bandwidth_Data_Summary
        return data

    def getPublicBandwidthGraphImage(self, identifier: int, startTime: datetime, endTime: datetime) -> str:
        """Retrieve a graph of a server's public network usage."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPublicBandwidthGraphImage', startTime, endTime, id=identifier)
        return data

    def getPublicBandwidthTotal(self, identifier: int, startTime: int, endTime: int) -> int:
        """Retrieve total number of public bytes used by a server over time period specified."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPublicBandwidthTotal', startTime, endTime, id=identifier)
        return data

    def getPublicNetworkComponent(self, identifier: int) -> 'Network_Component':
        """Retrieve a server's public network component."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPublicNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getPublicVlan(self, identifier: int) -> 'Network_Vlan':
        """Retrieve the frontend VLAN for the primary IP address of the server"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPublicVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getPublicVlanByHostname(self, hostname: str) -> 'Network_Vlan':
        """Retrieve the frontend VLAN by a server's hostname."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPublicVlanByHostname', hostname)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getReverseDomainRecords(self, identifier: int) -> list['Dns_Domain']:
        """Retrieve the reverse domain records associated with a server."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getReverseDomainRecords', id=identifier)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def getSensorData(self, identifier: int) -> list['Container_RemoteManagement_SensorReading']:
        """Retrieve a server's hardware state via its internal sensors."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getSensorData', id=identifier)
        from SoftLayer.sltypes.Container_RemoteManagement_SensorReading import Container_RemoteManagement_SensorReading
        return data

    def getSensorDataWithGraphs(self, identifier: int) -> 'Container_RemoteManagement_SensorReadingsWithGraphs':
        """Retrieve server's temperature and fan speed graphs as well the sensor raw data."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getSensorDataWithGraphs', id=identifier)
        from SoftLayer.sltypes.Container_RemoteManagement_SensorReadingsWithGraphs import Container_RemoteManagement_SensorReadingsWithGraphs
        return data

    def getServerDetails(self, identifier: int) -> 'Container_Hardware_Server_Details':
        """Retrieve a server's hardware components, software, and network components."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getServerDetails', id=identifier)
        from SoftLayer.sltypes.Container_Hardware_Server_Details import Container_Hardware_Server_Details
        return data

    def getServerFanSpeedGraphs(self, identifier: int) -> list['Container_RemoteManagement_Graphs_SensorSpeed']:
        """Retrieve server's fan speed graphs."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getServerFanSpeedGraphs', id=identifier)
        from SoftLayer.sltypes.Container_RemoteManagement_Graphs_SensorSpeed import Container_RemoteManagement_Graphs_SensorSpeed
        return data

    def getServerPowerState(self, identifier: int) -> str:
        """Retrieves server's power state"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getServerPowerState', id=identifier)
        return data

    def getServerTemperatureGraphs(self, identifier: int) -> list['Container_RemoteManagement_Graphs_SensorTemperature']:
        """Retrieve server's temperature graphs"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getServerTemperatureGraphs', id=identifier)
        from SoftLayer.sltypes.Container_RemoteManagement_Graphs_SensorTemperature import Container_RemoteManagement_Graphs_SensorTemperature
        return data

    def getValidBlockDeviceTemplateGroups(self, identifier: int, visibility: str) -> list['Virtual_Guest_Block_Device_Template_Group']:
        """Return a list of valid block device template groups based on this host"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getValidBlockDeviceTemplateGroups', visibility, id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group import Virtual_Guest_Block_Device_Template_Group
        return data

    def getWindowsUpdateAvailableUpdates(self, identifier: int) -> list['Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem']:
        """Retrieve a list of Windows updates available to a server."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getWindowsUpdateAvailableUpdates', id=identifier)
        from SoftLayer.sltypes.Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem import Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem
        return data

    def getWindowsUpdateInstalledUpdates(self, identifier: int) -> list['Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem']:
        """Retrieve a list of Windows updates installed on a server."""
        data = self.client.call('SoftLayer_Hardware_Server', 'getWindowsUpdateInstalledUpdates', id=identifier)
        from SoftLayer.sltypes.Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem import Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem
        return data

    def getWindowsUpdateStatus(self, identifier: int) -> 'Container_Utility_Microsoft_Windows_UpdateServices_Status':
        """Retrieve a server's Windows update synchronization status"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getWindowsUpdateStatus', id=identifier)
        from SoftLayer.sltypes.Container_Utility_Microsoft_Windows_UpdateServices_Status import Container_Utility_Microsoft_Windows_UpdateServices_Status
        return data

    def initiateIderaBareMetalRestore(self, identifier: int) -> bool:
        """Initiate an Idera bare metal restore for the server tied to an Idera Server Backup"""
        data = self.client.call('SoftLayer_Hardware_Server', 'initiateIderaBareMetalRestore', id=identifier)
        return data

    def initiateR1SoftBareMetalRestore(self, identifier: int) -> bool:
        """Initiate an R1Soft bare metal restore for the server tied to an R1Soft CDP Server"""
        data = self.client.call('SoftLayer_Hardware_Server', 'initiateR1SoftBareMetalRestore', id=identifier)
        return data

    def isBackendPingable(self, identifier: int) -> bool:
        """Verifies if a server's backend ip address is pingable."""
        data = self.client.call('SoftLayer_Hardware_Server', 'isBackendPingable', id=identifier)
        return data

    def isPingable(self, identifier: int) -> bool:
        """Verifies if server is pingable."""
        data = self.client.call('SoftLayer_Hardware_Server', 'isPingable', id=identifier)
        return data

    def isWindowsServer(self, identifier: int) -> bool:
        """Determine if a server runs the Microsoft Windows operating system."""
        data = self.client.call('SoftLayer_Hardware_Server', 'isWindowsServer', id=identifier)
        return data

    def massFirmwareReflash(self, hardwareIds: int, ipmi: bool, raidController: bool, bios: bool) -> list['Container_Hardware_Server_Request']:
        """Runs firmware reflashes on the servers components."""
        data = self.client.call('SoftLayer_Hardware_Server', 'massFirmwareReflash', hardwareIds, ipmi, raidController, bios)
        from SoftLayer.sltypes.Container_Hardware_Server_Request import Container_Hardware_Server_Request
        return data

    def massFirmwareUpdate(self, hardwareIds: int, ipmi: bool, raidController: bool, bios: bool, harddrive: bool, networkCard: bool) -> list['Container_Hardware_Server_Request']:
        """Runs firmware updates on the servers components."""
        data = self.client.call('SoftLayer_Hardware_Server', 'massFirmwareUpdate', hardwareIds, ipmi, raidController, bios, harddrive, networkCard)
        from SoftLayer.sltypes.Container_Hardware_Server_Request import Container_Hardware_Server_Request
        return data

    def massHyperThreadingUpdate(self, hardwareIds: int, disableHyperthreading: bool) -> list['Container_Hardware_Server_Request']:
        """Runs firmware reflashes on the servers components."""
        data = self.client.call('SoftLayer_Hardware_Server', 'massHyperThreadingUpdate', hardwareIds, disableHyperthreading)
        from SoftLayer.sltypes.Container_Hardware_Server_Request import Container_Hardware_Server_Request
        return data

    def massReloadOperatingSystem(self, hardwareIds: str, token: str, config: 'Container_Hardware_Server_Configuration') -> str:
        """Reloads operating system configuration on a set of hardware Ids."""
        data = self.client.call('SoftLayer_Hardware_Server', 'massReloadOperatingSystem', hardwareIds, token, config)
        return data

    def massSparePool(self, hardwareIds: str, action: str, newOrder: bool) -> list['Container_Hardware_Server_Request']:
        """Allows multiple servers to be added to or removed from the spare pool."""
        data = self.client.call('SoftLayer_Hardware_Server', 'massSparePool', hardwareIds, action, newOrder)
        from SoftLayer.sltypes.Container_Hardware_Server_Request import Container_Hardware_Server_Request
        return data

    def ping(self, identifier: int) -> str:
        """Issues ping command."""
        data = self.client.call('SoftLayer_Hardware_Server', 'ping', id=identifier)
        return data

    def populateServerRam(self, identifier: int, ramSerialString: str) -> None:
        data = self.client.call('SoftLayer_Hardware_Server', 'populateServerRam', ramSerialString, id=identifier)
        return data

    def powerCycle(self, identifier: int) -> bool:
        """Issues power cycle to server."""
        data = self.client.call('SoftLayer_Hardware_Server', 'powerCycle', id=identifier)
        return data

    def powerOff(self, identifier: int) -> bool:
        """Power off server."""
        data = self.client.call('SoftLayer_Hardware_Server', 'powerOff', id=identifier)
        return data

    def powerOn(self, identifier: int) -> bool:
        """Power on server."""
        data = self.client.call('SoftLayer_Hardware_Server', 'powerOn', id=identifier)
        return data

    def rebootDefault(self, identifier: int) -> bool:
        """Reboot the server via the default method."""
        data = self.client.call('SoftLayer_Hardware_Server', 'rebootDefault', id=identifier)
        return data

    def rebootHard(self, identifier: int) -> bool:
        """Reboot the server via "hard" reboot."""
        data = self.client.call('SoftLayer_Hardware_Server', 'rebootHard', id=identifier)
        return data

    def rebootSoft(self, identifier: int) -> bool:
        """Reboot the server via gracefully (soft reboot)."""
        data = self.client.call('SoftLayer_Hardware_Server', 'rebootSoft', id=identifier)
        return data

    def reloadCurrentOperatingSystemConfiguration(self, identifier: int, token: str) -> str:
        """Reloads current operating system configuration."""
        data = self.client.call('SoftLayer_Hardware_Server', 'reloadCurrentOperatingSystemConfiguration', token, id=identifier)
        return data

    def reloadOperatingSystem(self, identifier: int, token: str, config: 'Container_Hardware_Server_Configuration') -> str:
        """Reloads operating system configuration."""
        data = self.client.call('SoftLayer_Hardware_Server', 'reloadOperatingSystem', token, config, id=identifier)
        return data

    def runPassmarkCertificationBenchmark(self, identifier: int) -> bool:
        """Runs a hardware stress test on the server to obtain a Passmark Certification."""
        data = self.client.call('SoftLayer_Hardware_Server', 'runPassmarkCertificationBenchmark', id=identifier)
        return data

    def setOperatingSystemPassword(self, identifier: int, newPassword: str) -> bool:
        """Changes the password stored in our system for a servers' Operating System"""
        data = self.client.call('SoftLayer_Hardware_Server', 'setOperatingSystemPassword', newPassword, id=identifier)
        return data

    def setPrivateNetworkInterfaceSpeed(self, identifier: int, newSpeed: int, redundancy: str) -> bool:
        """Set the speed and redundancy configuration of a server's private network interface."""
        data = self.client.call('SoftLayer_Hardware_Server', 'setPrivateNetworkInterfaceSpeed', newSpeed, redundancy, id=identifier)
        return data

    def setPublicNetworkInterfaceSpeed(self, identifier: int, newSpeed: int, redundancy: str) -> bool:
        """Set the speed and redundancy configuration of a server's public network interface."""
        data = self.client.call('SoftLayer_Hardware_Server', 'setPublicNetworkInterfaceSpeed', newSpeed, redundancy, id=identifier)
        return data

    def setUserMetadata(self, identifier: int, metadata: str) -> list['Hardware_Attribute']:
        """Sets the server's user metadata value."""
        data = self.client.call('SoftLayer_Hardware_Server', 'setUserMetadata', metadata, id=identifier)
        from SoftLayer.sltypes.Hardware_Attribute import Hardware_Attribute
        return data

    def shutdownPrivatePort(self, identifier: int) -> bool:
        """Disconnect a server's private network interface."""
        data = self.client.call('SoftLayer_Hardware_Server', 'shutdownPrivatePort', id=identifier)
        return data

    def shutdownPublicPort(self, identifier: int) -> bool:
        """Disconnect a server's public network interface."""
        data = self.client.call('SoftLayer_Hardware_Server', 'shutdownPublicPort', id=identifier)
        return data

    def sparePool(self, identifier: int, action: str, newOrder: bool) -> bool:
        """Allows servers to be added to or removed from the spare pool."""
        data = self.client.call('SoftLayer_Hardware_Server', 'sparePool', action, newOrder, id=identifier)
        return data

    def testRaidAlertService(self, identifier: int) -> bool:
        """Tests the RAID Alert service."""
        data = self.client.call('SoftLayer_Hardware_Server', 'testRaidAlertService', id=identifier)
        return data

    def toggleManagementInterface(self, identifier: int, enabled: bool) -> bool:
        """Toggle the IPMI interface on and off."""
        data = self.client.call('SoftLayer_Hardware_Server', 'toggleManagementInterface', enabled, id=identifier)
        return data

    def updateIpmiPassword(self, identifier: int, password: str) -> bool:
        """Update the root IPMI user password"""
        data = self.client.call('SoftLayer_Hardware_Server', 'updateIpmiPassword', password, id=identifier)
        return data

    def validatePartitionsForOperatingSystem(self, operatingSystem: 'Software_Description', partitions: 'Hardware_Component_Partition') -> bool:
        """Validates a collection of partitions for an operating system"""
        data = self.client.call('SoftLayer_Hardware_Server', 'validatePartitionsForOperatingSystem', operatingSystem, partitions)
        return data

    def getActiveNetworkFirewallBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getActiveNetworkFirewallBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getActiveTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getActiveTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getActiveTransaction(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getActiveTransaction', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getActiveTransactions(self, identifier: int) -> list['Provisioning_Version1_Transaction']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getActiveTransactions', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getAvailableMonitoring(self, identifier: int) -> list['Network_Monitor_Version1_Query_Host_Stratum']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getAvailableMonitoring', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_Host_Stratum import Network_Monitor_Version1_Query_Host_Stratum
        return data

    def getAverageDailyBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getAverageDailyBandwidthUsage', id=identifier)
        return data

    def getAverageDailyPrivateBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getAverageDailyPrivateBandwidthUsage', id=identifier)
        return data

    def getBillingCycleBandwidthUsage(self, identifier: int) -> list['Network_Bandwidth_Usage']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getBillingCycleBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBillingCyclePrivateBandwidthUsage(self, identifier: int) -> 'Network_Bandwidth_Usage':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getBillingCyclePrivateBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBillingCyclePublicBandwidthUsage(self, identifier: int) -> 'Network_Bandwidth_Usage':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getBillingCyclePublicBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBiosPasswordNullFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getBiosPasswordNullFlag', id=identifier)
        return data

    def getCaptureEnabledFlag(self, identifier: int) -> 'Container_Hardware_CaptureEnabled':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getCaptureEnabledFlag', id=identifier)
        from SoftLayer.sltypes.Container_Hardware_CaptureEnabled import Container_Hardware_CaptureEnabled
        return data

    def getContainsSolidStateDrivesFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getContainsSolidStateDrivesFlag', id=identifier)
        return data

    def getControlPanel(self, identifier: int) -> 'Software_Component_ControlPanel':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getControlPanel', id=identifier)
        from SoftLayer.sltypes.Software_Component_ControlPanel import Software_Component_ControlPanel
        return data

    def getCost(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getCost', id=identifier)
        return data

    def getCurrentBandwidthSummary(self, identifier: int) -> 'Metric_Tracking_Object_Bandwidth_Summary':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getCurrentBandwidthSummary', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Bandwidth_Summary import Metric_Tracking_Object_Bandwidth_Summary
        return data

    def getCustomerInstalledOperatingSystemFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getCustomerInstalledOperatingSystemFlag', id=identifier)
        return data

    def getCustomerOwnedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getCustomerOwnedFlag', id=identifier)
        return data

    def getHasSingleRootVirtualizationBillingItemFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getHasSingleRootVirtualizationBillingItemFlag', id=identifier)
        return data

    def getInboundPrivateBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getInboundPrivateBandwidthUsage', id=identifier)
        return data

    def getIsCloudReadyNodeCertified(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getIsCloudReadyNodeCertified', id=identifier)
        return data

    def getIsIpmiDisabled(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getIsIpmiDisabled', id=identifier)
        return data

    def getIsVirtualPrivateCloudNode(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getIsVirtualPrivateCloudNode', id=identifier)
        return data

    def getLastOperatingSystemReload(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getLastOperatingSystemReload', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getLogicalVolumeStorageGroups(self, identifier: int) -> list['Configuration_Storage_Group']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getLogicalVolumeStorageGroups', id=identifier)
        from SoftLayer.sltypes.Configuration_Storage_Group import Configuration_Storage_Group
        return data

    def getMetricTrackingObjectId(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getMetricTrackingObjectId', id=identifier)
        return data

    def getMonitoringUserNotification(self, identifier: int) -> list['User_Customer_Notification_Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getMonitoringUserNotification', id=identifier)
        from SoftLayer.sltypes.User_Customer_Notification_Hardware import User_Customer_Notification_Hardware
        return data

    def getOpenCancellationTicket(self, identifier: int) -> 'Ticket':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getOpenCancellationTicket', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOutboundPrivateBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getOutboundPrivateBandwidthUsage', id=identifier)
        return data

    def getOverBandwidthAllocationFlag(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getOverBandwidthAllocationFlag', id=identifier)
        return data

    def getPartitions(self, identifier: int) -> list['Hardware_Server_Partition']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPartitions', id=identifier)
        from SoftLayer.sltypes.Hardware_Server_Partition import Hardware_Server_Partition
        return data

    def getPrivateBackendNetworkComponents(self, identifier: int) -> list['Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPrivateBackendNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getPrivateIpAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getPrivateIpAddress', id=identifier)
        return data

    def getProjectedOverBandwidthAllocationFlag(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getProjectedOverBandwidthAllocationFlag', id=identifier)
        return data

    def getProjectedPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getProjectedPublicBandwidthUsage', id=identifier)
        return data

    def getReadyNodeFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getReadyNodeFlag', id=identifier)
        return data

    def getRecentRemoteManagementCommands(self, identifier: int) -> list['Hardware_Component_RemoteManagement_Command_Request']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getRecentRemoteManagementCommands', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_RemoteManagement_Command_Request import Hardware_Component_RemoteManagement_Command_Request
        return data

    def getRegionalInternetRegistry(self, identifier: int) -> 'Network_Regional_Internet_Registry':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getRegionalInternetRegistry', id=identifier)
        from SoftLayer.sltypes.Network_Regional_Internet_Registry import Network_Regional_Internet_Registry
        return data

    def getRemoteManagement(self, identifier: int) -> 'Hardware_Component_RemoteManagement':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getRemoteManagement', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_RemoteManagement import Hardware_Component_RemoteManagement
        return data

    def getRemoteManagementUsers(self, identifier: int) -> list['Hardware_Component_RemoteManagement_User']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getRemoteManagementUsers', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_RemoteManagement_User import Hardware_Component_RemoteManagement_User
        return data

    def getSoftwareGuardExtensionEnabled(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getSoftwareGuardExtensionEnabled', id=identifier)
        return data

    def getStatisticsRemoteManagement(self, identifier: int) -> 'Hardware_Component_RemoteManagement':
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getStatisticsRemoteManagement', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_RemoteManagement import Hardware_Component_RemoteManagement
        return data

    def getUefiBootFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getUefiBootFlag', id=identifier)
        return data

    def getUsers(self, identifier: int) -> list['User_Customer']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getUsers', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Server', 'getVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data
