# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Bandwidth_Version1_Allotment(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Bandwidth_Version1_Allotment'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Network_Bandwidth_Version1_Allotment',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Bandwidth_Version1_Allotment':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def editObject(
        self,
        templateObject: 'SoftLayer_Network_Bandwidth_Version1_Allotment',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


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
        draw: bool,
        dateSpecified: str,
        dateSpecifiedEnd: str,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getBandwidthImage',
            networkType,
            snapshotRange,
            draw,
            dateSpecified,
            dateSpecifiedEnd,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


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


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Version1_Allotment':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getVdrMemberRecurringFee(
        self,
        identifier: int
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getVdrMemberRecurringFee',
            id=identifier
        )
        
        return data


    def reassignServers(
        self,
        templateObjects: 'SoftLayer_Hardware',
        newAllotmentId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'reassignServers',
            templateObjects,
            newAllotmentId
        )
        
        return data


    def requestVdrCancellation(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'requestVdrCancellation',
            id=identifier
        )
        
        return data


    def requestVdrContentUpdates(
        self,
        hardwareToAdd: 'SoftLayer_Hardware',
        hardwareToRemove: 'SoftLayer_Hardware',
        cloudsToAdd: 'SoftLayer_Virtual_Guest',
        cloudsToRemove: 'SoftLayer_Virtual_Guest',
        optionalAllotmentId: int,
        adcToAdd: 'SoftLayer_Network_Application_Delivery_Controller',
        adcToRemove: 'SoftLayer_Network_Application_Delivery_Controller',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'requestVdrContentUpdates',
            hardwareToAdd,
            hardwareToRemove,
            cloudsToAdd,
            cloudsToRemove,
            optionalAllotmentId,
            adcToAdd,
            adcToRemove,
            id=identifier
        )
        
        return data


    def setVdrContent(
        self,
        hardware: 'SoftLayer_Hardware',
        bareMetalServers: 'SoftLayer_Hardware',
        virtualServerInstance: 'SoftLayer_Virtual_Guest',
        adc: 'SoftLayer_Network_Application_Delivery_Controller',
        optionalAllotmentId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setVdrContent',
            hardware,
            bareMetalServers,
            virtualServerInstance,
            adc,
            optionalAllotmentId,
            id=identifier
        )
        
        return data


    def unassignServers(
        self,
        templateObjects: 'SoftLayer_Hardware'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'unassignServers',
            templateObjects
        )
        
        return data


    def voidPendingServerMove(
        self,
        id: int,
        type: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'voidPendingServerMove',
            id,
            type,
            id=identifier
        )
        
        return data


    def voidPendingVdrCancellation(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'voidPendingVdrCancellation',
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


    def getActiveDetails(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment_Detail]':

        data = self.client.call(
            self.service,
            'getActiveDetails',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment.Detail import Detail
        return Detail(data)


    def getApplicationDeliveryControllers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller]':

        data = self.client.call(
            self.service,
            'getApplicationDeliveryControllers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller import Controller
        return Controller(data)


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


    def getBandwidthAllotmentType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Version1_Allotment_Type':

        data = self.client.call(
            self.service,
            'getBandwidthAllotmentType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment.Type import Type
        return Type(data)


    def getBareMetalInstances(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getBareMetalInstances',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


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


    def getBillingCyclePublicUsageTotal(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getBillingCyclePublicUsageTotal',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


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


    def getDetails(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment_Detail]':

        data = self.client.call(
            self.service,
            'getDetails',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment.Detail import Detail
        return Detail(data)


    def getHardware(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardware',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


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


    def getLocationGroup(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Group':

        data = self.client.call(
            self.service,
            'getLocationGroup',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Group import Group
        return Group(data)


    def getManagedBareMetalInstances(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getManagedBareMetalInstances',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getManagedHardware(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getManagedHardware',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getManagedVirtualGuests(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getManagedVirtualGuests',
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


    def getPrivateNetworkOnlyHardware(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getPrivateNetworkOnlyHardware',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


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


    def getServiceProvider(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Service_Provider':

        data = self.client.call(
            self.service,
            'getServiceProvider',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Service.Provider import Provider
        return Provider(data)


    def getTotalBandwidthAllocated(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedLong':

        data = self.client.call(
            self.service,
            'getTotalBandwidthAllocated',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getVirtualGuests(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuests',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


