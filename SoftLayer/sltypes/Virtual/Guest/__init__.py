from SoftLayer.sltypes.Virtual.Guest.SupplementalCreateObjectOptions import Virtual_Guest_SupplementalCreateObjectOptions
from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_Guest(Entity):
    """The virtual guest data type presents the structure in which all virtual guests will be presented. Internally,
the structure supports various virtualization platforms with no change to external interaction.   A guest,
also known as a virtual server, represents an allocation of resources on a virtual host."""
    accountId: int
    createDate: datetime
    dedicatedAccountHostOnlyFlag: bool
    deviceStatusId: int
    domain: str
    fullyQualifiedDomainName: str
    hostname: str
    id_: int
    lastPowerStateId: int
    lastVerifiedDate: datetime
    maxCpu: int
    maxCpuUnits: str
    maxMemory: int
    metricPollDate: datetime
    modifyDate: datetime
    notes: str
    placementGroupId: int
    postInstallScriptUri: str
    provisionDate: datetime
    reclaimDate: datetime
    startCpus: int
    statusId: int
    supplementalCreateObjectOptions: Virtual_Guest_SupplementalCreateObjectOptions
    typeId: int
    uuid: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_Guest'

    def activatePrivatePort(self, identifier: int) -> bool:
        """Activate the private port"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'activatePrivatePort', id=identifier)
        return data

    def activatePublicPort(self, identifier: int) -> bool:
        """Activate the public port"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'activatePublicPort', id=identifier)
        return data

    def allowAccessToNetworkStorage(self, identifier: int, networkStorageTemplateObject: 'Network_Storage') -> bool:
        """Allow access to a SoftLayer_Network_Storage volume from this device."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'allowAccessToNetworkStorage', networkStorageTemplateObject, id=identifier)
        return data

    def allowAccessToNetworkStorageList(self, identifier: int, networkStorageTemplateObjects: 'Network_Storage') -> bool:
        """Allow access to multiple SoftLayer_Network_Storage volumes from this device."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'allowAccessToNetworkStorageList', networkStorageTemplateObjects, id=identifier)
        return data

    def attachDiskImage(self, identifier: int, imageId: int) -> 'Provisioning_Version1_Transaction':
        """Attaches a disk image."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'attachDiskImage', imageId, id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def cancelIsolationForDestructiveAction(self, identifier: int) -> None:
        data = self.client.call('SoftLayer_Virtual_Guest', 'cancelIsolationForDestructiveAction', id=identifier)
        return data

    def captureImage(self, identifier: int, captureTemplate: 'Container_Disk_Image_Capture_Template') -> 'Virtual_Guest_Block_Device_Template_Group':
        """Captures a Flex Image of the hard disk on the virtual machine."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'captureImage', captureTemplate, id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group import Virtual_Guest_Block_Device_Template_Group
        return data

    def checkHostDiskAvailability(self, identifier: int, diskCapacity: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest', 'checkHostDiskAvailability', diskCapacity, id=identifier)
        return data

    def configureMetadataDisk(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """Configures the guest's metadata disk."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'configureMetadataDisk', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def createArchiveTemplate(self, identifier: int, groupName: str, blockDevices: 'Virtual_Guest_Block_Device', note: str) -> 'Virtual_Guest_Block_Device_Template_Group':
        """[[SoftLayer_Virtual_Guest_Block_Devices|Block Devices]] can be grouped together in and backed up in an
archive for later use. This method generates a transaction to perform an archive of the provided block
devices."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'createArchiveTemplate', groupName, blockDevices, note, id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group import Virtual_Guest_Block_Device_Template_Group
        return data

    def createArchiveTransaction(self, identifier: int, groupName: str, blockDevices: 'Virtual_Guest_Block_Device', note: str) -> 'Provisioning_Version1_Transaction':
        """[[SoftLayer_Virtual_Guest_Block_Device]] can be grouped together in and backed up in an archive for later
use. This method generates a transaction to perform an archive of the provided block devices."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'createArchiveTransaction', groupName, blockDevices, note, id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def createObject(self, templateObject: 'Virtual_Guest') -> 'Virtual_Guest':
        """Create a new computing instance"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'createObject', templateObject)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def createObjects(self, templateObjects: 'Virtual_Guest') -> list['Virtual_Guest']:
        """Create new computing instances"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'createObjects', templateObjects)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def createPostSoftwareInstallTransaction(self, identifier: int, data: str, returnBoolean: bool) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest', 'createPostSoftwareInstallTransaction', data, returnBoolean, id=identifier)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a computing instance"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'deleteObject', id=identifier)
        return data

    def deleteTag(self, identifier: int, tagName: str) -> bool:
        """Delete a tag"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'deleteTag', tagName, id=identifier)
        return data

    def deleteTransientWebhook(self, identifier: int) -> None:
        data = self.client.call('SoftLayer_Virtual_Guest', 'deleteTransientWebhook', id=identifier)
        return data

    def detachDiskImage(self, identifier: int, imageId: int) -> 'Provisioning_Version1_Transaction':
        """Detaches a disk image."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'detachDiskImage', imageId, id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def editObject(self, identifier: int, templateObject: 'Virtual_Guest') -> bool:
        """Edit a computing instance's properties"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'editObject', templateObject, id=identifier)
        return data

    def executeIderaBareMetalRestore(self, identifier: int) -> bool:
        """Reboot a guest into the Idera Bare Metal Restore image."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'executeIderaBareMetalRestore', id=identifier)
        return data

    def executeR1SoftBareMetalRestore(self, identifier: int) -> bool:
        """Reboot a guest into the R1Soft Bare Metal Restore image."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'executeR1SoftBareMetalRestore', id=identifier)
        return data

    def executeRemoteScript(self, identifier: int, uri: str) -> None:
        """Download and run remote script from uri on the virtual guest. Requires https for script to be executed after
download."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'executeRemoteScript', uri, id=identifier)
        return data

    def executeRescueLayer(self, identifier: int) -> bool:
        """Reboot a Linux guest into the Xen rescue image."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'executeRescueLayer', id=identifier)
        return data

    def findByHostname(self, hostname: str) -> list['Virtual_Guest']:
        data = self.client.call('SoftLayer_Virtual_Guest', 'findByHostname', hostname)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def findByIpAddress(self, ipAddress: str) -> 'Virtual_Guest':
        """Find CCI by its primary public or private IP (ipv4) address."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'findByIpAddress', ipAddress)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def generateOrderTemplate(self, templateObject: 'Virtual_Guest') -> 'Container_Product_Order':
        """Obtain an order container for a given template object"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'generateOrderTemplate', templateObject)
        from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order
        return data

    def getAdditionalRequiredPricesForOsReload(self, identifier: int, config: 'Container_Hardware_Server_Configuration') -> list['Product_Item_Price']:
        """Return a collection of SoftLayer_Item_Price objects for an OS reload"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAdditionalRequiredPricesForOsReload', config, id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getAttachedNetworkStorages(self, identifier: int, nasType: str) -> list['Network_Storage']:
        """Return a list of SoftLayer_Network_Storage volumes authorized to this device."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAttachedNetworkStorages', nasType, id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAvailableBlockDevicePositions(self, identifier: int) -> list[str]:
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAvailableBlockDevicePositions', id=identifier)
        return data

    def getAvailableNetworkStorages(self, identifier: int, nasType: str) -> list['Network_Storage']:
        """Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAvailableNetworkStorages', nasType, id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getBandwidthDataByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime, networkType: str) -> list['Metric_Tracking_Object_Data']:
        """Retrieve the amount of network traffic that occurred for the specified time frame for a computing instance."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBandwidthDataByDate', startDateTime, endDateTime, networkType, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getBandwidthForDateRange(self, identifier: int, startDate: datetime, endDate: datetime) -> list['Metric_Tracking_Object_Data']:
        """Retrieve bandwidth data from a tracking object."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBandwidthForDateRange', startDate, endDate, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getBandwidthImage(self, identifier: int, networkType: str, snapshotRange: str, dateSpecified: datetime, dateSpecifiedEnd: datetime) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame
for a computing instance."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBandwidthImage', networkType, snapshotRange, dateSpecified, dateSpecifiedEnd, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getBandwidthImageByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime, networkType: str) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame
for a computing instance."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBandwidthImageByDate', startDateTime, endDateTime, networkType, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getBandwidthTotal(self, identifier: int, startDateTime: datetime, endDateTime: datetime, direction: str, side: str) -> int:
        """Retrieve total amount of network traffic that was in use during the time specified by the input parameters
for a computing instance."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBandwidthTotal', startDateTime, endDateTime, direction, side, id=identifier)
        return data

    def getBootMode(self, identifier: int) -> str:
        """Retrieves the boot mode of the VSI."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBootMode', id=identifier)
        return data

    def getBootOrder(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBootOrder', id=identifier)
        return data

    def getConsoleAccessLog(self, identifier: int) -> list['Network_Logging_Syslog']:
        """get console access logs"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getConsoleAccessLog', id=identifier)
        from SoftLayer.sltypes.Network_Logging_Syslog import Network_Logging_Syslog
        return data

    def getCoreRestrictedOperatingSystemPrice(self, identifier: int) -> 'Product_Item_Price':
        """Return the associated core-restricted operating system item price for the virtual server."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getCoreRestrictedOperatingSystemPrice', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getCpuMetricDataByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime, cpuIndexes: int) -> list['Metric_Tracking_Object_Data']:
        """Retrieve records containing the percentage of the amount of time that a cpu was in use for the specified time
frame for a computing instance."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getCpuMetricDataByDate', startDateTime, endDateTime, cpuIndexes, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getCpuMetricImage(self, identifier: int, snapshotRange: str, dateSpecified: datetime) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve a visual representation of the percentage of the amount of time that a cpu was in use for the
specified time frame for a computing instance."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getCpuMetricImage', snapshotRange, dateSpecified, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getCpuMetricImageByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime, cpuIndexes: int) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve a visual representation of the percentage of the amount of time that a cpu was in use for the
specified time frame for a computing instance."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getCpuMetricImageByDate', startDateTime, endDateTime, cpuIndexes, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getCreateObjectOptions(self) -> 'Container_Virtual_Guest_Configuration':
        """Determine options available when creating a computing instance"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getCreateObjectOptions')
        from SoftLayer.sltypes.Container_Virtual_Guest_Configuration import Container_Virtual_Guest_Configuration
        return data

    def getCurrentBillingDetail(self, identifier: int) -> list['Billing_Item']:
        """<< EOT"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getCurrentBillingDetail', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getCurrentBillingTotal(self, identifier: int) -> float:
        """Get the billing total for this instance's usage up to this point. This total includes all bandwidth charges."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getCurrentBillingTotal', id=identifier)
        return data

    def getCustomBandwidthDataByDate(self, identifier: int, graphData: 'Container_Graph') -> 'Container_Graph':
        """Retrieve bandwidth graph by date."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getCustomBandwidthDataByDate', graphData, id=identifier)
        from SoftLayer.sltypes.Container_Graph import Container_Graph
        return data

    def getCustomMetricDataByDate(self, identifier: int, graphData: 'Container_Graph') -> 'Container_Graph':
        """Retrieve bandwidth graph by date."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getCustomMetricDataByDate', graphData, id=identifier)
        from SoftLayer.sltypes.Container_Graph import Container_Graph
        return data

    def getDriveRetentionItemPrice(self, identifier: int) -> 'Product_Item_Price':
        """Return a drive retention SoftLayer_Item_Price object for a guest."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getDriveRetentionItemPrice', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getFirewallProtectableSubnets(self, identifier: int) -> list['Network_Subnet']:
        """Get the subnets associated with this CloudLayer computing instance that are protectable by a network
component firewall."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getFirewallProtectableSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getFirstAvailableBlockDevicePosition(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Virtual_Guest', 'getFirstAvailableBlockDevicePosition', id=identifier)
        return data

    def getIsoBootImage(self, identifier: int) -> 'Virtual_Disk_Image':
        data = self.client.call('SoftLayer_Virtual_Guest', 'getIsoBootImage', id=identifier)
        from SoftLayer.sltypes.Virtual_Disk_Image import Virtual_Disk_Image
        return data

    def getItemPricesFromSoftwareDescriptions(self, identifier: int, softwareDescriptions: 'Software_Description', includeTranslationsFlag: bool, returnAllPricesFlag: bool) -> list['Product_Item']:
        """Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getItemPricesFromSoftwareDescriptions', softwareDescriptions, includeTranslationsFlag, returnAllPricesFlag, id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getMemoryMetricDataByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime) -> list['Metric_Tracking_Object_Data']:
        """Retrieve records containing the amount memory that was used for the specified time frame for a computing
instance."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getMemoryMetricDataByDate', startDateTime, endDateTime, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getMemoryMetricImage(self, identifier: int, snapshotRange: str, dateSpecified: datetime) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve a visual representation of the amount of memory used for the specified time frame for a computing
instance."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getMemoryMetricImage', snapshotRange, dateSpecified, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getMemoryMetricImageByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve a visual representation of the amount of memory used for the specified time frame for a computing
instance."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getMemoryMetricImageByDate', startDateTime, endDateTime, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getNetworkComponentFirewallProtectableIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """Get the IP addresses associated with this CloudLayer computing instance that are protectable by a network
component firewall."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getNetworkComponentFirewallProtectableIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getObject(self, identifier: int) -> 'Virtual_Guest':
        """Retrieve a SoftLayer_Virtual_Guest record."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getObject', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getOrderTemplate(self, identifier: int, billingType: str, orderPrices: 'Product_Item_Price') -> 'Container_Product_Order':
        """Obtain an order container that is ready to be sent to the
[[SoftLayer_Product_Order#placeOrder|SoftLayer_Product_Order::placeOrder]] method."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getOrderTemplate', billingType, orderPrices, id=identifier)
        from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order
        return data

    def getPendingMaintenanceActions(self, identifier: int) -> list['Container_Virtual_Guest_PendingMaintenanceAction']:
        """Returns a list of all the pending maintenance actions affecting this guest."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getPendingMaintenanceActions', id=identifier)
        from SoftLayer.sltypes.Container_Virtual_Guest_PendingMaintenanceAction import Container_Virtual_Guest_PendingMaintenanceAction
        return data

    def getProvisionDate(self, identifier: int) -> datetime:
        data = self.client.call('SoftLayer_Virtual_Guest', 'getProvisionDate', id=identifier)
        return data

    def getRecentMetricData(self, identifier: int, time: int) -> list['Metric_Tracking_Object']:
        """Recent metric data for a guest"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getRecentMetricData', time, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object import Metric_Tracking_Object
        return data

    def getReverseDomainRecords(self, identifier: int) -> list['Dns_Domain']:
        """Retrieve the reverse domain records associated with a server."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getReverseDomainRecords', id=identifier)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def getUpgradeItemPrices(self, identifier: int, includeDowngradeItemPrices: bool) -> list['Product_Item_Price']:
        """Retrieve a computing instance's upgradeable items."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getUpgradeItemPrices', includeDowngradeItemPrices, id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getValidBlockDeviceTemplateGroups(self, identifier: int, visibility: str) -> list['Virtual_Guest_Block_Device_Template_Group']:
        """Return a list of valid block device template groups based on this host"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getValidBlockDeviceTemplateGroups', visibility, id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group import Virtual_Guest_Block_Device_Template_Group
        return data

    def isBackendPingable(self, identifier: int) -> bool:
        """Verifies if a guest's backend ip address is pingable."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'isBackendPingable', id=identifier)
        return data

    def isCloudInit(self, identifier: int) -> bool:
        """Determines if the virtual guest was provisioned from a cloud-init enabled image."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'isCloudInit', id=identifier)
        return data

    def isPingable(self, identifier: int) -> bool:
        """Verifies if guest is pingable."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'isPingable', id=identifier)
        return data

    def isolateInstanceForDestructiveAction(self, identifier: int) -> None:
        data = self.client.call('SoftLayer_Virtual_Guest', 'isolateInstanceForDestructiveAction', id=identifier)
        return data

    def migrate(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """Creates a transaction to migrate a virtual guest to a new host. NOTE: Will only migrate if
SoftLayer_Virtual_Guest property pendingMigrationFlag = true"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'migrate', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def migrateDedicatedHost(self, identifier: int, destinationHostId: int) -> None:
        """Migrate a dedicated instance from one dedicated host to another dedicated host"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'migrateDedicatedHost', destinationHostId, id=identifier)
        return data

    def mountIsoImage(self, identifier: int, diskImageId: int) -> 'Provisioning_Version1_Transaction':
        data = self.client.call('SoftLayer_Virtual_Guest', 'mountIsoImage', diskImageId, id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def pause(self, identifier: int) -> bool:
        """Pause a guest."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'pause', id=identifier)
        return data

    def powerCycle(self, identifier: int) -> bool:
        """Power cycle a guest."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'powerCycle', id=identifier)
        return data

    def powerOff(self, identifier: int) -> bool:
        """Power off a guest."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'powerOff', id=identifier)
        return data

    def powerOffSoft(self, identifier: int) -> bool:
        """Cleanly shut down a guest and disable power"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'powerOffSoft', id=identifier)
        return data

    def powerOn(self, identifier: int) -> bool:
        """Power on a guest."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'powerOn', id=identifier)
        return data

    def rebootDefault(self, identifier: int) -> bool:
        """Power cycle a guest."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'rebootDefault', id=identifier)
        return data

    def rebootHard(self, identifier: int) -> bool:
        """Power cycle a guest."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'rebootHard', id=identifier)
        return data

    def rebootSoft(self, identifier: int) -> bool:
        """Attempt to complete a soft reboot of a guest by shutting down the operating system."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'rebootSoft', id=identifier)
        return data

    def reloadCurrentOperatingSystemConfiguration(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """Perform an OS reload"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'reloadCurrentOperatingSystemConfiguration', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def reloadOperatingSystem(self, identifier: int, token: str, config: 'Container_Hardware_Server_Configuration') -> str:
        """Reloads operating system configuration."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'reloadOperatingSystem', token, config, id=identifier)
        return data

    def removeAccessToNetworkStorage(self, identifier: int, networkStorageTemplateObject: 'Network_Storage') -> bool:
        """Remove access to a SoftLayer_Network_Storage volume from this device."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'removeAccessToNetworkStorage', networkStorageTemplateObject, id=identifier)
        return data

    def removeAccessToNetworkStorageList(self, identifier: int, networkStorageTemplateObjects: 'Network_Storage') -> bool:
        """Remove access to multiple SoftLayer_Network_Storage volumes from this device."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'removeAccessToNetworkStorageList', networkStorageTemplateObjects, id=identifier)
        return data

    def removeTags(self, identifier: int, tags: str) -> bool:
        """Remove a tag reference"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'removeTags', tags, id=identifier)
        return data

    def resume(self, identifier: int) -> bool:
        """Resume a guest."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'resume', id=identifier)
        return data

    def sendTestReclaimScheduledAlert(self, identifier: int) -> None:
        data = self.client.call('SoftLayer_Virtual_Guest', 'sendTestReclaimScheduledAlert', id=identifier)
        return data

    def setPrivateNetworkInterfaceSpeed(self, identifier: int, newSpeed: int) -> bool:
        """Updates the private network interface (eth0) speed."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'setPrivateNetworkInterfaceSpeed', newSpeed, id=identifier)
        return data

    def setPublicNetworkInterfaceSpeed(self, identifier: int, newSpeed: int) -> bool:
        """Updates the public network interface (eth1) speed."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'setPublicNetworkInterfaceSpeed', newSpeed, id=identifier)
        return data

    def setTags(self, identifier: int, tags: str) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest', 'setTags', tags, id=identifier)
        return data

    def setTransientWebhook(self, identifier: int, uri: str, secret: str) -> None:
        data = self.client.call('SoftLayer_Virtual_Guest', 'setTransientWebhook', uri, secret, id=identifier)
        return data

    def setUserMetadata(self, identifier: int, metadata: str) -> bool:
        """Configures the guest's metadata disk."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'setUserMetadata', metadata, id=identifier)
        return data

    def shutdownPrivatePort(self, identifier: int) -> bool:
        """Shuts down the private port"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'shutdownPrivatePort', id=identifier)
        return data

    def shutdownPublicPort(self, identifier: int) -> bool:
        """Shuts down the public port"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'shutdownPublicPort', id=identifier)
        return data

    def unmountIsoImage(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        data = self.client.call('SoftLayer_Virtual_Guest', 'unmountIsoImage', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def validateImageTemplate(self, identifier: int, imageTemplateId: int) -> bool:
        """Validates an image template for OS Reload"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'validateImageTemplate', imageTemplateId, id=identifier)
        return data

    def verifyReloadOperatingSystem(self, identifier: int, config: 'Container_Hardware_Server_Configuration') -> bool:
        """Verify that a virtual server can go through the operating system reload process."""
        data = self.client.call('SoftLayer_Virtual_Guest', 'verifyReloadOperatingSystem', config, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAccountOwnedPoolFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAccountOwnedPoolFlag', id=identifier)
        return data

    def getActiveNetworkMonitorIncident(self, identifier: int) -> list['Network_Monitor_Version1_Incident']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getActiveNetworkMonitorIncident', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Incident import Network_Monitor_Version1_Incident
        return data

    def getActiveTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getActiveTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getActiveTransaction(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getActiveTransaction', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getActiveTransactions(self, identifier: int) -> list['Provisioning_Version1_Transaction']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getActiveTransactions', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getAllowedHost(self, identifier: int) -> 'Network_Storage_Allowed_Host':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAllowedHost', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
        return data

    def getAllowedNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAllowedNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAllowedNetworkStorageReplicas(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAllowedNetworkStorageReplicas', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAntivirusSpywareSoftwareComponent(self, identifier: int) -> 'Software_Component':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAntivirusSpywareSoftwareComponent', id=identifier)
        from SoftLayer.sltypes.Software_Component import Software_Component
        return data

    def getApplicationDeliveryController(self, identifier: int) -> 'Network_Application_Delivery_Controller':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getApplicationDeliveryController', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller import Network_Application_Delivery_Controller
        return data

    def getAttributes(self, identifier: int) -> list['Virtual_Guest_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Attribute import Virtual_Guest_Attribute
        return data

    def getAvailableMonitoring(self, identifier: int) -> list['Network_Monitor_Version1_Query_Host_Stratum']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAvailableMonitoring', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_Host_Stratum import Network_Monitor_Version1_Query_Host_Stratum
        return data

    def getAverageDailyPrivateBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAverageDailyPrivateBandwidthUsage', id=identifier)
        return data

    def getAverageDailyPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getAverageDailyPublicBandwidthUsage', id=identifier)
        return data

    def getBackendNetworkComponents(self, identifier: int) -> list['Virtual_Guest_Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBackendNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component import Virtual_Guest_Network_Component
        return data

    def getBackendRouters(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBackendRouters', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getBandwidthAllocation(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBandwidthAllocation', id=identifier)
        return data

    def getBandwidthAllotmentDetail(self, identifier: int) -> 'Network_Bandwidth_Version1_Allotment_Detail':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBandwidthAllotmentDetail', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment_Detail import Network_Bandwidth_Version1_Allotment_Detail
        return data

    def getBillingCycleBandwidthUsage(self, identifier: int) -> list['Network_Bandwidth_Usage']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBillingCycleBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBillingCyclePrivateBandwidthUsage(self, identifier: int) -> 'Network_Bandwidth_Usage':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBillingCyclePrivateBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBillingCyclePublicBandwidthUsage(self, identifier: int) -> 'Network_Bandwidth_Usage':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBillingCyclePublicBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item_Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Virtual_Guest import Billing_Item_Virtual_Guest
        return data

    def getBlockCancelBecauseDisconnectedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBlockCancelBecauseDisconnectedFlag', id=identifier)
        return data

    def getBlockDeviceTemplateGroup(self, identifier: int) -> 'Virtual_Guest_Block_Device_Template_Group':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBlockDeviceTemplateGroup', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group import Virtual_Guest_Block_Device_Template_Group
        return data

    def getBlockDevices(self, identifier: int) -> list['Virtual_Guest_Block_Device']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBlockDevices', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device import Virtual_Guest_Block_Device
        return data

    def getBrowserConsoleAccessLogs(self, identifier: int) -> list['Virtual_BrowserConsoleAccessLog']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getBrowserConsoleAccessLogs', id=identifier)
        from SoftLayer.sltypes.Virtual_BrowserConsoleAccessLog import Virtual_BrowserConsoleAccessLog
        return data

    def getConsoleData(self, identifier: int) -> 'Container_Virtual_ConsoleData':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getConsoleData', id=identifier)
        from SoftLayer.sltypes.Container_Virtual_ConsoleData import Container_Virtual_ConsoleData
        return data

    def getConsoleIpAddressFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getConsoleIpAddressFlag', id=identifier)
        return data

    def getConsoleIpAddressRecord(self, identifier: int) -> 'Virtual_Guest_Network_Component_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getConsoleIpAddressRecord', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component_IpAddress import Virtual_Guest_Network_Component_IpAddress
        return data

    def getContinuousDataProtectionSoftwareComponent(self, identifier: int) -> 'Software_Component':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getContinuousDataProtectionSoftwareComponent', id=identifier)
        from SoftLayer.sltypes.Software_Component import Software_Component
        return data

    def getControlPanel(self, identifier: int) -> 'Software_Component':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getControlPanel', id=identifier)
        from SoftLayer.sltypes.Software_Component import Software_Component
        return data

    def getCurrentBandwidthSummary(self, identifier: int) -> 'Metric_Tracking_Object_Bandwidth_Summary':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getCurrentBandwidthSummary', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Bandwidth_Summary import Metric_Tracking_Object_Bandwidth_Summary
        return data

    def getDatacenter(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getDedicatedHost(self, identifier: int) -> 'Virtual_DedicatedHost':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getDedicatedHost', id=identifier)
        from SoftLayer.sltypes.Virtual_DedicatedHost import Virtual_DedicatedHost
        return data

    def getDeviceStatus(self, identifier: int) -> 'Device_Status':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getDeviceStatus', id=identifier)
        from SoftLayer.sltypes.Device_Status import Device_Status
        return data

    def getEvaultNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getEvaultNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getFirewallServiceComponent(self, identifier: int) -> 'Network_Component_Firewall':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getFirewallServiceComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component_Firewall import Network_Component_Firewall
        return data

    def getFrontendNetworkComponents(self, identifier: int) -> list['Virtual_Guest_Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getFrontendNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component import Virtual_Guest_Network_Component
        return data

    def getFrontendRouters(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getFrontendRouters', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getGlobalIdentifier(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getGlobalIdentifier', id=identifier)
        return data

    def getGpuCount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getGpuCount', id=identifier)
        return data

    def getGpuType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getGpuType', id=identifier)
        return data

    def getGuestBootParameter(self, identifier: int) -> 'Virtual_Guest_Boot_Parameter':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getGuestBootParameter', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Boot_Parameter import Virtual_Guest_Boot_Parameter
        return data

    def getHardwareFunctionDescription(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getHardwareFunctionDescription', id=identifier)
        return data

    def getHost(self, identifier: int) -> 'Virtual_Host':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getHost', id=identifier)
        from SoftLayer.sltypes.Virtual_Host import Virtual_Host
        return data

    def getHostIpsSoftwareComponent(self, identifier: int) -> 'Software_Component':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getHostIpsSoftwareComponent', id=identifier)
        from SoftLayer.sltypes.Software_Component import Software_Component
        return data

    def getHourlyBillingFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getHourlyBillingFlag', id=identifier)
        return data

    def getInboundPrivateBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getInboundPrivateBandwidthUsage', id=identifier)
        return data

    def getInboundPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getInboundPublicBandwidthUsage', id=identifier)
        return data

    def getInternalTagReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getInternalTagReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data

    def getLastKnownPowerState(self, identifier: int) -> 'Virtual_Guest_Power_State':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getLastKnownPowerState', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Power_State import Virtual_Guest_Power_State
        return data

    def getLastOperatingSystemReload(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getLastOperatingSystemReload', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getLastTransaction(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getLastTransaction', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getLatestNetworkMonitorIncident(self, identifier: int) -> 'Network_Monitor_Version1_Incident':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getLatestNetworkMonitorIncident', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Incident import Network_Monitor_Version1_Incident
        return data

    def getLocalDiskFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getLocalDiskFlag', id=identifier)
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getManagedResourceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getManagedResourceFlag', id=identifier)
        return data

    def getMetricTrackingObject(self, identifier: int) -> 'Metric_Tracking_Object':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getMetricTrackingObject', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object import Metric_Tracking_Object
        return data

    def getMetricTrackingObjectId(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getMetricTrackingObjectId', id=identifier)
        return data

    def getMonitoringRobot(self, identifier: int) -> 'Monitoring_Robot':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getMonitoringRobot', id=identifier)
        from SoftLayer.sltypes.Monitoring_Robot import Monitoring_Robot
        return data

    def getMonitoringServiceComponent(self, identifier: int) -> 'Network_Monitor_Version1_Query_Host_Stratum':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getMonitoringServiceComponent', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_Host_Stratum import Network_Monitor_Version1_Query_Host_Stratum
        return data

    def getMonitoringServiceEligibilityFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getMonitoringServiceEligibilityFlag', id=identifier)
        return data

    def getMonitoringUserNotification(self, identifier: int) -> list['User_Customer_Notification_Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getMonitoringUserNotification', id=identifier)
        from SoftLayer.sltypes.User_Customer_Notification_Virtual_Guest import User_Customer_Notification_Virtual_Guest
        return data

    def getNetworkComponents(self, identifier: int) -> list['Virtual_Guest_Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component import Virtual_Guest_Network_Component
        return data

    def getNetworkMonitorIncidents(self, identifier: int) -> list['Network_Monitor_Version1_Incident']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getNetworkMonitorIncidents', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Incident import Network_Monitor_Version1_Incident
        return data

    def getNetworkMonitors(self, identifier: int) -> list['Network_Monitor_Version1_Query_Host']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getNetworkMonitors', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_Host import Network_Monitor_Version1_Query_Host
        return data

    def getNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getNetworkVlans(self, identifier: int) -> list['Network_Vlan']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getNetworkVlans', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getOpenCancellationTicket(self, identifier: int) -> 'Ticket':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getOpenCancellationTicket', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOperatingSystem(self, identifier: int) -> 'Software_Component_OperatingSystem':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getOperatingSystem', id=identifier)
        from SoftLayer.sltypes.Software_Component_OperatingSystem import Software_Component_OperatingSystem
        return data

    def getOperatingSystemReferenceCode(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getOperatingSystemReferenceCode', id=identifier)
        return data

    def getOrderedPackageId(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getOrderedPackageId', id=identifier)
        return data

    def getOutboundPrivateBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getOutboundPrivateBandwidthUsage', id=identifier)
        return data

    def getOutboundPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getOutboundPublicBandwidthUsage', id=identifier)
        return data

    def getOverBandwidthAllocationFlag(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getOverBandwidthAllocationFlag', id=identifier)
        return data

    def getPendingMigrationFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getPendingMigrationFlag', id=identifier)
        return data

    def getPlacementGroup(self, identifier: int) -> 'Virtual_PlacementGroup':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getPlacementGroup', id=identifier)
        from SoftLayer.sltypes.Virtual_PlacementGroup import Virtual_PlacementGroup
        return data

    def getPowerState(self, identifier: int) -> 'Virtual_Guest_Power_State':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getPowerState', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Power_State import Virtual_Guest_Power_State
        return data

    def getPrimaryBackendIpAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getPrimaryBackendIpAddress', id=identifier)
        return data

    def getPrimaryBackendNetworkComponent(self, identifier: int) -> 'Virtual_Guest_Network_Component':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getPrimaryBackendNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component import Virtual_Guest_Network_Component
        return data

    def getPrimaryIpAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getPrimaryIpAddress', id=identifier)
        return data

    def getPrimaryNetworkComponent(self, identifier: int) -> 'Virtual_Guest_Network_Component':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getPrimaryNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component import Virtual_Guest_Network_Component
        return data

    def getPrivateNetworkOnlyFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getPrivateNetworkOnlyFlag', id=identifier)
        return data

    def getProjectedOverBandwidthAllocationFlag(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getProjectedOverBandwidthAllocationFlag', id=identifier)
        return data

    def getProjectedPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getProjectedPublicBandwidthUsage', id=identifier)
        return data

    def getRecentEvents(self, identifier: int) -> list['Notification_Occurrence_Event']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getRecentEvents', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Event import Notification_Occurrence_Event
        return data

    def getRegionalGroup(self, identifier: int) -> 'Location_Group_Regional':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getRegionalGroup', id=identifier)
        from SoftLayer.sltypes.Location_Group_Regional import Location_Group_Regional
        return data

    def getRegionalInternetRegistry(self, identifier: int) -> 'Network_Regional_Internet_Registry':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getRegionalInternetRegistry', id=identifier)
        from SoftLayer.sltypes.Network_Regional_Internet_Registry import Network_Regional_Internet_Registry
        return data

    def getReservedCapacityGroup(self, identifier: int) -> 'Virtual_ReservedCapacityGroup':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getReservedCapacityGroup', id=identifier)
        from SoftLayer.sltypes.Virtual_ReservedCapacityGroup import Virtual_ReservedCapacityGroup
        return data

    def getReservedCapacityGroupFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getReservedCapacityGroupFlag', id=identifier)
        return data

    def getReservedCapacityGroupInstance(self, identifier: int) -> 'Virtual_ReservedCapacityGroup_Instance':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getReservedCapacityGroupInstance', id=identifier)
        from SoftLayer.sltypes.Virtual_ReservedCapacityGroup_Instance import Virtual_ReservedCapacityGroup_Instance
        return data

    def getSecurityScanRequests(self, identifier: int) -> list['Network_Security_Scanner_Request']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getSecurityScanRequests', id=identifier)
        from SoftLayer.sltypes.Network_Security_Scanner_Request import Network_Security_Scanner_Request
        return data

    def getServerRoom(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getServerRoom', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getSoftwareComponents(self, identifier: int) -> list['Software_Component']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getSoftwareComponents', id=identifier)
        from SoftLayer.sltypes.Software_Component import Software_Component
        return data

    def getSshKeys(self, identifier: int) -> list['Security_Ssh_Key']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getSshKeys', id=identifier)
        from SoftLayer.sltypes.Security_Ssh_Key import Security_Ssh_Key
        return data

    def getStatus(self, identifier: int) -> 'Virtual_Guest_Status':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Status import Virtual_Guest_Status
        return data

    def getTagReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getTagReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data

    def getTransientGuestFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getTransientGuestFlag', id=identifier)
        return data

    def getTransientWebhookURI(self, identifier: int) -> 'Virtual_Guest_Attribute':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getTransientWebhookURI', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Attribute import Virtual_Guest_Attribute
        return data

    def getType(self, identifier: int) -> 'Virtual_Guest_Type':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getType', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Type import Virtual_Guest_Type
        return data

    def getUpgradeRequest(self, identifier: int) -> 'Product_Upgrade_Request':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getUpgradeRequest', id=identifier)
        from SoftLayer.sltypes.Product_Upgrade_Request import Product_Upgrade_Request
        return data

    def getUserData(self, identifier: int) -> list['Virtual_Guest_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getUserData', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Attribute import Virtual_Guest_Attribute
        return data

    def getUsers(self, identifier: int) -> list['User_Customer']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getUsers', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getVirtualRack(self, identifier: int) -> 'Network_Bandwidth_Version1_Allotment':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getVirtualRack', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getVirtualRackId(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getVirtualRackId', id=identifier)
        return data

    def getVirtualRackName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest', 'getVirtualRackName', id=identifier)
        return data
