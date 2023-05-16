# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAvailableSecureTransportCiphers(
        self,
        
    ) -> 'list[SoftLayer_Security_SecureTransportCipher]':
        data = self.client.call(
            self.service,
            'getAvailableSecureTransportCiphers',
            
        )
        from SoftLayer.datatypes.Security.SecureTransportCipher import SecureTransportCipher
        return SL_SecureTransportCipher(data)

# This file was automatically generated with tools/generateTypes.py
    def getAvailableSecureTransportProtocols(
        self,
        
    ) -> 'list[SoftLayer_Security_SecureTransportProtocol]':
        data = self.client.call(
            self.service,
            'getAvailableSecureTransportProtocols',
            
        )
        from SoftLayer.datatypes.Security.SecureTransportProtocol import SecureTransportProtocol
        return SL_SecureTransportProtocol(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return SL_VirtualIpAddress(data)

# This file was automatically generated with tools/generateTypes.py
    def startSsl(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'startSsl',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def stopSsl(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'stopSsl',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def upgradeConnectionLimit(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'upgradeConnectionLimit',
            
        )
        
        return data

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
        return SL_Controller(data)

# This file was automatically generated with tools/generateTypes.py
    def getApplicationDeliveryControllers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller]':
        data = self.client.call(
            self.service,
            'getApplicationDeliveryControllers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller import Controller
        return SL_Controller(data)

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
    def getDedicatedBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Network_LoadBalancer':
        data = self.client.call(
            self.service,
            'getDedicatedBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Network.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def getHighAvailabilityFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getHighAvailabilityFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':
        data = self.client.call(
            self.service,
            'getIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return SL_IpAddress(data)

# This file was automatically generated with tools/generateTypes.py
    def getLoadBalancerHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getLoadBalancerHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getManagedResourceFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getManagedResourceFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getSecureTransportCiphers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportCipher]':
        data = self.client.call(
            self.service,
            'getSecureTransportCiphers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualIpAddress.SecureTransportCipher import SecureTransportCipher
        return SL_SecureTransportCipher(data)

# This file was automatically generated with tools/generateTypes.py
    def getSecureTransportProtocols(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportProtocol]':
        data = self.client.call(
            self.service,
            'getSecureTransportProtocols',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualIpAddress.SecureTransportProtocol import SecureTransportProtocol
        return SL_SecureTransportProtocol(data)

# This file was automatically generated with tools/generateTypes.py
    def getSecurityCertificate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Security_Certificate':
        data = self.client.call(
            self.service,
            'getSecurityCertificate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Security.Certificate import Certificate
        return SL_Certificate(data)

# This file was automatically generated with tools/generateTypes.py
    def getSecurityCertificateEntry(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Security_Certificate_Entry':
        data = self.client.call(
            self.service,
            'getSecurityCertificateEntry',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Security.Certificate.Entry import Entry
        return SL_Entry(data)

# This file was automatically generated with tools/generateTypes.py
    def getVirtualServers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer]':
        data = self.client.call(
            self.service,
            'getVirtualServers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualServer import VirtualServer
        return SL_VirtualServer(data)


