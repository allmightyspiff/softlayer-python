from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Subnet_IpAddress(Entity):
    """The SoftLayer_Network_Subnet_IpAddress data type contains general information relating to a single SoftLayer
IPv4 address."""
    id_: int
    ipAddress: str
    isBroadcast: bool
    isGateway: bool
    isNetwork: bool
    isReserved: bool
    note: str
    subnetId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Subnet_IpAddress'

    def allowAccessToNetworkStorage(self, identifier: int, networkStorageTemplateObject: 'Network_Storage') -> bool:
        """Allow access to a SoftLayer_Network_Storage volume from this device."""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'allowAccessToNetworkStorage', networkStorageTemplateObject, id=identifier)
        return data

    def allowAccessToNetworkStorageList(self, identifier: int, networkStorageTemplateObjects: 'Network_Storage') -> bool:
        """Allow access to multiple SoftLayer_Network_Storage volumes from this device."""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'allowAccessToNetworkStorageList', networkStorageTemplateObjects, id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Subnet_IpAddress') -> bool:
        """Edit the object by passing in a modified instance of the object"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'editObject', templateObject, id=identifier)
        return data

    def editObjects(self, templateObjects: 'Network_Subnet_IpAddress') -> bool:
        """Edit multiple objects by passing in modified instances of the object."""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'editObjects', templateObjects)
        return data

    def findByIpv4Address(self, ipAddress: str) -> 'Network_Subnet_IpAddress':
        """Search for an IP address record by IPv4 address."""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'findByIpv4Address', ipAddress)
        return data

    def getAttachedNetworkStorages(self, identifier: int, nasType: str) -> list['Network_Storage']:
        """Return a list of SoftLayer_Network_Storage volumes authorized to this device."""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getAttachedNetworkStorages', nasType, id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAvailableNetworkStorages(self, identifier: int, nasType: str) -> list['Network_Storage']:
        """Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device."""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getAvailableNetworkStorages', nasType, id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getByIpAddress(self, ipAddress: str) -> 'Network_Subnet_IpAddress':
        """Search for an IP address record."""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getByIpAddress', ipAddress)
        return data

    def getObject(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """Retrieve a SoftLayer_Network_Subnet_IpAddress record."""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getObject', id=identifier)
        return data

    def removeAccessToNetworkStorageList(self, identifier: int, networkStorageTemplateObjects: 'Network_Storage') -> bool:
        """Remove access to multiple SoftLayer_Network_Storage volumes from this device."""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'removeAccessToNetworkStorageList', networkStorageTemplateObjects, id=identifier)
        return data

    def getAllowedHost(self, identifier: int) -> 'Network_Storage_Allowed_Host':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getAllowedHost', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
        return data

    def getAllowedNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getAllowedNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAllowedNetworkStorageReplicas(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getAllowedNetworkStorageReplicas', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getApplicationDeliveryController(self, identifier: int) -> 'Network_Application_Delivery_Controller':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getApplicationDeliveryController', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller import Network_Application_Delivery_Controller
        return data

    def getContextTunnelTranslations(self, identifier: int) -> list['Network_Tunnel_Module_Context_Address_Translation']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getContextTunnelTranslations', id=identifier)
        from SoftLayer.sltypes.Network_Tunnel_Module_Context_Address_Translation import Network_Tunnel_Module_Context_Address_Translation
        return data

    def getEndpointSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getEndpointSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getGuestNetworkComponent(self, identifier: int) -> 'Virtual_Guest_Network_Component':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getGuestNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component import Virtual_Guest_Network_Component
        return data

    def getGuestNetworkComponentBinding(self, identifier: int) -> 'Virtual_Guest_Network_Component_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getGuestNetworkComponentBinding', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component_IpAddress import Virtual_Guest_Network_Component_IpAddress
        return data

    def getHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getNetworkComponent(self, identifier: int) -> 'Network_Component':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getPrivateNetworkGateway(self, identifier: int) -> 'Network_Gateway':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getPrivateNetworkGateway', id=identifier)
        from SoftLayer.sltypes.Network_Gateway import Network_Gateway
        return data

    def getProtectionAddress(self, identifier: int) -> list['Network_Protection_Address']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getProtectionAddress', id=identifier)
        from SoftLayer.sltypes.Network_Protection_Address import Network_Protection_Address
        return data

    def getPublicNetworkGateway(self, identifier: int) -> 'Network_Gateway':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getPublicNetworkGateway', id=identifier)
        from SoftLayer.sltypes.Network_Gateway import Network_Gateway
        return data

    def getRemoteManagementNetworkComponent(self, identifier: int) -> 'Network_Component':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getRemoteManagementNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getSubnet(self, identifier: int) -> 'Network_Subnet':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getSubnet', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getSyslogEventsOneDay(self, identifier: int) -> list['Network_Logging_Syslog']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getSyslogEventsOneDay', id=identifier)
        from SoftLayer.sltypes.Network_Logging_Syslog import Network_Logging_Syslog
        return data

    def getSyslogEventsSevenDays(self, identifier: int) -> list['Network_Logging_Syslog']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getSyslogEventsSevenDays', id=identifier)
        from SoftLayer.sltypes.Network_Logging_Syslog import Network_Logging_Syslog
        return data

    def getTopTenSyslogEventsByDestinationPortOneDay(self, identifier: int) -> list['Network_Logging_Syslog']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getTopTenSyslogEventsByDestinationPortOneDay', id=identifier)
        from SoftLayer.sltypes.Network_Logging_Syslog import Network_Logging_Syslog
        return data

    def getTopTenSyslogEventsByDestinationPortSevenDays(self, identifier: int) -> list['Network_Logging_Syslog']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getTopTenSyslogEventsByDestinationPortSevenDays', id=identifier)
        from SoftLayer.sltypes.Network_Logging_Syslog import Network_Logging_Syslog
        return data

    def getTopTenSyslogEventsByProtocolsOneDay(self, identifier: int) -> list['Network_Logging_Syslog']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getTopTenSyslogEventsByProtocolsOneDay', id=identifier)
        from SoftLayer.sltypes.Network_Logging_Syslog import Network_Logging_Syslog
        return data

    def getTopTenSyslogEventsByProtocolsSevenDays(self, identifier: int) -> list['Network_Logging_Syslog']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getTopTenSyslogEventsByProtocolsSevenDays', id=identifier)
        from SoftLayer.sltypes.Network_Logging_Syslog import Network_Logging_Syslog
        return data

    def getTopTenSyslogEventsBySourceIpOneDay(self, identifier: int) -> list['Network_Logging_Syslog']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getTopTenSyslogEventsBySourceIpOneDay', id=identifier)
        from SoftLayer.sltypes.Network_Logging_Syslog import Network_Logging_Syslog
        return data

    def getTopTenSyslogEventsBySourceIpSevenDays(self, identifier: int) -> list['Network_Logging_Syslog']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getTopTenSyslogEventsBySourceIpSevenDays', id=identifier)
        from SoftLayer.sltypes.Network_Logging_Syslog import Network_Logging_Syslog
        return data

    def getTopTenSyslogEventsBySourcePortOneDay(self, identifier: int) -> list['Network_Logging_Syslog']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getTopTenSyslogEventsBySourcePortOneDay', id=identifier)
        from SoftLayer.sltypes.Network_Logging_Syslog import Network_Logging_Syslog
        return data

    def getTopTenSyslogEventsBySourcePortSevenDays(self, identifier: int) -> list['Network_Logging_Syslog']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getTopTenSyslogEventsBySourcePortSevenDays', id=identifier)
        from SoftLayer.sltypes.Network_Logging_Syslog import Network_Logging_Syslog
        return data

    def getVirtualGuest(self, identifier: int) -> 'Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getVirtualGuest', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualLicenses(self, identifier: int) -> list['Software_VirtualLicense']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getVirtualLicenses', id=identifier)
        from SoftLayer.sltypes.Software_VirtualLicense import Software_VirtualLicense
        return data
