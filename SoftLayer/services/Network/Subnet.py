# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Subnet(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Subnet'
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


    def clearRoute(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'clearRoute',
            
        )
        
        return data


    def createReverseDomainRecords(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Dns_Domain_Reverse':

        data = self.client.call(
            self.service,
            'createReverseDomainRecords',
            mask=objectMask
        )
        from SoftLayer.datatypes.Dns.Domain.Reverse import Reverse
        return Reverse(data)


    def createSubnetRouteUpdateTransaction(
        self,
        newEndPointIpAddress: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createSubnetRouteUpdateTransaction',
            newEndPointIpAddress
        )
        
        return data


    def createSwipTransaction(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createSwipTransaction',
            
        )
        
        return data


    def editNote(
        self,
        note: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editNote',
            note
        )
        
        return data


    def findAllSubnetsAndActiveSwipTransactionStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'findAllSubnetsAndActiveSwipTransactionStatus',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


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


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


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
        return Domain(data)


    def getRoutableEndpointIpAddresses(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getRoutableEndpointIpAddresses',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getSubnetForIpAddress(
        self,
        ipAddress: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Subnet':

        data = self.client.call(
            self.service,
            'getSubnetForIpAddress',
            ipAddress,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


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


    def route(
        self,
        type: str,
        identifier: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'route',
            type,
            identifier
        )
        
        return data


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
        return Account(data)


    def getActiveRegistration(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_Registration':

        data = self.client.call(
            self.service,
            'getActiveRegistration',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.Registration import Registration
        return Registration(data)


    def getActiveSwipTransaction(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_Swip_Transaction':

        data = self.client.call(
            self.service,
            'getActiveSwipTransaction',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.Swip.Transaction import Transaction
        return Transaction(data)


    def getActiveTransaction(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'getActiveTransaction',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getAddressSpace(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAddressSpace',
            mask=objectMask,
            filter=objectFilter
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


    def getBoundDescendants(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getBoundDescendants',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getBoundRouterFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getBoundRouterFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBoundRouters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getBoundRouters',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getChildren(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getChildren',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getDatacenter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Datacenter':

        data = self.client.call(
            self.service,
            'getDatacenter',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Datacenter import Datacenter
        return Datacenter(data)


    def getDescendants(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getDescendants',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getDisplayLabel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDisplayLabel',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getEndPointIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getEndPointIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getGlobalIpRecord(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress_Global':

        data = self.client.call(
            self.service,
            'getGlobalIpRecord',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress.Global import Global
        return Global(data)


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
        return Hardware(data)


    def getIpAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getIpAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getNetworkComponentFirewall(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Component_Firewall':

        data = self.client.call(
            self.service,
            'getNetworkComponentFirewall',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component.Firewall import Firewall
        return Firewall(data)


    def getNetworkProtectionAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Protection_Address]':

        data = self.client.call(
            self.service,
            'getNetworkProtectionAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Protection.Address import Address
        return Address(data)


    def getNetworkTunnelContexts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Tunnel_Module_Context]':

        data = self.client.call(
            self.service,
            'getNetworkTunnelContexts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Tunnel.Module.Context import Context
        return Context(data)


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
        return IpAddress(data)


    def getRegionalInternetRegistry(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Regional_Internet_Registry':

        data = self.client.call(
            self.service,
            'getRegionalInternetRegistry',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Regional.Internet.Registry import Registry
        return Registry(data)


    def getRegistrations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_Registration]':

        data = self.client.call(
            self.service,
            'getRegistrations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.Registration import Registration
        return Registration(data)


    def getReverseDomain(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain':

        data = self.client.call(
            self.service,
            'getReverseDomain',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return Domain(data)


    def getRoleKeyName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getRoleKeyName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getRoleName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getRoleName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getRoutingTypeKeyName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getRoutingTypeKeyName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getRoutingTypeName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getRoutingTypeName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSwipTransaction(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_Swip_Transaction]':

        data = self.client.call(
            self.service,
            'getSwipTransaction',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.Swip.Transaction import Transaction
        return Transaction(data)


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


    def getUnboundDescendants(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getUnboundDescendants',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getUtilizedIpAddressCount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getUtilizedIpAddressCount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


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
        return Guest(data)


