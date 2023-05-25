from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_Guest_Network_Component(Entity):
    """The virtual guest network component data type presents the structure in which all computing instance network
components are presented. Internally, the structure supports various virtualization platforms with no change
to external interaction.   A guest, also known as a virtual server, represents an allocation of resources on
a virtual host."""
    createDate: datetime
    guestId: int
    id_: int
    macAddress: str
    maxSpeed: int
    modifyDate: datetime
    name: str
    networkId: int
    port: int
    speed: int
    status: str
    uuid: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_Guest_Network_Component'

    def disable(self, identifier: int) -> bool:
        """Disable a network component to restrict network traffic"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'disable', id=identifier)
        return data

    def enable(self, identifier: int) -> bool:
        """Enable a network component to allow network traffic"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'enable', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Virtual_Guest_Network_Component':
        """Retrieve a SoftLayer_Virtual_Guest_Network_Component record."""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getObject', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component import Virtual_Guest_Network_Component
        return data

    def isPingable(self, identifier: int) -> bool:
        """Verifies if network component is pingable."""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'isPingable', id=identifier)
        return data

    def securityGroupsReady(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'securityGroupsReady', id=identifier)
        return data

    def getGuest(self, identifier: int) -> 'Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getGuest', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getHighAvailabilityFirewallFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getHighAvailabilityFirewallFlag', id=identifier)
        return data

    def getIcpBinding(self, identifier: int) -> 'Virtual_Guest_Network_Component_IcpBinding':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getIcpBinding', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component_IcpBinding import Virtual_Guest_Network_Component_IcpBinding
        return data

    def getIpAddressBindings(self, identifier: int) -> list['Virtual_Guest_Network_Component_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getIpAddressBindings', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component_IpAddress import Virtual_Guest_Network_Component_IpAddress
        return data

    def getNetworkComponentFirewall(self, identifier: int) -> 'Network_Component_Firewall':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getNetworkComponentFirewall', id=identifier)
        from SoftLayer.sltypes.Network_Component_Firewall import Network_Component_Firewall
        return data

    def getNetworkVlan(self, identifier: int) -> 'Network_Vlan':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getNetworkVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getPrimaryIpAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getPrimaryIpAddress', id=identifier)
        return data

    def getPrimaryIpAddressRecord(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getPrimaryIpAddressRecord', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getPrimarySubnet(self, identifier: int) -> 'Network_Subnet':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getPrimarySubnet', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getPrimaryVersion6IpAddressRecord(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getPrimaryVersion6IpAddressRecord', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getRouter(self, identifier: int) -> 'Hardware_Router':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getRouter', id=identifier)
        from SoftLayer.sltypes.Hardware_Router import Hardware_Router
        return data

    def getSecurityGroupBindings(self, identifier: int) -> list['Virtual_Network_SecurityGroup_NetworkComponentBinding']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getSecurityGroupBindings', id=identifier)
        from SoftLayer.sltypes.Virtual_Network_SecurityGroup_NetworkComponentBinding import Virtual_Network_SecurityGroup_NetworkComponentBinding
        return data

    def getSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Network_Component', 'getSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data
