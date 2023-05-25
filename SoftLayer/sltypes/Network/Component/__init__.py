from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Component(Entity):
    """Every piece of hardware running in SoftLayer's datacenters connected to the public, private, or management
networks (where applicable) have a corresponding network component. These network components are modeled by
the SoftLayer_Network_Component data type. These data types reflect the servers' local ethernet and remote
management interfaces."""
    duplexModeId: str
    hardwareId: int
    id_: int
    ipmiIpAddress: str
    ipmiMacAddress: str
    macAddress: str
    maxSpeed: int
    modifyDate: datetime
    name: str
    networkVlanId: int
    port: int
    primaryIpAddress: str
    speed: int
    status: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Component'

    def addNetworkVlanTrunks(self, identifier: int, networkVlans: 'Network_Vlan') -> list['Network_Vlan']:
        """Add VLAN trunks to a network component"""
        data = self.client.call('SoftLayer_Network_Component', 'addNetworkVlanTrunks', networkVlans, id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def clearNetworkVlanTrunks(self, identifier: int) -> list['Network_Vlan']:
        """Remove all VLAN trunks from a network component"""
        data = self.client.call('SoftLayer_Network_Component', 'clearNetworkVlanTrunks', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getCustomBandwidthDataByDate(self, identifier: int, graphData: 'Container_Graph') -> 'Container_Graph':
        """Retrieve bandwidth graph by date."""
        data = self.client.call('SoftLayer_Network_Component', 'getCustomBandwidthDataByDate', graphData, id=identifier)
        from SoftLayer.sltypes.Container_Graph import Container_Graph
        return data

    def getObject(self, identifier: int) -> 'Network_Component':
        """Retrieve a SoftLayer_Network_Component record."""
        data = self.client.call('SoftLayer_Network_Component', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getPortStatistics(self, identifier: int) -> 'Container_Network_Port_Statistic':
        """Retrieve various network statistics for the specific port."""
        data = self.client.call('SoftLayer_Network_Component', 'getPortStatistics', id=identifier)
        from SoftLayer.sltypes.Container_Network_Port_Statistic import Container_Network_Port_Statistic
        return data

    def removeNetworkVlanTrunks(self, identifier: int, networkVlans: 'Network_Vlan') -> list['Network_Vlan']:
        """Remove VLAN trunks from a network component"""
        data = self.client.call('SoftLayer_Network_Component', 'removeNetworkVlanTrunks', networkVlans, id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getActiveCommand(self, identifier: int) -> 'Hardware_Component_RemoteManagement_Command_Request':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getActiveCommand', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_RemoteManagement_Command_Request import Hardware_Component_RemoteManagement_Command_Request
        return data

    def getDownlinkComponent(self, identifier: int) -> 'Network_Component':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getDownlinkComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getDuplexMode(self, identifier: int) -> 'Network_Component_Duplex_Mode':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getDuplexMode', id=identifier)
        from SoftLayer.sltypes.Network_Component_Duplex_Mode import Network_Component_Duplex_Mode
        return data

    def getHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHighAvailabilityFirewallFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getHighAvailabilityFirewallFlag', id=identifier)
        return data

    def getIpAddressBindings(self, identifier: int) -> list['Network_Component_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getIpAddressBindings', id=identifier)
        from SoftLayer.sltypes.Network_Component_IpAddress import Network_Component_IpAddress
        return data

    def getIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getLastCommand(self, identifier: int) -> 'Hardware_Component_RemoteManagement_Command_Request':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getLastCommand', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_RemoteManagement_Command_Request import Hardware_Component_RemoteManagement_Command_Request
        return data

    def getMetricTrackingObject(self, identifier: int) -> 'Metric_Tracking_Object':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getMetricTrackingObject', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object import Metric_Tracking_Object
        return data

    def getNetworkComponentFirewall(self, identifier: int) -> 'Network_Component_Firewall':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getNetworkComponentFirewall', id=identifier)
        from SoftLayer.sltypes.Network_Component_Firewall import Network_Component_Firewall
        return data

    def getNetworkComponentGroup(self, identifier: int) -> 'Network_Component_Group':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getNetworkComponentGroup', id=identifier)
        from SoftLayer.sltypes.Network_Component_Group import Network_Component_Group
        return data

    def getNetworkHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getNetworkHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getNetworkVlan(self, identifier: int) -> 'Network_Vlan':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getNetworkVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getNetworkVlanTrunks(self, identifier: int) -> list['Network_Component_Network_Vlan_Trunk']:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getNetworkVlanTrunks', id=identifier)
        from SoftLayer.sltypes.Network_Component_Network_Vlan_Trunk import Network_Component_Network_Vlan_Trunk
        return data

    def getNetworkVlansTrunkable(self, identifier: int) -> list['Network_Vlan']:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getNetworkVlansTrunkable', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getPrimaryIpAddressRecord(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getPrimaryIpAddressRecord', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getPrimarySubnet(self, identifier: int) -> 'Network_Subnet':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getPrimarySubnet', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getPrimaryVersion6IpAddressRecord(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getPrimaryVersion6IpAddressRecord', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getRecentCommands(self, identifier: int) -> list['Hardware_Component_RemoteManagement_Command_Request']:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getRecentCommands', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_RemoteManagement_Command_Request import Hardware_Component_RemoteManagement_Command_Request
        return data

    def getRedundancyCapableFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getRedundancyCapableFlag', id=identifier)
        return data

    def getRedundancyEnabledFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getRedundancyEnabledFlag', id=identifier)
        return data

    def getRemoteManagementUsers(self, identifier: int) -> list['Hardware_Component_RemoteManagement_User']:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getRemoteManagementUsers', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_RemoteManagement_User import Hardware_Component_RemoteManagement_User
        return data

    def getRouter(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getRouter', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getStorageNetworkFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getStorageNetworkFlag', id=identifier)
        return data

    def getSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getUplinkComponent(self, identifier: int) -> 'Network_Component':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getUplinkComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getUplinkDuplexMode(self, identifier: int) -> 'Network_Component_Duplex_Mode':
        """"""
        data = self.client.call('SoftLayer_Network_Component', 'getUplinkDuplexMode', id=identifier)
        from SoftLayer.sltypes.Network_Component_Duplex_Mode import Network_Component_Duplex_Mode
        return data
