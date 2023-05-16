# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Application_Delivery_Controller(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Application_Delivery_Controller'
        self.client = client

    def createLiveLoadBalancer(
        self,
        loadBalancer: 'SoftLayer_Network_LoadBalancer_VirtualIpAddress',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createLiveLoadBalancer',
            loadBalancer,
            id=identifier
        )
        
        return data


    def deleteLiveLoadBalancer(
        self,
        loadBalancer: 'SoftLayer_Network_LoadBalancer_VirtualIpAddress',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteLiveLoadBalancer',
            loadBalancer,
            id=identifier
        )
        
        return data


    def deleteLiveLoadBalancerService(
        self,
        service: 'SoftLayer_Network_LoadBalancer_Service',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteLiveLoadBalancerService',
            service,
            id=identifier
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_Network_Application_Delivery_Controller',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def getBandwidthDataByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        networkType: str,
        identifier: int
    ) -> 'list[SoftLayer_Metric_Tracking_Object_Data]':

        data = self.client.call(
            self.service,
            'getBandwidthDataByDate',
            startDateTime,
            endDateTime,
            networkType,
            id=identifier
        )
        from SoftLayer.datatypes.Metric.Tracking.Object.Data import Data
        return Data(data)


    def getBandwidthImageByDate(
        self,
        startDateTime: str,
        endDateTime: str,
        networkType: str,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getBandwidthImageByDate',
            startDateTime,
            endDateTime,
            networkType,
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


    def getLiveLoadBalancerServiceGraphImage(
        self,
        service: 'SoftLayer_Network_LoadBalancer_Service',
        graphType: str,
        metric: str,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getLiveLoadBalancerServiceGraphImage',
            service,
            graphType,
            metric,
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller import Controller
        return Controller(data)


    def restoreBaseConfiguration(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'restoreBaseConfiguration',
            id=identifier
        )
        
        return data


    def restoreConfiguration(
        self,
        configurationHistoryId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'restoreConfiguration',
            configurationHistoryId,
            id=identifier
        )
        
        return data


    def saveCurrentConfiguration(
        self,
        notes: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_Configuration_History':

        data = self.client.call(
            self.service,
            'saveCurrentConfiguration',
            notes,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.Configuration.History import History
        return History(data)


    def updateLiveLoadBalancer(
        self,
        loadBalancer: 'SoftLayer_Network_LoadBalancer_VirtualIpAddress',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateLiveLoadBalancer',
            loadBalancer,
            id=identifier
        )
        
        return data


    def updateNetScalerLicense(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'updateNetScalerLicense',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


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


    def getBillingItem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Network_Application_Delivery_Controller':

        data = self.client.call(
            self.service,
            'getBillingItem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Network.Application.Delivery.Controller import Controller
        return Controller(data)


    def getConfigurationHistory(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_Configuration_History]':

        data = self.client.call(
            self.service,
            'getConfigurationHistory',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.Configuration.History import History
        return History(data)


    def getDatacenter(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getDatacenter',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getDescription(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDescription',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


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


    def getLicenseExpirationDate(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'dateTime':

        data = self.client.call(
            self.service,
            'getLicenseExpirationDate',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLoadBalancers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LoadBalancer_VirtualIpAddress]':

        data = self.client.call(
            self.service,
            'getLoadBalancers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return VirtualIpAddress(data)


    def getManagedResourceFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getManagedResourceFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getManagementIpAddress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getManagementIpAddress',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNetworkVlan(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan':

        data = self.client.call(
            self.service,
            'getNetworkVlan',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getNetworkVlans(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Vlan]':

        data = self.client.call(
            self.service,
            'getNetworkVlans',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


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


    def getPassword(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component_Password':

        data = self.client.call(
            self.service,
            'getPassword',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component.Password import Password
        return Password(data)


    def getPrimaryIpAddress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPrimaryIpAddress',
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


    def getSubnets(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getSubnets',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getTagReferences(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':

        data = self.client.call(
            self.service,
            'getTagReferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return Reference(data)


    def getType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_Type':

        data = self.client.call(
            self.service,
            'getType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.Type import Type
        return Type(data)


    def getVirtualIpAddresses(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress]':

        data = self.client.call(
            self.service,
            'getVirtualIpAddresses',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return VirtualIpAddress(data)


