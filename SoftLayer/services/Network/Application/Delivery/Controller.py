# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Application_Delivery_Controller(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Application_Delivery_Controller'
        self.client = client

    def createLiveLoadBalancer(
        self,
        loadBalancer: SoftLayer_Network_LoadBalancer_VirtualIpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createLiveLoadBalancer',
            loadBalancer
        )
        
        return data


    def deleteLiveLoadBalancer(
        self,
        loadBalancer: SoftLayer_Network_LoadBalancer_VirtualIpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteLiveLoadBalancer',
            loadBalancer
        )
        
        return data


    def deleteLiveLoadBalancerService(
        self,
        service: SoftLayer_Network_LoadBalancer_Service
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteLiveLoadBalancerService',
            service
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Network_Application_Delivery_Controller
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


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


    def getLiveLoadBalancerServiceGraphImage(
        self,
        service: SoftLayer_Network_LoadBalancer_Service,
        graphType: str,
        metric: str
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getLiveLoadBalancerServiceGraphImage',
            service,
            graphType,
            metric
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller import Controller
        return Controller(data)


    def restoreBaseConfiguration(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'restoreBaseConfiguration',
            
        )
        
        return data


    def restoreConfiguration(
        self,
        configurationHistoryId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'restoreConfiguration',
            configurationHistoryId
        )
        
        return data


    def saveCurrentConfiguration(
        self,
        notes: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_Configuration_History':

        data = self.client.call(
            self.service,
            'saveCurrentConfiguration',
            notes,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.Configuration.History import History
        return History(data)


    def updateLiveLoadBalancer(
        self,
        loadBalancer: SoftLayer_Network_LoadBalancer_VirtualIpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateLiveLoadBalancer',
            loadBalancer
        )
        
        return data


    def updateNetScalerLicense(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'updateNetScalerLicense',
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


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


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Network_Application_Delivery_Controller':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Network.Application.Delivery.Controller import Controller
        return Controller(data)


    def getConfigurationHistory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_Configuration_History]':

        data = self.client.call(
            self.service,
            'getConfigurationHistory',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.Configuration.History import History
        return History(data)


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


    def getDescription(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDescription',
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


    def getLicenseExpirationDate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'dateTime':

        data = self.client.call(
            self.service,
            'getLicenseExpirationDate',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLoadBalancers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LoadBalancer_VirtualIpAddress]':

        data = self.client.call(
            self.service,
            'getLoadBalancers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return VirtualIpAddress(data)


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


    def getManagementIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getManagementIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNetworkVlan(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan':

        data = self.client.call(
            self.service,
            'getNetworkVlan',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


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


    def getPassword(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component_Password':

        data = self.client.call(
            self.service,
            'getPassword',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component.Password import Password
        return Password(data)


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


    def getSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


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


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.Type import Type
        return Type(data)


    def getVirtualIpAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress]':

        data = self.client.call(
            self.service,
            'getVirtualIpAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return VirtualIpAddress(data)


