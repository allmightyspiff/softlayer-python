# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Vlan_Firewall(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Vlan_Firewall'
        self.client = client

    def approveBypassRequest(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'approveBypassRequest',
            
        )
        
        return data


    def getFirewallFirmwareVersion(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFirewallFirmwareVersion',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan_Firewall':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan.Firewall import Firewall
        return Firewall(data)


    def hasActiveTransactions(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'hasActiveTransactions',
            
        )
        
        return data


    def isAccountAllowed(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isAccountAllowed',
            
        )
        
        return data


    def isHighAvailabilityUpgradeAvailable(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isHighAvailabilityUpgradeAvailable',
            
        )
        
        return data


    def rejectBypassRequest(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'rejectBypassRequest',
            
        )
        
        return data


    def restoreDefaults(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'restoreDefaults',
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


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


    def updateRouteBypass(
        self,
        bypass: boolean,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'updateRouteBypass',
            bypass,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getAccountId(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getAccountId',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


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


    def getBypassRequestStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBypassRequestStatus',
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


    def getFirewallType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFirewallType',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getFullyQualifiedDomainName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFullyQualifiedDomainName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getManagementCredentials(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component_Password':

        data = self.client.call(
            self.service,
            'getManagementCredentials',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component.Password import Password
        return Password(data)


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


    def getNetworkFirewallUpdateRequests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Firewall_Update_Request]':

        data = self.client.call(
            self.service,
            'getNetworkFirewallUpdateRequests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Firewall.Update.Request import Request
        return Request(data)


    def getNetworkGateway(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway':

        data = self.client.call(
            self.service,
            'getNetworkGateway',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway import Gateway
        return Gateway(data)


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


    def getRules(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Vlan_Firewall_Rule]':

        data = self.client.call(
            self.service,
            'getRules',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Vlan.Firewall.Rule import Rule
        return Rule(data)


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


