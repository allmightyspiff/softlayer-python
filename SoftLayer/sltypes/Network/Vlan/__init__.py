from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Vlan(Entity):
    """VLANs comprise the fundamental segmentation model on the network, isolating customer networks from one
another.   VLANs are scoped to a single network, generally public or private, and a pod. Through association
to a single VLAN, assigned subnets are routed on the network to provide IP address connectivity.   Compute
devices are associated to a single VLAN per active network, to which the Primary IP Address and containing
Primary Subnet belongs. Additional VLANs may be associated to bare metal devices using VLAN trunking.   [VLAN
at Wikipedia](https://en.wikipedia.org/wiki/VLAN)"""
    accountId: int
    fullyQualifiedName: str
    id_: int
    modifyDate: datetime
    name: str
    note: str
    primarySubnetId: int
    vlanNumber: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Vlan'

    def editObject(self, identifier: int, templateObject: 'Network_Vlan') -> bool:
        """Update the properties of this VLAN"""
        data = self.client.call('SoftLayer_Network_Vlan', 'editObject', templateObject, id=identifier)
        return data

    def getCancelFailureReasons(self, identifier: int) -> list[str]:
        """A list of descriptions why this VLAN may not be cancelled."""
        data = self.client.call('SoftLayer_Network_Vlan', 'getCancelFailureReasons', id=identifier)
        return data

    def getFirewallProtectableIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """[DEPRECATED] Retrieve the IP addresses routed on this VLAN that are protectable by a Hardware Firewall."""
        data = self.client.call('SoftLayer_Network_Vlan', 'getFirewallProtectableIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getFirewallProtectableSubnets(self, identifier: int) -> list['Network_Subnet']:
        """[DEPRECATED] Retrieve the subnets routed on this VLAN that are protectable by a Hardware Firewall."""
        data = self.client.call('SoftLayer_Network_Vlan', 'getFirewallProtectableSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getObject(self, identifier: int) -> 'Network_Vlan':
        """Retrieve a SoftLayer_Network_Vlan record."""
        data = self.client.call('SoftLayer_Network_Vlan', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getPrivateVlan(self, identifier: int) -> 'Network_Vlan':
        """[DEPRECATED] Retrieve a private VLAN connected to one or more hosts also connected to this public VLAN."""
        data = self.client.call('SoftLayer_Network_Vlan', 'getPrivateVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getPrivateVlanByIpAddress(self, ipAddress: str) -> 'Network_Vlan':
        """[DEPRECATED] Retrieve the private network VLAN associated with an IP address."""
        data = self.client.call('SoftLayer_Network_Vlan', 'getPrivateVlanByIpAddress', ipAddress)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getPublicVlanByFqdn(self, fqdn: str) -> 'Network_Vlan':
        """[DEPRECATED] Retrieve a public VLAN by an associated host's fully-qualified domain name"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getPublicVlanByFqdn', fqdn)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getReverseDomainRecords(self, identifier: int) -> list['Dns_Domain']:
        """[DEPRECATED] DNS PTR records associated with IP addresses routed on this VLAN."""
        data = self.client.call('SoftLayer_Network_Vlan', 'getReverseDomainRecords', id=identifier)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def getVlanForIpAddress(self, ipAddress: str) -> 'Network_Vlan':
        """The VLAN on which the given IP address is routed."""
        data = self.client.call('SoftLayer_Network_Vlan', 'getVlanForIpAddress', ipAddress)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def setTags(self, identifier: int, tags: str) -> bool:
        """Associate tags with this VLAN."""
        data = self.client.call('SoftLayer_Network_Vlan', 'setTags', tags, id=identifier)
        return data

    def updateFirewallIntraVlanCommunication(self, identifier: int, enabled: bool) -> None:
        """[DEPRECATED] Update the firewall associated to this VLAN to allow or disallow intra-VLAN communication."""
        data = self.client.call('SoftLayer_Network_Vlan', 'updateFirewallIntraVlanCommunication', enabled, id=identifier)
        return data

    def upgrade(self, identifier: int) -> 'Container_Product_Order_Network_Vlan':
        """Convert the VLAN to a paid resource, from an Automatic to a Premium VLAN."""
        data = self.client.call('SoftLayer_Network_Vlan', 'upgrade', id=identifier)
        from SoftLayer.sltypes.Container_Product_Order_Network_Vlan import Container_Product_Order_Network_Vlan
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAdditionalPrimarySubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getAdditionalPrimarySubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getAttachedNetworkGateway(self, identifier: int) -> 'Network_Gateway':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getAttachedNetworkGateway', id=identifier)
        from SoftLayer.sltypes.Network_Gateway import Network_Gateway
        return data

    def getAttachedNetworkGatewayFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getAttachedNetworkGatewayFlag', id=identifier)
        return data

    def getAttachedNetworkGatewayVlan(self, identifier: int) -> 'Network_Gateway_Vlan':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getAttachedNetworkGatewayVlan', id=identifier)
        from SoftLayer.sltypes.Network_Gateway_Vlan import Network_Gateway_Vlan
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getDatacenter(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getDedicatedFirewallFlag(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getDedicatedFirewallFlag', id=identifier)
        return data

    def getExtensionRouter(self, identifier: int) -> 'Hardware_Router':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getExtensionRouter', id=identifier)
        from SoftLayer.sltypes.Hardware_Router import Hardware_Router
        return data

    def getFirewallGuestNetworkComponents(self, identifier: int) -> list['Network_Component_Firewall']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getFirewallGuestNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Network_Component_Firewall import Network_Component_Firewall
        return data

    def getFirewallInterfaces(self, identifier: int) -> list['Network_Firewall_Module_Context_Interface']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getFirewallInterfaces', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_Module_Context_Interface import Network_Firewall_Module_Context_Interface
        return data

    def getFirewallNetworkComponents(self, identifier: int) -> list['Network_Component_Firewall']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getFirewallNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Network_Component_Firewall import Network_Component_Firewall
        return data

    def getFirewallRules(self, identifier: int) -> list['Network_Vlan_Firewall_Rule']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getFirewallRules', id=identifier)
        from SoftLayer.sltypes.Network_Vlan_Firewall_Rule import Network_Vlan_Firewall_Rule
        return data

    def getGuestNetworkComponents(self, identifier: int) -> list['Virtual_Guest_Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getGuestNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component import Virtual_Guest_Network_Component
        return data

    def getHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHighAvailabilityFirewallFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getHighAvailabilityFirewallFlag', id=identifier)
        return data

    def getLocalDiskStorageCapabilityFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getLocalDiskStorageCapabilityFlag', id=identifier)
        return data

    def getNetwork(self, identifier: int) -> 'Network':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getNetwork', id=identifier)
        from SoftLayer.sltypes.Network import Network
        return data

    def getNetworkComponentTrunks(self, identifier: int) -> list['Network_Component_Network_Vlan_Trunk']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getNetworkComponentTrunks', id=identifier)
        from SoftLayer.sltypes.Network_Component_Network_Vlan_Trunk import Network_Component_Network_Vlan_Trunk
        return data

    def getNetworkComponents(self, identifier: int) -> list['Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getNetworkComponents', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getNetworkComponentsTrunkable(self, identifier: int) -> list['Network_Component']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getNetworkComponentsTrunkable', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getNetworkSpace(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getNetworkSpace', id=identifier)
        return data

    def getNetworkVlanFirewall(self, identifier: int) -> 'Network_Vlan_Firewall':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getNetworkVlanFirewall', id=identifier)
        from SoftLayer.sltypes.Network_Vlan_Firewall import Network_Vlan_Firewall
        return data

    def getPodName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getPodName', id=identifier)
        return data

    def getPrimaryRouter(self, identifier: int) -> 'Hardware_Router':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getPrimaryRouter', id=identifier)
        from SoftLayer.sltypes.Hardware_Router import Hardware_Router
        return data

    def getPrimarySubnet(self, identifier: int) -> 'Network_Subnet':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getPrimarySubnet', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getPrimarySubnetVersion6(self, identifier: int) -> 'Network_Subnet':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getPrimarySubnetVersion6', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getPrimarySubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getPrimarySubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getPrivateNetworkGateways(self, identifier: int) -> list['Network_Gateway']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getPrivateNetworkGateways', id=identifier)
        from SoftLayer.sltypes.Network_Gateway import Network_Gateway
        return data

    def getProtectedIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getProtectedIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getPublicNetworkGateways(self, identifier: int) -> list['Network_Gateway']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getPublicNetworkGateways', id=identifier)
        from SoftLayer.sltypes.Network_Gateway import Network_Gateway
        return data

    def getSanStorageCapabilityFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getSanStorageCapabilityFlag', id=identifier)
        return data

    def getSecondaryRouter(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getSecondaryRouter', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getSecondarySubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getSecondarySubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getTagReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getTagReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data

    def getTotalPrimaryIpAddressCount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getTotalPrimaryIpAddressCount', id=identifier)
        return data

    def getType(self, identifier: int) -> 'Network_Vlan_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getType', id=identifier)
        from SoftLayer.sltypes.Network_Vlan_Type import Network_Vlan_Type
        return data

    def getVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Network_Vlan', 'getVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data
