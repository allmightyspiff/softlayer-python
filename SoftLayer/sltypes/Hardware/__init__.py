from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Hardware(Entity):
    """The SoftLayer_Hardware data type contains general information relating to a single SoftLayer hardware."""
    accountId: int
    bareMetalInstanceFlag: int
    domain: str
    fullyQualifiedDomainName: str
    hardwareStatusId: int
    hostname: str
    id_: int
    manufacturerSerialNumber: str
    notes: str
    postInstallScriptUri: str
    provisionDate: datetime
    serialNumber: str
    serviceProviderId: int
    serviceProviderResourceId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Hardware'

    def allowAccessToNetworkStorage(self, identifier: int, networkStorageTemplateObject: 'Network_Storage') -> bool:
        """Allow access to a SoftLayer_Network_Storage volume from this device."""
        data = self.client.call('SoftLayer_Hardware', 'allowAccessToNetworkStorage', networkStorageTemplateObject, id=identifier)
        return data

    def allowAccessToNetworkStorageList(self, identifier: int, networkStorageTemplateObjects: 'Network_Storage') -> bool:
        """Allow access to multiple SoftLayer_Network_Storage volumes from this device."""
        data = self.client.call('SoftLayer_Hardware', 'allowAccessToNetworkStorageList', networkStorageTemplateObjects, id=identifier)
        return data

    def captureImage(self, identifier: int, captureTemplate: 'Container_Disk_Image_Capture_Template') -> 'Virtual_Guest_Block_Device_Template_Group':
        """Captures an Image of the hard disk on the physical machine."""
        data = self.client.call('SoftLayer_Hardware', 'captureImage', captureTemplate, id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group import Virtual_Guest_Block_Device_Template_Group
        return data

    def createObject(self, templateObject: 'Hardware') -> 'Hardware':
        """Create a new server"""
        data = self.client.call('SoftLayer_Hardware', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a server"""
        data = self.client.call('SoftLayer_Hardware', 'deleteObject', id=identifier)
        return data

    def deleteSoftwareComponentPasswords(self, identifier: int, softwareComponentPasswords: 'Software_Component_Password') -> bool:
        """Delete software component passwords."""
        data = self.client.call('SoftLayer_Hardware', 'deleteSoftwareComponentPasswords', softwareComponentPasswords, id=identifier)
        return data

    def deleteTag(self, identifier: int, tagName: str) -> bool:
        """Delete a tag"""
        data = self.client.call('SoftLayer_Hardware', 'deleteTag', tagName, id=identifier)
        return data

    def editSoftwareComponentPasswords(self, identifier: int, softwareComponentPasswords: 'Software_Component_Password') -> bool:
        """Edit the properties of software component passwords."""
        data = self.client.call('SoftLayer_Hardware', 'editSoftwareComponentPasswords', softwareComponentPasswords, id=identifier)
        return data

    def executeRemoteScript(self, identifier: int, uri: str) -> None:
        """Download and run remote script from uri on the hardware. Requires https for script to be executed after
download."""
        data = self.client.call('SoftLayer_Hardware', 'executeRemoteScript', uri, id=identifier)
        return data

    def findByIpAddress(self, ipAddress: str) -> 'Hardware':
        """Find hardware by its primary public or private IP (ipv4) address."""
        data = self.client.call('SoftLayer_Hardware', 'findByIpAddress', ipAddress)
        return data

    def generateOrderTemplate(self, templateObject: 'Hardware') -> 'Container_Product_Order':
        """Obtain an order container for a given template object"""
        data = self.client.call('SoftLayer_Hardware', 'generateOrderTemplate', templateObject)
        from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order
        return data

    def getAttachedNetworkStorages(self, identifier: int, nasType: str) -> list['Network_Storage']:
        """Return a list of SoftLayer_Network_Storage volumes authorized to this device."""
        data = self.client.call('SoftLayer_Hardware', 'getAttachedNetworkStorages', nasType, id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAvailableBillingTermChangePrices(self, identifier: int) -> list['Product_Item_Price']:
        """Retrieves a list of available term prices available to this of hardware."""
        data = self.client.call('SoftLayer_Hardware', 'getAvailableBillingTermChangePrices', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getAvailableNetworkStorages(self, identifier: int, nasType: str) -> list['Network_Storage']:
        """Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device."""
        data = self.client.call('SoftLayer_Hardware', 'getAvailableNetworkStorages', nasType, id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getBackendIncomingBandwidth(self, identifier: int, startDate: datetime, endDate: datetime) -> float:
        """Retrieve the amount of incoming private network bandwidth used by a server over a period of time."""
        data = self.client.call('SoftLayer_Hardware', 'getBackendIncomingBandwidth', startDate, endDate, id=identifier)
        return data

    def getBackendOutgoingBandwidth(self, identifier: int, startDate: datetime, endDate: datetime) -> float:
        """Retrieve the amount of outgoing private network bandwidth used by a server over a period of time."""
        data = self.client.call('SoftLayer_Hardware', 'getBackendOutgoingBandwidth', startDate, endDate, id=identifier)
        return data

    def getComponentDetailsXML(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Hardware', 'getComponentDetailsXML', id=identifier)
        return data

    def getCreateObjectOptions(self) -> 'Container_Hardware_Configuration':
        """Determine options available when creating a server"""
        data = self.client.call('SoftLayer_Hardware', 'getCreateObjectOptions')
        from SoftLayer.sltypes.Container_Hardware_Configuration import Container_Hardware_Configuration
        return data

    def getCurrentBillingDetail(self, identifier: int) -> list['Billing_Item']:
        """<< EOT"""
        data = self.client.call('SoftLayer_Hardware', 'getCurrentBillingDetail', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getCurrentBillingTotal(self, identifier: int) -> float:
        """Get the billing total for this instance's usage up to this point. This total includes all bandwidth charges."""
        data = self.client.call('SoftLayer_Hardware', 'getCurrentBillingTotal', id=identifier)
        return data

    def getDailyAverage(self, identifier: int, startDate: datetime, endDate: datetime) -> float:
        """calculate the average daily network traffic used by a server in gigabytes."""
        data = self.client.call('SoftLayer_Hardware', 'getDailyAverage', startDate, endDate, id=identifier)
        return data

    def getFrontendIncomingBandwidth(self, identifier: int, startDate: datetime, endDate: datetime) -> float:
        """Retrieve the amount of incoming public network bandwidth used by a server over a period of time."""
        data = self.client.call('SoftLayer_Hardware', 'getFrontendIncomingBandwidth', startDate, endDate, id=identifier)
        return data

    def getFrontendOutgoingBandwidth(self, identifier: int, startDate: datetime, endDate: datetime) -> float:
        """Retrieve the amount of outgoing public network bandwidth used by a server over a period of time."""
        data = self.client.call('SoftLayer_Hardware', 'getFrontendOutgoingBandwidth', startDate, endDate, id=identifier)
        return data

    def getHourlyBandwidth(self, identifier: int, mode: str, day: datetime) -> list['Metric_Tracking_Object_Data']:
        """Retrieves bandwidth hourly over a 24-hour period for the specified hardware."""
        data = self.client.call('SoftLayer_Hardware', 'getHourlyBandwidth', mode, day, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getObject(self, identifier: int) -> 'Hardware':
        """Retrieve a SoftLayer_Hardware record."""
        data = self.client.call('SoftLayer_Hardware', 'getObject', id=identifier)
        return data

    def getPrivateBandwidthData(self, identifier: int, startTime: int, endTime: int) -> list['Metric_Tracking_Object_Data']:
        """Retrieve a graph of a server's private network usage."""
        data = self.client.call('SoftLayer_Hardware', 'getPrivateBandwidthData', startTime, endTime, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getPublicBandwidthData(self, identifier: int, startTime: int, endTime: int) -> list['Metric_Tracking_Object_Data']:
        """Retrieve a graph of a server's public network usage."""
        data = self.client.call('SoftLayer_Hardware', 'getPublicBandwidthData', startTime, endTime, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getSensorData(self, identifier: int) -> list['Container_RemoteManagement_SensorReading']:
        """Retrieve a server's hardware state via its internal sensors"""
        data = self.client.call('SoftLayer_Hardware', 'getSensorData', id=identifier)
        from SoftLayer.sltypes.Container_RemoteManagement_SensorReading import Container_RemoteManagement_SensorReading
        return data

    def getSensorDataWithGraphs(self, identifier: int) -> 'Container_RemoteManagement_SensorReadingsWithGraphs':
        """Retrieve server's temperature and fan speed graphs as well the sensor raw data."""
        data = self.client.call('SoftLayer_Hardware', 'getSensorDataWithGraphs', id=identifier)
        from SoftLayer.sltypes.Container_RemoteManagement_SensorReadingsWithGraphs import Container_RemoteManagement_SensorReadingsWithGraphs
        return data

    def getServerFanSpeedGraphs(self, identifier: int) -> list['Container_RemoteManagement_Graphs_SensorSpeed']:
        """Retrieve a server's fan speed graphs."""
        data = self.client.call('SoftLayer_Hardware', 'getServerFanSpeedGraphs', id=identifier)
        from SoftLayer.sltypes.Container_RemoteManagement_Graphs_SensorSpeed import Container_RemoteManagement_Graphs_SensorSpeed
        return data

    def getServerPowerState(self, identifier: int) -> str:
        """Retrieves a server's power state."""
        data = self.client.call('SoftLayer_Hardware', 'getServerPowerState', id=identifier)
        return data

    def getServerTemperatureGraphs(self, identifier: int) -> list['Container_RemoteManagement_Graphs_SensorTemperature']:
        """Retrieve server's temperature graphs"""
        data = self.client.call('SoftLayer_Hardware', 'getServerTemperatureGraphs', id=identifier)
        from SoftLayer.sltypes.Container_RemoteManagement_Graphs_SensorTemperature import Container_RemoteManagement_Graphs_SensorTemperature
        return data

    def getTransactionHistory(self, identifier: int) -> list['Provisioning_Version1_Transaction_History']:
        """Get transaction history for a piece of hardware."""
        data = self.client.call('SoftLayer_Hardware', 'getTransactionHistory', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction_History import Provisioning_Version1_Transaction_History
        return data

    def getUpgradeItemPrices(self, identifier: int) -> list['Product_Item_Price']:
        """Retrieve a list of upgradeable items available to a piece of hardware."""
        data = self.client.call('SoftLayer_Hardware', 'getUpgradeItemPrices', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def importVirtualHost(self, identifier: int) -> 'Virtual_Host':
        """attempt to import the host record for the virtualization platform running on a server"""
        data = self.client.call('SoftLayer_Hardware', 'importVirtualHost', id=identifier)
        from SoftLayer.sltypes.Virtual_Host import Virtual_Host
        return data

    def isPingable(self, identifier: int) -> bool:
        """Verifies whether or not a server is pingable."""
        data = self.client.call('SoftLayer_Hardware', 'isPingable', id=identifier)
        return data

    def ping(self, identifier: int) -> str:
        """Issues ping command."""
        data = self.client.call('SoftLayer_Hardware', 'ping', id=identifier)
        return data

    def powerCycle(self, identifier: int) -> bool:
        """Issues power cycle to server."""
        data = self.client.call('SoftLayer_Hardware', 'powerCycle', id=identifier)
        return data

    def powerOff(self, identifier: int) -> bool:
        """Power off server."""
        data = self.client.call('SoftLayer_Hardware', 'powerOff', id=identifier)
        return data

    def powerOn(self, identifier: int) -> bool:
        """Power on server."""
        data = self.client.call('SoftLayer_Hardware', 'powerOn', id=identifier)
        return data

    def rebootDefault(self, identifier: int) -> bool:
        """Reboot the server via the default method."""
        data = self.client.call('SoftLayer_Hardware', 'rebootDefault', id=identifier)
        return data

    def rebootHard(self, identifier: int) -> bool:
        """Reboot the server via "hard" reboot."""
        data = self.client.call('SoftLayer_Hardware', 'rebootHard', id=identifier)
        return data

    def rebootSoft(self, identifier: int) -> bool:
        """Execute a soft reboot to the server."""
        data = self.client.call('SoftLayer_Hardware', 'rebootSoft', id=identifier)
        return data

    def refreshDeviceStatus(self, identifier: int) -> 'Hardware_State':
        data = self.client.call('SoftLayer_Hardware', 'refreshDeviceStatus', id=identifier)
        from SoftLayer.sltypes.Hardware_State import Hardware_State
        return data

    def removeAccessToNetworkStorage(self, identifier: int, networkStorageTemplateObject: 'Network_Storage') -> bool:
        """Remove access to a SoftLayer_Network_Storage volume from this device."""
        data = self.client.call('SoftLayer_Hardware', 'removeAccessToNetworkStorage', networkStorageTemplateObject, id=identifier)
        return data

    def removeAccessToNetworkStorageList(self, identifier: int, networkStorageTemplateObjects: 'Network_Storage') -> bool:
        """Remove access to multiple SoftLayer_Network_Storage volumes from this device."""
        data = self.client.call('SoftLayer_Hardware', 'removeAccessToNetworkStorageList', networkStorageTemplateObjects, id=identifier)
        return data

    def removeTags(self, identifier: int, tags: str) -> bool:
        """Remove a tag reference"""
        data = self.client.call('SoftLayer_Hardware', 'removeTags', tags, id=identifier)
        return data

    def setTags(self, identifier: int, tags: str) -> bool:
        data = self.client.call('SoftLayer_Hardware', 'setTags', tags, id=identifier)
        return data

    def updateIpmiPassword(self, identifier: int, password: str) -> bool:
        """Update the root IPMI user password"""
        data = self.client.call('SoftLayer_Hardware', 'updateIpmiPassword', password, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getActiveComponents(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getActiveComponents', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getActiveNetworkMonitorIncident(self, identifier: int) -> list['Network_Monitor_Version1_Incident']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getActiveNetworkMonitorIncident', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Incident import Network_Monitor_Version1_Incident
        return data

    def getAllPowerComponents(self, identifier: int) -> list['Hardware_Power_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getAllPowerComponents', id=identifier)
        from SoftLayer.sltypes.Hardware_Power_Component import Hardware_Power_Component
        return data

    def getAllowedHost(self, identifier: int) -> 'Network_Storage_Allowed_Host':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getAllowedHost', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
        return data

    def getAllowedNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getAllowedNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAllowedNetworkStorageReplicas(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getAllowedNetworkStorageReplicas', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAntivirusSpywareSoftwareComponent(self, identifier: int) -> 'Software_Component':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getAntivirusSpywareSoftwareComponent', id=identifier)
        from SoftLayer.sltypes.Software_Component import Software_Component
        return data

    def getAttributes(self, identifier: int) -> list['Hardware_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Hardware_Attribute import Hardware_Attribute
        return data

    def getAverageDailyPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getAverageDailyPublicBandwidthUsage', id=identifier)
        return data

    def getBackendNetworkComponents(self, identifier: int) -> list['Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getBackendNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getBackendRouters(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getBackendRouters', id=identifier)
        return data

    def getBandwidthAllocation(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getBandwidthAllocation', id=identifier)
        return data

    def getBandwidthAllotmentDetail(self, identifier: int) -> 'Network_Bandwidth_Version1_Allotment_Detail':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getBandwidthAllotmentDetail', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment_Detail import Network_Bandwidth_Version1_Allotment_Detail
        return data

    def getBenchmarkCertifications(self, identifier: int) -> list['Hardware_Benchmark_Certification']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getBenchmarkCertifications', id=identifier)
        from SoftLayer.sltypes.Hardware_Benchmark_Certification import Hardware_Benchmark_Certification
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item_Hardware':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Hardware import Billing_Item_Hardware
        return data

    def getBillingItemFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getBillingItemFlag', id=identifier)
        return data

    def getBlockCancelBecauseDisconnectedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getBlockCancelBecauseDisconnectedFlag', id=identifier)
        return data

    def getBusinessContinuanceInsuranceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getBusinessContinuanceInsuranceFlag', id=identifier)
        return data

    def getChildrenHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getChildrenHardware', id=identifier)
        return data

    def getComponents(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getComponents', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getContinuousDataProtectionSoftwareComponent(self, identifier: int) -> 'Software_Component':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getContinuousDataProtectionSoftwareComponent', id=identifier)
        from SoftLayer.sltypes.Software_Component import Software_Component
        return data

    def getCurrentBillableBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getCurrentBillableBandwidthUsage', id=identifier)
        return data

    def getDatacenter(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getDatacenterName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDatacenterName', id=identifier)
        return data

    def getDaysInSparePool(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDaysInSparePool', id=identifier)
        return data

    def getDownlinkHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDownlinkHardware', id=identifier)
        return data

    def getDownlinkNetworkHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDownlinkNetworkHardware', id=identifier)
        return data

    def getDownlinkServers(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDownlinkServers', id=identifier)
        return data

    def getDownlinkVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDownlinkVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getDownstreamHardwareBindings(self, identifier: int) -> list['Network_Component_Uplink_Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDownstreamHardwareBindings', id=identifier)
        from SoftLayer.sltypes.Network_Component_Uplink_Hardware import Network_Component_Uplink_Hardware
        return data

    def getDownstreamNetworkHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDownstreamNetworkHardware', id=identifier)
        return data

    def getDownstreamNetworkHardwareWithIncidents(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDownstreamNetworkHardwareWithIncidents', id=identifier)
        return data

    def getDownstreamServers(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDownstreamServers', id=identifier)
        return data

    def getDownstreamVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDownstreamVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getDriveControllers(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getDriveControllers', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getEvaultNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getEvaultNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getFirewallServiceComponent(self, identifier: int) -> 'Network_Component_Firewall':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getFirewallServiceComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component_Firewall import Network_Component_Firewall
        return data

    def getFixedConfigurationPreset(self, identifier: int) -> 'Product_Package_Preset':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getFixedConfigurationPreset', id=identifier)
        from SoftLayer.sltypes.Product_Package_Preset import Product_Package_Preset
        return data

    def getFrontendNetworkComponents(self, identifier: int) -> list['Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getFrontendNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getFrontendRouters(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getFrontendRouters', id=identifier)
        return data

    def getFutureBillingItem(self, identifier: int) -> 'Billing_Item_Hardware':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getFutureBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Hardware import Billing_Item_Hardware
        return data

    def getGlobalIdentifier(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getGlobalIdentifier', id=identifier)
        return data

    def getHardDrives(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getHardDrives', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getHardwareChassis(self, identifier: int) -> 'Hardware_Chassis':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getHardwareChassis', id=identifier)
        from SoftLayer.sltypes.Hardware_Chassis import Hardware_Chassis
        return data

    def getHardwareFunction(self, identifier: int) -> 'Hardware_Function':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getHardwareFunction', id=identifier)
        from SoftLayer.sltypes.Hardware_Function import Hardware_Function
        return data

    def getHardwareFunctionDescription(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getHardwareFunctionDescription', id=identifier)
        return data

    def getHardwareState(self, identifier: int) -> 'Hardware_State':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getHardwareState', id=identifier)
        from SoftLayer.sltypes.Hardware_State import Hardware_State
        return data

    def getHardwareStatus(self, identifier: int) -> 'Hardware_Status':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getHardwareStatus', id=identifier)
        from SoftLayer.sltypes.Hardware_Status import Hardware_Status
        return data

    def getHasTrustedPlatformModuleBillingItemFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getHasTrustedPlatformModuleBillingItemFlag', id=identifier)
        return data

    def getHostIpsSoftwareComponent(self, identifier: int) -> 'Software_Component':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getHostIpsSoftwareComponent', id=identifier)
        from SoftLayer.sltypes.Software_Component import Software_Component
        return data

    def getHourlyBillingFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getHourlyBillingFlag', id=identifier)
        return data

    def getInboundBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getInboundBandwidthUsage', id=identifier)
        return data

    def getInboundPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getInboundPublicBandwidthUsage', id=identifier)
        return data

    def getIsBillingTermChangeAvailableFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getIsBillingTermChangeAvailableFlag', id=identifier)
        return data

    def getLastTransaction(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getLastTransaction', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getLatestNetworkMonitorIncident(self, identifier: int) -> 'Network_Monitor_Version1_Incident':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getLatestNetworkMonitorIncident', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Incident import Network_Monitor_Version1_Incident
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getLocationPathString(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getLocationPathString', id=identifier)
        return data

    def getLockboxNetworkStorage(self, identifier: int) -> 'Network_Storage':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getLockboxNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getManagedResourceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getManagedResourceFlag', id=identifier)
        return data

    def getMemory(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getMemory', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getMemoryCapacity(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getMemoryCapacity', id=identifier)
        return data

    def getMetricTrackingObject(self, identifier: int) -> 'Metric_Tracking_Object':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getMetricTrackingObject', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object import Metric_Tracking_Object
        return data

    def getModules(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getModules', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getMonitoringRobot(self, identifier: int) -> 'Monitoring_Robot':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getMonitoringRobot', id=identifier)
        from SoftLayer.sltypes.Monitoring_Robot import Monitoring_Robot
        return data

    def getMonitoringServiceComponent(self, identifier: int) -> 'Network_Monitor_Version1_Query_Host_Stratum':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getMonitoringServiceComponent', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_Host_Stratum import Network_Monitor_Version1_Query_Host_Stratum
        return data

    def getMonitoringServiceEligibilityFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getMonitoringServiceEligibilityFlag', id=identifier)
        return data

    def getMotherboard(self, identifier: int) -> 'Hardware_Component':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getMotherboard', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getNetworkCards(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkCards', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getNetworkComponents(self, identifier: int) -> list['Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getNetworkGatewayMember(self, identifier: int) -> 'Network_Gateway_Member':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkGatewayMember', id=identifier)
        from SoftLayer.sltypes.Network_Gateway_Member import Network_Gateway_Member
        return data

    def getNetworkGatewayMemberFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkGatewayMemberFlag', id=identifier)
        return data

    def getNetworkManagementIpAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkManagementIpAddress', id=identifier)
        return data

    def getNetworkMonitorAttachedDownHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkMonitorAttachedDownHardware', id=identifier)
        return data

    def getNetworkMonitorAttachedDownVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkMonitorAttachedDownVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getNetworkMonitorIncidents(self, identifier: int) -> list['Network_Monitor_Version1_Incident']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkMonitorIncidents', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Incident import Network_Monitor_Version1_Incident
        return data

    def getNetworkMonitors(self, identifier: int) -> list['Network_Monitor_Version1_Query_Host']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkMonitors', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_Host import Network_Monitor_Version1_Query_Host
        return data

    def getNetworkStatus(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkStatus', id=identifier)
        return data

    def getNetworkStatusAttribute(self, identifier: int) -> 'Hardware_Attribute':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkStatusAttribute', id=identifier)
        from SoftLayer.sltypes.Hardware_Attribute import Hardware_Attribute
        return data

    def getNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getNetworkVlans(self, identifier: int) -> list['Network_Vlan']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNetworkVlans', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getNextBillingCycleBandwidthAllocation(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNextBillingCycleBandwidthAllocation', id=identifier)
        return data

    def getNotesHistory(self, identifier: int) -> list['Hardware_Note']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNotesHistory', id=identifier)
        from SoftLayer.sltypes.Hardware_Note import Hardware_Note
        return data

    def getNvRamCapacity(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNvRamCapacity', id=identifier)
        return data

    def getNvRamComponentModels(self, identifier: int) -> list['Hardware_Component_Model']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getNvRamComponentModels', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model import Hardware_Component_Model
        return data

    def getOperatingSystem(self, identifier: int) -> 'Software_Component_OperatingSystem':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getOperatingSystem', id=identifier)
        from SoftLayer.sltypes.Software_Component_OperatingSystem import Software_Component_OperatingSystem
        return data

    def getOperatingSystemReferenceCode(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getOperatingSystemReferenceCode', id=identifier)
        return data

    def getOutboundBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getOutboundBandwidthUsage', id=identifier)
        return data

    def getOutboundPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getOutboundPublicBandwidthUsage', id=identifier)
        return data

    def getParentBay(self, identifier: int) -> 'Hardware_Blade':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getParentBay', id=identifier)
        from SoftLayer.sltypes.Hardware_Blade import Hardware_Blade
        return data

    def getParentHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getParentHardware', id=identifier)
        return data

    def getPointOfPresenceLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getPointOfPresenceLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getPowerComponents(self, identifier: int) -> list['Hardware_Power_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getPowerComponents', id=identifier)
        from SoftLayer.sltypes.Hardware_Power_Component import Hardware_Power_Component
        return data

    def getPowerSupply(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getPowerSupply', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getPrimaryBackendIpAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getPrimaryBackendIpAddress', id=identifier)
        return data

    def getPrimaryBackendNetworkComponent(self, identifier: int) -> 'Network_Component':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getPrimaryBackendNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getPrimaryIpAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getPrimaryIpAddress', id=identifier)
        return data

    def getPrimaryNetworkComponent(self, identifier: int) -> 'Network_Component':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getPrimaryNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getPrivateNetworkOnlyFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getPrivateNetworkOnlyFlag', id=identifier)
        return data

    def getProcessorCoreAmount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getProcessorCoreAmount', id=identifier)
        return data

    def getProcessorPhysicalCoreAmount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getProcessorPhysicalCoreAmount', id=identifier)
        return data

    def getProcessors(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getProcessors', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getRack(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getRack', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getRaidControllers(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getRaidControllers', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getRecentEvents(self, identifier: int) -> list['Notification_Occurrence_Event']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getRecentEvents', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Event import Notification_Occurrence_Event
        return data

    def getRemoteManagementAccounts(self, identifier: int) -> list['Hardware_Component_RemoteManagement_User']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getRemoteManagementAccounts', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_RemoteManagement_User import Hardware_Component_RemoteManagement_User
        return data

    def getRemoteManagementComponent(self, identifier: int) -> 'Network_Component':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getRemoteManagementComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getResourceConfigurations(self, identifier: int) -> list['Hardware_Resource_Configuration']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getResourceConfigurations', id=identifier)
        from SoftLayer.sltypes.Hardware_Resource_Configuration import Hardware_Resource_Configuration
        return data

    def getResourceGroupMemberReferences(self, identifier: int) -> list['Resource_Group_Member']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getResourceGroupMemberReferences', id=identifier)
        from SoftLayer.sltypes.Resource_Group_Member import Resource_Group_Member
        return data

    def getResourceGroupRoles(self, identifier: int) -> list['Resource_Group_Role']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getResourceGroupRoles', id=identifier)
        from SoftLayer.sltypes.Resource_Group_Role import Resource_Group_Role
        return data

    def getResourceGroups(self, identifier: int) -> list['Resource_Group']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getResourceGroups', id=identifier)
        from SoftLayer.sltypes.Resource_Group import Resource_Group
        return data

    def getRouters(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getRouters', id=identifier)
        return data

    def getSecurityScanRequests(self, identifier: int) -> list['Network_Security_Scanner_Request']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getSecurityScanRequests', id=identifier)
        from SoftLayer.sltypes.Network_Security_Scanner_Request import Network_Security_Scanner_Request
        return data

    def getServerRoom(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getServerRoom', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getServiceProvider(self, identifier: int) -> 'Service_Provider':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getServiceProvider', id=identifier)
        from SoftLayer.sltypes.Service_Provider import Service_Provider
        return data

    def getSoftwareComponents(self, identifier: int) -> list['Software_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getSoftwareComponents', id=identifier)
        from SoftLayer.sltypes.Software_Component import Software_Component
        return data

    def getSparePoolBillingItem(self, identifier: int) -> 'Billing_Item_Hardware':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getSparePoolBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Hardware import Billing_Item_Hardware
        return data

    def getSshKeys(self, identifier: int) -> list['Security_Ssh_Key']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getSshKeys', id=identifier)
        from SoftLayer.sltypes.Security_Ssh_Key import Security_Ssh_Key
        return data

    def getStorageGroups(self, identifier: int) -> list['Configuration_Storage_Group']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getStorageGroups', id=identifier)
        from SoftLayer.sltypes.Configuration_Storage_Group import Configuration_Storage_Group
        return data

    def getStorageNetworkComponents(self, identifier: int) -> list['Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getStorageNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getTagReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getTagReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data

    def getTopLevelLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getTopLevelLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getUpgradeRequest(self, identifier: int) -> 'Product_Upgrade_Request':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getUpgradeRequest', id=identifier)
        from SoftLayer.sltypes.Product_Upgrade_Request import Product_Upgrade_Request
        return data

    def getUpgradeableActiveComponents(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getUpgradeableActiveComponents', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getUplinkHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getUplinkHardware', id=identifier)
        return data

    def getUplinkNetworkComponents(self, identifier: int) -> list['Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getUplinkNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getUserData(self, identifier: int) -> list['Hardware_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getUserData', id=identifier)
        from SoftLayer.sltypes.Hardware_Attribute import Hardware_Attribute
        return data

    def getVirtualChassis(self, identifier: int) -> 'Hardware_Group':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getVirtualChassis', id=identifier)
        from SoftLayer.sltypes.Hardware_Group import Hardware_Group
        return data

    def getVirtualChassisSiblings(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getVirtualChassisSiblings', id=identifier)
        return data

    def getVirtualHost(self, identifier: int) -> 'Virtual_Host':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getVirtualHost', id=identifier)
        from SoftLayer.sltypes.Virtual_Host import Virtual_Host
        return data

    def getVirtualLicenses(self, identifier: int) -> list['Software_VirtualLicense']:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getVirtualLicenses', id=identifier)
        from SoftLayer.sltypes.Software_VirtualLicense import Software_VirtualLicense
        return data

    def getVirtualRack(self, identifier: int) -> 'Network_Bandwidth_Version1_Allotment':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getVirtualRack', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getVirtualRackId(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getVirtualRackId', id=identifier)
        return data

    def getVirtualRackName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getVirtualRackName', id=identifier)
        return data

    def getVirtualizationPlatform(self, identifier: int) -> 'Software_Component':
        """"""
        data = self.client.call('SoftLayer_Hardware', 'getVirtualizationPlatform', id=identifier)
        from SoftLayer.sltypes.Software_Component import Software_Component
        return data
