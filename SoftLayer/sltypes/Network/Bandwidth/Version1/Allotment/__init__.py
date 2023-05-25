from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Bandwidth_Version1_Allotment(Entity):
    """The SoftLayer_Network_Bandwidth_Version1_Allotment class provides methods and data structures necessary to
work with an array of hardware objects associated with a single Bandwidth Pooling."""
    accountId: int
    bandwidthAllotmentTypeId: int
    createDate: datetime
    endDate: datetime
    id_: int
    locationGroupId: int
    name: str
    serviceProviderId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Bandwidth_Version1_Allotment'

    def createObject(self, templateObject: 'Network_Bandwidth_Version1_Allotment') -> 'Network_Bandwidth_Version1_Allotment':
        """create a new allotment by passing in a allotment object."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'createObject', templateObject)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Bandwidth_Version1_Allotment') -> bool:
        """Edit a bandwidth allotment"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'editObject', templateObject, id=identifier)
        return data

    def getBandwidthForDateRange(self, identifier: int, startDate: datetime, endDate: datetime) -> list['Metric_Tracking_Object_Data']:
        """Retrieve bandwidth data from a tracking object."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getBandwidthForDateRange', startDate, endDate, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getBandwidthImage(self, identifier: int, networkType: str, snapshotRange: str, draw: bool, dateSpecified: datetime, dateSpecifiedEnd: datetime) -> 'Container_Bandwidth_GraphOutputs':
        """generate a graph image of all the bandwidth usage for an entire allotment of servers."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getBandwidthImage', networkType, snapshotRange, draw, dateSpecified, dateSpecifiedEnd, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getCustomBandwidthDataByDate(self, identifier: int, graphData: 'Container_Graph') -> 'Container_Graph':
        """Retrieve bandwidth graph by date."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getCustomBandwidthDataByDate', graphData, id=identifier)
        from SoftLayer.sltypes.Container_Graph import Container_Graph
        return data

    def getObject(self, identifier: int) -> 'Network_Bandwidth_Version1_Allotment':
        """Retrieve a SoftLayer_Network_Bandwidth_Version1_Allotment record."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getVdrMemberRecurringFee(self, identifier: int) -> float:
        """Gets the monthly recurring fee of a pooled server."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getVdrMemberRecurringFee', id=identifier)
        return data

    def reassignServers(self, templateObjects: 'Hardware', newAllotmentId: int) -> bool:
        """reassign a collection of servers to a different allotment."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'reassignServers', templateObjects, newAllotmentId)
        return data

    def requestVdrCancellation(self, identifier: int) -> bool:
        """cancel a bandwidth pooling and assign contents, if any, to bandwidth pool."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'requestVdrCancellation', id=identifier)
        return data

    def requestVdrContentUpdates(self, identifier: int, hardwareToAdd: 'Hardware', hardwareToRemove: 'Hardware', cloudsToAdd: 'Virtual_Guest', cloudsToRemove: 'Virtual_Guest', optionalAllotmentId: int, adcToAdd: 'Network_Application_Delivery_Controller', adcToRemove: 'Network_Application_Delivery_Controller') -> bool:
        """Move servers into our out of a bandwidth pool."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'requestVdrContentUpdates', hardwareToAdd, hardwareToRemove, cloudsToAdd, cloudsToRemove, optionalAllotmentId, adcToAdd, adcToRemove, id=identifier)
        return data

    def setVdrContent(self, identifier: int, hardware: 'Hardware', bareMetalServers: 'Hardware', virtualServerInstance: 'Virtual_Guest', adc: 'Network_Application_Delivery_Controller', optionalAllotmentId: int) -> bool:
        """Update bandwidth pool."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'setVdrContent', hardware, bareMetalServers, virtualServerInstance, adc, optionalAllotmentId, id=identifier)
        return data

    def unassignServers(self, templateObjects: 'Hardware') -> bool:
        """unassign a collection of servers from an allotment and insert them into the accounts VPR."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'unassignServers', templateObjects)
        return data

    def voidPendingServerMove(self, identifier: int, id_: int, type_: str) -> bool:
        """Void a pending server removal from this bandwidth pooling."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'voidPendingServerMove', id, type, id=identifier)
        return data

    def voidPendingVdrCancellation(self, identifier: int) -> bool:
        """Void a pending cancellation on a bandwidth pool."""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'voidPendingVdrCancellation', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getActiveDetails(self, identifier: int) -> list['Network_Bandwidth_Version1_Allotment_Detail']:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getActiveDetails', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment_Detail import Network_Bandwidth_Version1_Allotment_Detail
        return data

    def getApplicationDeliveryControllers(self, identifier: int) -> list['Network_Application_Delivery_Controller']:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getApplicationDeliveryControllers', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller import Network_Application_Delivery_Controller
        return data

    def getAverageDailyPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getAverageDailyPublicBandwidthUsage', id=identifier)
        return data

    def getBandwidthAllotmentType(self, identifier: int) -> 'Network_Bandwidth_Version1_Allotment_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getBandwidthAllotmentType', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment_Type import Network_Bandwidth_Version1_Allotment_Type
        return data

    def getBareMetalInstances(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getBareMetalInstances', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getBillingCycleBandwidthUsage(self, identifier: int) -> list['Network_Bandwidth_Usage']:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getBillingCycleBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBillingCyclePrivateBandwidthUsage(self, identifier: int) -> 'Network_Bandwidth_Usage':
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getBillingCyclePrivateBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBillingCyclePublicBandwidthUsage(self, identifier: int) -> 'Network_Bandwidth_Usage':
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getBillingCyclePublicBandwidthUsage', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Usage import Network_Bandwidth_Usage
        return data

    def getBillingCyclePublicUsageTotal(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getBillingCyclePublicUsageTotal', id=identifier)
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getCurrentBandwidthSummary(self, identifier: int) -> 'Metric_Tracking_Object_Bandwidth_Summary':
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getCurrentBandwidthSummary', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Bandwidth_Summary import Metric_Tracking_Object_Bandwidth_Summary
        return data

    def getDetails(self, identifier: int) -> list['Network_Bandwidth_Version1_Allotment_Detail']:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getDetails', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment_Detail import Network_Bandwidth_Version1_Allotment_Detail
        return data

    def getHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getInboundPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getInboundPublicBandwidthUsage', id=identifier)
        return data

    def getLocationGroup(self, identifier: int) -> 'Location_Group':
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getLocationGroup', id=identifier)
        from SoftLayer.sltypes.Location_Group import Location_Group
        return data

    def getManagedBareMetalInstances(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getManagedBareMetalInstances', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getManagedHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getManagedHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getManagedVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getManagedVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getMetricTrackingObject(self, identifier: int) -> 'Metric_Tracking_Object':
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getMetricTrackingObject', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object import Metric_Tracking_Object
        return data

    def getMetricTrackingObjectId(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getMetricTrackingObjectId', id=identifier)
        return data

    def getOutboundPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getOutboundPublicBandwidthUsage', id=identifier)
        return data

    def getOverBandwidthAllocationFlag(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getOverBandwidthAllocationFlag', id=identifier)
        return data

    def getPrivateNetworkOnlyHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getPrivateNetworkOnlyHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getProjectedOverBandwidthAllocationFlag(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getProjectedOverBandwidthAllocationFlag', id=identifier)
        return data

    def getProjectedPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getProjectedPublicBandwidthUsage', id=identifier)
        return data

    def getServiceProvider(self, identifier: int) -> 'Service_Provider':
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getServiceProvider', id=identifier)
        from SoftLayer.sltypes.Service_Provider import Service_Provider
        return data

    def getTotalBandwidthAllocated(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getTotalBandwidthAllocated', id=identifier)
        return data

    def getVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'getVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data
