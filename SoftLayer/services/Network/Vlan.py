# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Vlan(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Vlan'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Network_Vlan
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCancelFailureReasons(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getCancelFailureReasons',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getFirewallProtectableIpAddresses(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':
        data = self.client.call(
            self.service,
            'getFirewallProtectableIpAddresses',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return SL_IpAddress(data)

# This file was automatically generated with tools/generateTypes.py
    def getFirewallProtectableSubnets(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Subnet]':
        data = self.client.call(
            self.service,
            'getFirewallProtectableSubnets',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrivateVlan(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Vlan':
        data = self.client.call(
            self.service,
            'getPrivateVlan',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrivateVlanByIpAddress(
        self,
        ipAddress: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Vlan':
        data = self.client.call(
            self.service,
            'getPrivateVlanByIpAddress',
            ipAddress,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
    def getPublicVlanByFqdn(
        self,
        fqdn: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Vlan':
        data = self.client.call(
            self.service,
            'getPublicVlanByFqdn',
            fqdn,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
    def getReverseDomainRecords(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Dns_Domain]':
        data = self.client.call(
            self.service,
            'getReverseDomainRecords',
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return SL_Domain(data)

# This file was automatically generated with tools/generateTypes.py
    def getVlanForIpAddress(
        self,
        ipAddress: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Vlan':
        data = self.client.call(
            self.service,
            'getVlanForIpAddress',
            ipAddress,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def updateFirewallIntraVlanCommunication(
        self,
        enabled: boolean
    ) -> 'void':
        data = self.client.call(
            self.service,
            'updateFirewallIntraVlanCommunication',
            enabled
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def upgrade(
        self,
        
    ) -> 'SoftLayer_Container_Product_Order_Network_Vlan':
        data = self.client.call(
            self.service,
            'upgrade',
            
        )
        from SoftLayer.datatypes.Container.Product.Order.Network.Vlan import Vlan
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getAdditionalPrimarySubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':
        data = self.client.call(
            self.service,
            'getAdditionalPrimarySubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttachedNetworkGateway(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway':
        data = self.client.call(
            self.service,
            'getAttachedNetworkGateway',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway import Gateway
        return SL_Gateway(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttachedNetworkGatewayFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getAttachedNetworkGatewayFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAttachedNetworkGatewayVlan(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway_Vlan':
        data = self.client.call(
            self.service,
            'getAttachedNetworkGatewayVlan',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway.Vlan import Vlan
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getDedicatedFirewallFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getDedicatedFirewallFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getExtensionRouter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Router':
        data = self.client.call(
            self.service,
            'getExtensionRouter',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Router import Router
        return SL_Router(data)

# This file was automatically generated with tools/generateTypes.py
    def getFirewallGuestNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Component_Firewall]':
        data = self.client.call(
            self.service,
            'getFirewallGuestNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Component.Firewall import Firewall
        return SL_Firewall(data)

# This file was automatically generated with tools/generateTypes.py
    def getFirewallInterfaces(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Firewall_Module_Context_Interface]':
        data = self.client.call(
            self.service,
            'getFirewallInterfaces',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Firewall.Module.Context.Interface import Interface
        return SL_Interface(data)

# This file was automatically generated with tools/generateTypes.py
    def getFirewallNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Component_Firewall]':
        data = self.client.call(
            self.service,
            'getFirewallNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Component.Firewall import Firewall
        return SL_Firewall(data)

# This file was automatically generated with tools/generateTypes.py
    def getFirewallRules(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Vlan_Firewall_Rule]':
        data = self.client.call(
            self.service,
            'getFirewallRules',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Vlan.Firewall.Rule import Rule
        return SL_Rule(data)

# This file was automatically generated with tools/generateTypes.py
    def getGuestNetworkComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Network_Component]':
        data = self.client.call(
            self.service,
            'getGuestNetworkComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getHighAvailabilityFirewallFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getHighAvailabilityFirewallFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getLocalDiskStorageCapabilityFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getLocalDiskStorageCapabilityFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getNetwork(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network':
        data = self.client.call(
            self.service,
            'getNetwork',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network import Network
        return SL_Network(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkComponentTrunks(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Component_Network_Vlan_Trunk]':
        data = self.client.call(
            self.service,
            'getNetworkComponentTrunks',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Component.Network.Vlan.Trunk import Trunk
        return SL_Trunk(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkComponentsTrunkable(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Component]':
        data = self.client.call(
            self.service,
            'getNetworkComponentsTrunkable',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkSpace(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getNetworkSpace',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getNetworkVlanFirewall(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan_Firewall':
        data = self.client.call(
            self.service,
            'getNetworkVlanFirewall',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan.Firewall import Firewall
        return SL_Firewall(data)

# This file was automatically generated with tools/generateTypes.py
    def getPodName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPodName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPrimaryRouter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Router':
        data = self.client.call(
            self.service,
            'getPrimaryRouter',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Router import Router
        return SL_Router(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrimarySubnet(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet':
        data = self.client.call(
            self.service,
            'getPrimarySubnet',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrimarySubnetVersion6(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet':
        data = self.client.call(
            self.service,
            'getPrimarySubnetVersion6',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrimarySubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':
        data = self.client.call(
            self.service,
            'getPrimarySubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrivateNetworkGateways(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Gateway]':
        data = self.client.call(
            self.service,
            'getPrivateNetworkGateways',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Gateway import Gateway
        return SL_Gateway(data)

# This file was automatically generated with tools/generateTypes.py
    def getProtectedIpAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':
        data = self.client.call(
            self.service,
            'getProtectedIpAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return SL_IpAddress(data)

# This file was automatically generated with tools/generateTypes.py
    def getPublicNetworkGateways(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Gateway]':
        data = self.client.call(
            self.service,
            'getPublicNetworkGateways',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Gateway import Gateway
        return SL_Gateway(data)

# This file was automatically generated with tools/generateTypes.py
    def getSanStorageCapabilityFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getSanStorageCapabilityFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getSecondaryRouter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':
        data = self.client.call(
            self.service,
            'getSecondaryRouter',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getSecondarySubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':
        data = self.client.call(
            self.service,
            'getSecondarySubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Reference(data)

# This file was automatically generated with tools/generateTypes.py
    def getTotalPrimaryIpAddressCount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':
        data = self.client.call(
            self.service,
            'getTotalPrimaryIpAddressCount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan_Type':
        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan.Type import Type
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Guest(data)


