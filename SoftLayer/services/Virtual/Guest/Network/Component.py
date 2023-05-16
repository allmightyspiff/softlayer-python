# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_Guest_Network_Component(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_Guest_Network_Component'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def disable(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'disable',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def enable(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'enable',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Network_Component':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component import Component
        return SL_Component(data)

# This file was automatically generated with tools/generateTypes.py
    def isPingable(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isPingable',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def securityGroupsReady(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'securityGroupsReady',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getGuest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':
        data = self.client.call(
            self.service,
            'getGuest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return SL_Guest(data)

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
    def getIcpBinding(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Network_Component_IcpBinding':
        data = self.client.call(
            self.service,
            'getIcpBinding',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component.IcpBinding import IcpBinding
        return SL_IcpBinding(data)

# This file was automatically generated with tools/generateTypes.py
    def getIpAddressBindings(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Network_Component_IpAddress]':
        data = self.client.call(
            self.service,
            'getIpAddressBindings',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Network.Component.IpAddress import IpAddress
        return SL_IpAddress(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Firewall(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrimaryIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPrimaryIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPrimaryIpAddressRecord(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':
        data = self.client.call(
            self.service,
            'getPrimaryIpAddressRecord',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return SL_IpAddress(data)

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
    def getPrimaryVersion6IpAddressRecord(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':
        data = self.client.call(
            self.service,
            'getPrimaryVersion6IpAddressRecord',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return SL_IpAddress(data)

# This file was automatically generated with tools/generateTypes.py
    def getRouter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Router':
        data = self.client.call(
            self.service,
            'getRouter',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Router import Router
        return SL_Router(data)

# This file was automatically generated with tools/generateTypes.py
    def getSecurityGroupBindings(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding]':
        data = self.client.call(
            self.service,
            'getSecurityGroupBindings',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Network.SecurityGroup.NetworkComponentBinding import NetworkComponentBinding
        return SL_NetworkComponentBinding(data)

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


