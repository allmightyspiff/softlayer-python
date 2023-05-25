from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Subnet(Entity):
    """A subnet represents a continguous range of IP addresses. The range is represented by the networkIdentifer and
cidr/netmask properties. The version of a subnet, whether IPv4 or IPv6, is represented by the version
property.   When routed, a subnet is associated to a VLAN on your account, which defines its scope on the
network. Depending on a subnet's route type, IP addresses may be reserved for network and internal functions,
the most common of which is the allocation of network, gateway and broadcast IP addresses.   An unrouted
subnet is not active on the network and may generally be routed within the datacenter in which it resides.
[Subnetwork at Wikipedia](http://en.wikipedia.org/wiki/Subnetwork)   [RFC950:Internet Standard Subnetting
Procedure](http://datatracker.ietf.org/doc/html/rfc950)"""
    broadcastAddress: str
    cidr: int
    gateway: str
    id_: int
    isCustomerOwned: bool
    isCustomerRoutable: bool
    modifyDate: datetime
    netmask: str
    networkIdentifier: str
    networkVlanId: int
    note: str
    sortOrder: str
    subnetType: str
    totalIpAddresses: float
    usableIpAddressCount: float
    version: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Subnet'

    def allowAccessToNetworkStorage(self, identifier: int, networkStorageTemplateObject: 'Network_Storage') -> bool:
        """Allow access to a SoftLayer_Network_Storage volume from this device."""
        data = self.client.call('SoftLayer_Network_Subnet', 'allowAccessToNetworkStorage', networkStorageTemplateObject, id=identifier)
        return data

    def allowAccessToNetworkStorageList(self, identifier: int, networkStorageTemplateObjects: 'Network_Storage') -> bool:
        """Allow access to multiple SoftLayer_Network_Storage volumes from this device."""
        data = self.client.call('SoftLayer_Network_Subnet', 'allowAccessToNetworkStorageList', networkStorageTemplateObjects, id=identifier)
        return data

    def clearRoute(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Subnet', 'clearRoute', id=identifier)
        return data

    def createReverseDomainRecords(self, identifier: int) -> 'Dns_Domain_Reverse':
        """Create the default PTR records for this subnet"""
        data = self.client.call('SoftLayer_Network_Subnet', 'createReverseDomainRecords', id=identifier)
        from SoftLayer.sltypes.Dns_Domain_Reverse import Dns_Domain_Reverse
        return data

    def createSubnetRouteUpdateTransaction(self, identifier: int, newEndPointIpAddress: str) -> bool:
        """create a new transaction to modify a subnet route."""
        data = self.client.call('SoftLayer_Network_Subnet', 'createSubnetRouteUpdateTransaction', newEndPointIpAddress, id=identifier)
        return data

    def createSwipTransaction(self, identifier: int) -> bool:
        """create a SWIP transaction for a subnet"""
        data = self.client.call('SoftLayer_Network_Subnet', 'createSwipTransaction', id=identifier)
        return data

    def editNote(self, identifier: int, note: str) -> bool:
        """Edit the note for this subnet."""
        data = self.client.call('SoftLayer_Network_Subnet', 'editNote', note, id=identifier)
        return data

    def findAllSubnetsAndActiveSwipTransactionStatus(self) -> list['Network_Subnet']:
        """Retrieve a list of subnets along with their SWIP transaction statuses."""
        data = self.client.call('SoftLayer_Network_Subnet', 'findAllSubnetsAndActiveSwipTransactionStatus')
        return data

    def getAttachedNetworkStorages(self, identifier: int, nasType: str) -> list['Network_Storage']:
        """The network storage devices and replicas this subnet has been granted access to."""
        data = self.client.call('SoftLayer_Network_Subnet', 'getAttachedNetworkStorages', nasType, id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAvailableNetworkStorages(self, identifier: int, nasType: str) -> list['Network_Storage']:
        """The network storage devices and replicas this subnet has NOT been granted access to. Only devices within the
same datacenter as this subnet will be returned."""
        data = self.client.call('SoftLayer_Network_Subnet', 'getAvailableNetworkStorages', nasType, id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getObject(self, identifier: int) -> 'Network_Subnet':
        """Retrieve a SoftLayer_Network_Subnet record."""
        data = self.client.call('SoftLayer_Network_Subnet', 'getObject', id=identifier)
        return data

    def getReverseDomainRecords(self, identifier: int) -> list['Dns_Domain']:
        """Retrieve all reverse DNS records associated with a subnet."""
        data = self.client.call('SoftLayer_Network_Subnet', 'getReverseDomainRecords', id=identifier)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def getRoutableEndpointIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """Retrieve IP addresses which may be used as a routing endpoint from a subnet."""
        data = self.client.call('SoftLayer_Network_Subnet', 'getRoutableEndpointIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getSubnetForIpAddress(self, ipAddress: str) -> 'Network_Subnet':
        """Retrieve an IP addresses's associated subnet."""
        data = self.client.call('SoftLayer_Network_Subnet', 'getSubnetForIpAddress', ipAddress)
        return data

    def removeAccessToNetworkStorageList(self, identifier: int, networkStorageTemplateObjects: 'Network_Storage') -> bool:
        """Removes access to multiple devices and replicas this subnet has been granted access to."""
        data = self.client.call('SoftLayer_Network_Subnet', 'removeAccessToNetworkStorageList', networkStorageTemplateObjects, id=identifier)
        return data

    def route(self, identifier: int, type_: str, identifier: str) -> bool:
        data = self.client.call('SoftLayer_Network_Subnet', 'route', type, identifier, id=identifier)
        return data

    def setTags(self, identifier: int, tags: str) -> bool:
        data = self.client.call('SoftLayer_Network_Subnet', 'setTags', tags, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getActiveRegistration(self, identifier: int) -> 'Network_Subnet_Registration':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getActiveRegistration', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Registration import Network_Subnet_Registration
        return data

    def getActiveSwipTransaction(self, identifier: int) -> 'Network_Subnet_Swip_Transaction':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getActiveSwipTransaction', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Swip_Transaction import Network_Subnet_Swip_Transaction
        return data

    def getActiveTransaction(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getActiveTransaction', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getAddressSpace(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getAddressSpace', id=identifier)
        return data

    def getAllowedHost(self, identifier: int) -> 'Network_Storage_Allowed_Host':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getAllowedHost', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
        return data

    def getAllowedNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getAllowedNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAllowedNetworkStorageReplicas(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getAllowedNetworkStorageReplicas', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getBoundDescendants(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getBoundDescendants', id=identifier)
        return data

    def getBoundRouterFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getBoundRouterFlag', id=identifier)
        return data

    def getBoundRouters(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getBoundRouters', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getChildren(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getChildren', id=identifier)
        return data

    def getDatacenter(self, identifier: int) -> 'Location_Datacenter':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location_Datacenter import Location_Datacenter
        return data

    def getDescendants(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getDescendants', id=identifier)
        return data

    def getDisplayLabel(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getDisplayLabel', id=identifier)
        return data

    def getEndPointIpAddress(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getEndPointIpAddress', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getGlobalIpRecord(self, identifier: int) -> 'Network_Subnet_IpAddress_Global':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getGlobalIpRecord', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress_Global import Network_Subnet_IpAddress_Global
        return data

    def getHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getNetworkComponentFirewall(self, identifier: int) -> 'Network_Component_Firewall':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getNetworkComponentFirewall', id=identifier)
        from SoftLayer.sltypes.Network_Component_Firewall import Network_Component_Firewall
        return data

    def getNetworkProtectionAddresses(self, identifier: int) -> list['Network_Protection_Address']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getNetworkProtectionAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Protection_Address import Network_Protection_Address
        return data

    def getNetworkTunnelContexts(self, identifier: int) -> list['Network_Tunnel_Module_Context']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getNetworkTunnelContexts', id=identifier)
        from SoftLayer.sltypes.Network_Tunnel_Module_Context import Network_Tunnel_Module_Context
        return data

    def getNetworkVlan(self, identifier: int) -> 'Network_Vlan':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getNetworkVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getPodName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getPodName', id=identifier)
        return data

    def getProtectedIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getProtectedIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getRegionalInternetRegistry(self, identifier: int) -> 'Network_Regional_Internet_Registry':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getRegionalInternetRegistry', id=identifier)
        from SoftLayer.sltypes.Network_Regional_Internet_Registry import Network_Regional_Internet_Registry
        return data

    def getRegistrations(self, identifier: int) -> list['Network_Subnet_Registration']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getRegistrations', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Registration import Network_Subnet_Registration
        return data

    def getReverseDomain(self, identifier: int) -> 'Dns_Domain':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getReverseDomain', id=identifier)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def getRoleKeyName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getRoleKeyName', id=identifier)
        return data

    def getRoleName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getRoleName', id=identifier)
        return data

    def getRoutingTypeKeyName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getRoutingTypeKeyName', id=identifier)
        return data

    def getRoutingTypeName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getRoutingTypeName', id=identifier)
        return data

    def getSwipTransaction(self, identifier: int) -> list['Network_Subnet_Swip_Transaction']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getSwipTransaction', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Swip_Transaction import Network_Subnet_Swip_Transaction
        return data

    def getTagReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getTagReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data

    def getUnboundDescendants(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getUnboundDescendants', id=identifier)
        return data

    def getUtilizedIpAddressCount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getUtilizedIpAddressCount', id=identifier)
        return data

    def getVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet', 'getVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data
