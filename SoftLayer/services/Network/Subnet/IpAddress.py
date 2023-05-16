# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Subnet_IpAddress(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Subnet_IpAddress'
        self.client = client

    def allowAccessToNetworkStorage(
        self,
        networkStorageTemplateObject: SoftLayer_Network_Storage
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToNetworkStorage',
            networkStorageTemplateObject
        )
        
        return data


    def allowAccessToNetworkStorageList(
        self,
        networkStorageTemplateObjects: SoftLayer_Network_Storage
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToNetworkStorageList',
            networkStorageTemplateObjects
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Network_Subnet_IpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def editObjects(
        self,
        templateObjects: SoftLayer_Network_Subnet_IpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObjects',
            templateObjects
        )
        
        return data


    def findByIpv4Address(
        self,
        ipAddress: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'findByIpv4Address',
            ipAddress,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getAttachedNetworkStorages(
        self,
        nasType: str,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAttachedNetworkStorages',
            nasType,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getAvailableNetworkStorages(
        self,
        nasType: str,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAvailableNetworkStorages',
            nasType,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getByIpAddress(
        self,
        ipAddress: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getByIpAddress',
            ipAddress,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def removeAccessToNetworkStorageList(
        self,
        networkStorageTemplateObjects: SoftLayer_Network_Storage
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToNetworkStorageList',
            networkStorageTemplateObjects
        )
        
        return data


    def getAllowedHost(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Allowed_Host':

        data = self.client.call(
            self.service,
            'getAllowedHost',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def getAllowedNetworkStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAllowedNetworkStorage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getAllowedNetworkStorageReplicas(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAllowedNetworkStorageReplicas',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getApplicationDeliveryController(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller':

        data = self.client.call(
            self.service,
            'getApplicationDeliveryController',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller import Controller
        return Controller(data)


    def getContextTunnelTranslations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Tunnel_Module_Context_Address_Translation]':

        data = self.client.call(
            self.service,
            'getContextTunnelTranslations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Tunnel.Module.Context.Address.Translation import Translation
        return Translation(data)


    def getEndpointSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getEndpointSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getGuestNetworkComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Network_Component':

        data = self.client.call(
            self.service,
            'getGuestNetworkComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return Component(data)


    def getGuestNetworkComponentBinding(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Network_Component_IpAddress':

        data = self.client.call(
            self.service,
            'getGuestNetworkComponentBinding',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component.IpAddress import IpAddress
        return IpAddress(data)


    def getHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getHardware',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getNetworkComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Component':

        data = self.client.call(
            self.service,
            'getNetworkComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component import Component
        return Component(data)


    def getPrivateNetworkGateway(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway':

        data = self.client.call(
            self.service,
            'getPrivateNetworkGateway',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway import Gateway
        return Gateway(data)


    def getProtectionAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Protection_Address]':

        data = self.client.call(
            self.service,
            'getProtectionAddress',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Protection.Address import Address
        return Address(data)


    def getPublicNetworkGateway(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway':

        data = self.client.call(
            self.service,
            'getPublicNetworkGateway',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway import Gateway
        return Gateway(data)


    def getRemoteManagementNetworkComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Component':

        data = self.client.call(
            self.service,
            'getRemoteManagementNetworkComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component import Component
        return Component(data)


    def getSubnet(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet':

        data = self.client.call(
            self.service,
            'getSubnet',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getSyslogEventsOneDay(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getSyslogEventsOneDay',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getSyslogEventsSevenDays(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getSyslogEventsSevenDays',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getTopTenSyslogEventsByDestinationPortOneDay(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getTopTenSyslogEventsByDestinationPortOneDay',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getTopTenSyslogEventsByDestinationPortSevenDays(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getTopTenSyslogEventsByDestinationPortSevenDays',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getTopTenSyslogEventsByProtocolsOneDay(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getTopTenSyslogEventsByProtocolsOneDay',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getTopTenSyslogEventsByProtocolsSevenDays(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getTopTenSyslogEventsByProtocolsSevenDays',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getTopTenSyslogEventsBySourceIpOneDay(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getTopTenSyslogEventsBySourceIpOneDay',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getTopTenSyslogEventsBySourceIpSevenDays(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getTopTenSyslogEventsBySourceIpSevenDays',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getTopTenSyslogEventsBySourcePortOneDay(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getTopTenSyslogEventsBySourcePortOneDay',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getTopTenSyslogEventsBySourcePortSevenDays(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Logging_Syslog]':

        data = self.client.call(
            self.service,
            'getTopTenSyslogEventsBySourcePortSevenDays',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Logging.Syslog import Syslog
        return Syslog(data)


    def getVirtualGuest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getVirtualGuest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualLicenses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_VirtualLicense]':

        data = self.client.call(
            self.service,
            'getVirtualLicenses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.VirtualLicense import VirtualLicense
        return VirtualLicense(data)


