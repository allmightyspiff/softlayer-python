# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Bandwidth_Version1_Allotment(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Bandwidth_Version1_Allotment'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Network_Bandwidth_Version1_Allotment,
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
        templateObject: SoftLayer_Network_Bandwidth_Version1_Allotment
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


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
        return GraphOutputs(data)


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


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Version1_Allotment':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getVdrMemberRecurringFee(
        self,
        
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getVdrMemberRecurringFee',
            
        )
        
        return data


    def reassignServers(
        self,
        templateObjects: SoftLayer_Hardware,
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
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'requestVdrCancellation',
            
        )
        
        return data


    def requestVdrContentUpdates(
        self,
        hardwareToAdd: SoftLayer_Hardware,
        hardwareToRemove: SoftLayer_Hardware,
        cloudsToAdd: SoftLayer_Virtual_Guest,
        cloudsToRemove: SoftLayer_Virtual_Guest,
        optionalAllotmentId: int,
        adcToAdd: SoftLayer_Network_Application_Delivery_Controller,
        adcToRemove: SoftLayer_Network_Application_Delivery_Controller
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
            adcToRemove
        )
        
        return data


    def setVdrContent(
        self,
        hardware: SoftLayer_Hardware,
        bareMetalServers: SoftLayer_Hardware,
        virtualServerInstance: SoftLayer_Virtual_Guest,
        adc: SoftLayer_Network_Application_Delivery_Controller,
        optionalAllotmentId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setVdrContent',
            hardware,
            bareMetalServers,
            virtualServerInstance,
            adc,
            optionalAllotmentId
        )
        
        return data


    def unassignServers(
        self,
        templateObjects: SoftLayer_Hardware
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
        type: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'voidPendingServerMove',
            id,
            type
        )
        
        return data


    def voidPendingVdrCancellation(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'voidPendingVdrCancellation',
            
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


    def getActiveDetails(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment_Detail]':

        data = self.client.call(
            self.service,
            'getActiveDetails',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment.Detail import Detail
        return Detail(data)


    def getApplicationDeliveryControllers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller]':

        data = self.client.call(
            self.service,
            'getApplicationDeliveryControllers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller import Controller
        return Controller(data)


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


    def getBandwidthAllotmentType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Version1_Allotment_Type':

        data = self.client.call(
            self.service,
            'getBandwidthAllotmentType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment.Type import Type
        return Type(data)


    def getBareMetalInstances(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getBareMetalInstances',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


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


    def getBillingCyclePublicUsageTotal(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getBillingCyclePublicUsageTotal',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


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


    def getDetails(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment_Detail]':

        data = self.client.call(
            self.service,
            'getDetails',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment.Detail import Detail
        return Detail(data)


    def getHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


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


    def getLocationGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Group':

        data = self.client.call(
            self.service,
            'getLocationGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Group import Group
        return Group(data)


    def getManagedBareMetalInstances(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getManagedBareMetalInstances',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getManagedHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getManagedHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getManagedVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getManagedVirtualGuests',
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


    def getPrivateNetworkOnlyHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getPrivateNetworkOnlyHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


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


    def getTotalBandwidthAllocated(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedLong':

        data = self.client.call(
            self.service,
            'getTotalBandwidthAllocated',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


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
        return Guest(data)


