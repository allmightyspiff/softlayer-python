from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Application_Delivery_Controller(Entity):
    """The SoftLayer_Network_Application_Delivery_Controller data type models a single instance of an application
delivery controller. Local properties are read only, except for a ''notes'' property, which can be used to
describe your application delivery controller service. The type's relational properties provide more
information to the service's function and login information to the controller's backend management if
advanced view is enabled."""
    accountId: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    name: str
    notes: str
    typeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Application_Delivery_Controller'

    def createLiveLoadBalancer(self, identifier: int, loadBalancer: 'Network_LoadBalancer_VirtualIpAddress') -> bool:
        """Add to or create load balancer service from a virtual IP address"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'createLiveLoadBalancer', loadBalancer, id=identifier)
        return data

    def deleteLiveLoadBalancer(self, identifier: int, loadBalancer: 'Network_LoadBalancer_VirtualIpAddress') -> bool:
        """Remove a virtual IP address from a load balancer"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'deleteLiveLoadBalancer', loadBalancer, id=identifier)
        return data

    def deleteLiveLoadBalancerService(self, identifier: int, service: 'Network_LoadBalancer_Service') -> bool:
        """Remove load balancer service"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'deleteLiveLoadBalancerService', service, id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Application_Delivery_Controller') -> bool:
        """Edit an application delivery controller record"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'editObject', templateObject, id=identifier)
        return data

    def getBandwidthDataByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime, networkType: str) -> list['Metric_Tracking_Object_Data']:
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getBandwidthDataByDate', startDateTime, endDateTime, networkType, id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Data import Metric_Tracking_Object_Data
        return data

    def getBandwidthImageByDate(self, identifier: int, startDateTime: datetime, endDateTime: datetime, networkType: str) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame
for an application delivery controller."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getBandwidthImageByDate', startDateTime, endDateTime, networkType, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getCustomBandwidthDataByDate(self, identifier: int, graphData: 'Container_Graph') -> 'Container_Graph':
        """Retrieve bandwidth graph by date."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getCustomBandwidthDataByDate', graphData, id=identifier)
        from SoftLayer.sltypes.Container_Graph import Container_Graph
        return data

    def getLiveLoadBalancerServiceGraphImage(self, identifier: int, service: 'Network_LoadBalancer_Service', graphType: str, metric: str) -> str:
        """Get the connection or status graph image for an application delivery controller service."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getLiveLoadBalancerServiceGraphImage', service, graphType, metric, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Application_Delivery_Controller':
        """Retrieve a SoftLayer_Network_Application_Delivery_Controller record."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getObject', id=identifier)
        return data

    def restoreBaseConfiguration(self, identifier: int) -> bool:
        """Restore an application delivery controller's base configuration state."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'restoreBaseConfiguration', id=identifier)
        return data

    def restoreConfiguration(self, identifier: int, configurationHistoryId: int) -> bool:
        """Restore an application delivery controller's configuration state."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'restoreConfiguration', configurationHistoryId, id=identifier)
        return data

    def saveCurrentConfiguration(self, identifier: int, notes: str) -> 'Network_Application_Delivery_Controller_Configuration_History':
        """Save an application delivery controller's configuration state."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'saveCurrentConfiguration', notes, id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_Configuration_History import Network_Application_Delivery_Controller_Configuration_History
        return data

    def updateLiveLoadBalancer(self, identifier: int, loadBalancer: 'Network_LoadBalancer_VirtualIpAddress') -> bool:
        """Edit a virtual IP address within a load balancer"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'updateLiveLoadBalancer', loadBalancer, id=identifier)
        return data

    def updateNetScalerLicense(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """Update the NetScaler VPX License."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'updateNetScalerLicense', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAverageDailyPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getAverageDailyPublicBandwidthUsage', id=identifier)
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item_Network_Application_Delivery_Controller':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Network_Application_Delivery_Controller import Billing_Item_Network_Application_Delivery_Controller
        return data

    def getConfigurationHistory(self, identifier: int) -> list['Network_Application_Delivery_Controller_Configuration_History']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getConfigurationHistory', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_Configuration_History import Network_Application_Delivery_Controller_Configuration_History
        return data

    def getDatacenter(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getDescription(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getDescription', id=identifier)
        return data

    def getInboundPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getInboundPublicBandwidthUsage', id=identifier)
        return data

    def getLicenseExpirationDate(self, identifier: int) -> datetime:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getLicenseExpirationDate', id=identifier)
        return data

    def getLoadBalancers(self, identifier: int) -> list['Network_LoadBalancer_VirtualIpAddress']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getLoadBalancers', id=identifier)
        from SoftLayer.sltypes.Network_LoadBalancer_VirtualIpAddress import Network_LoadBalancer_VirtualIpAddress
        return data

    def getManagedResourceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getManagedResourceFlag', id=identifier)
        return data

    def getManagementIpAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getManagementIpAddress', id=identifier)
        return data

    def getNetworkVlan(self, identifier: int) -> 'Network_Vlan':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getNetworkVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getNetworkVlans(self, identifier: int) -> list['Network_Vlan']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getNetworkVlans', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getOutboundPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getOutboundPublicBandwidthUsage', id=identifier)
        return data

    def getPassword(self, identifier: int) -> 'Software_Component_Password':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getPassword', id=identifier)
        from SoftLayer.sltypes.Software_Component_Password import Software_Component_Password
        return data

    def getPrimaryIpAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getPrimaryIpAddress', id=identifier)
        return data

    def getProjectedPublicBandwidthUsage(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getProjectedPublicBandwidthUsage', id=identifier)
        return data

    def getSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getTagReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getTagReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data

    def getType(self, identifier: int) -> 'Network_Application_Delivery_Controller_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getType', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_Type import Network_Application_Delivery_Controller_Type
        return data

    def getVirtualIpAddresses(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller', 'getVirtualIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress import Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
        return data
