# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Hardware(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Hardware'
        self.client = client

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


    def createObject(
        self,
        templateObject: SoftLayer_Hardware,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


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
        return Hardware(data)


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
        return Order(data)


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
        return Price(data)


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


    def getComponentDetailsXML(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getComponentDetailsXML',
            
        )
        
        return data


    def getCreateObjectOptions(
        self,
        
    ) -> 'SoftLayer_Container_Hardware_Configuration':

        data = self.client.call(
            self.service,
            'getCreateObjectOptions',
            
        )
        from SoftLayer.datatypes.Container.Hardware.Configuration import Configuration
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
        return Data(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


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
        return Data(data)


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
        return Data(data)


    def getSensorData(
        self,
        
    ) -> 'list[SoftLayer_Container_RemoteManagement_SensorReading]':

        data = self.client.call(
            self.service,
            'getSensorData',
            
        )
        from SoftLayer.datatypes.Container.RemoteManagement.SensorReading import SensorReading
        return SensorReading(data)


    def getSensorDataWithGraphs(
        self,
        
    ) -> 'SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs':

        data = self.client.call(
            self.service,
            'getSensorDataWithGraphs',
            
        )
        from SoftLayer.datatypes.Container.RemoteManagement.SensorReadingsWithGraphs import SensorReadingsWithGraphs
        return SensorReadingsWithGraphs(data)


    def getServerFanSpeedGraphs(
        self,
        
    ) -> 'list[SoftLayer_Container_RemoteManagement_Graphs_SensorSpeed]':

        data = self.client.call(
            self.service,
            'getServerFanSpeedGraphs',
            
        )
        from SoftLayer.datatypes.Container.RemoteManagement.Graphs.SensorSpeed import SensorSpeed
        return SensorSpeed(data)


    def getServerPowerState(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getServerPowerState',
            
        )
        
        return data


    def getServerTemperatureGraphs(
        self,
        
    ) -> 'list[SoftLayer_Container_RemoteManagement_Graphs_SensorTemperature]':

        data = self.client.call(
            self.service,
            'getServerTemperatureGraphs',
            
        )
        from SoftLayer.datatypes.Container.RemoteManagement.Graphs.SensorTemperature import SensorTemperature
        return SensorTemperature(data)


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
        return History(data)


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
        return Price(data)


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
        return Host(data)


    def isPingable(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isPingable',
            
        )
        
        return data


    def ping(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'ping',
            
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
        return State(data)


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
        return Component(data)


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
        return Component(data)


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
        return Attribute(data)


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
        return Certification(data)


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
        return Hardware(data)


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
        return Hardware(data)


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
        return Component(data)


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
        return Hardware(data)


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
        return Hardware(data)


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
        return Hardware(data)


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
        return Guest(data)


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
        return Hardware(data)


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
        return Hardware(data)


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
        return Hardware(data)


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
        return Hardware(data)


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
        return Guest(data)


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
        return Component(data)


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
        return Preset(data)


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
        return Component(data)


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
        return Hardware(data)


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
        return Component(data)


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
        return Chassis(data)


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
        return Function(data)


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
        return State(data)


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
        return Status(data)


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
        return Storage(data)


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
        return Component(data)


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
        return Component(data)


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
        return Component(data)


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
        return Component(data)


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
        return Component(data)


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
        return Member(data)


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
        return Hardware(data)


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
        return Guest(data)


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
        return Attribute(data)


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
        return Note(data)


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
        return Model(data)


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
        return Blade(data)


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
        return Hardware(data)


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
        return Location(data)


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
        return Component(data)


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
        return Component(data)


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
    ) -> 'SoftLayer_Network_Component':

        data = self.client.call(
            self.service,
            'getPrimaryBackendNetworkComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component import Component
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
    ) -> 'SoftLayer_Network_Component':

        data = self.client.call(
            self.service,
            'getPrimaryNetworkComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component import Component
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
        return Component(data)


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
        return Location(data)


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
        return Component(data)


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
        return User(data)


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
        return Component(data)


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
        return Configuration(data)


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
        return Member(data)


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
        return Role(data)


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
        return Group(data)


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
        return Hardware(data)


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
        return Provider(data)


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
        return Hardware(data)


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
        return Group(data)


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
        return Component(data)


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
        return Location(data)


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
        return Component(data)


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
        return Hardware(data)


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
        return Component(data)


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
        return Attribute(data)


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
        return Group(data)


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
        return Hardware(data)


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
        return Host(data)


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
        return VirtualLicense(data)


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
        return Component(data)


