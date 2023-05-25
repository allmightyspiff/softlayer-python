from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress(Entity):
    accountId: int
    connectionLimit: int
    connectionLimitUnits: str
    dedicatedFlag: bool
    id_: int
    ipAddressId: int
    notes: str
    securityCertificateId: int
    sslActiveFlag: bool
    sslEnabledFlag: bool

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'

    def editObject(self, identifier: int, templateObject: 'Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress') -> bool:
        """Edit the object by passing in a modified instance of the object"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'editObject', templateObject, id=identifier)
        return data

    def getAvailableSecureTransportCiphers(self, identifier: int) -> list['Security_SecureTransportCipher']:
        """Lists the SSL encryption ciphers available to this virtual IP address"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getAvailableSecureTransportCiphers', id=identifier)
        from SoftLayer.sltypes.Security_SecureTransportCipher import Security_SecureTransportCipher
        return data

    def getAvailableSecureTransportProtocols(self, identifier: int) -> list['Security_SecureTransportProtocol']:
        """Lists the secure communication protocols available to this virtual IP address"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getAvailableSecureTransportProtocols', id=identifier)
        from SoftLayer.sltypes.Security_SecureTransportProtocol import Security_SecureTransportProtocol
        return data

    def getObject(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress':
        """Retrieve a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress record."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getObject', id=identifier)
        return data

    def startSsl(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'startSsl', id=identifier)
        return data

    def stopSsl(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'stopSsl', id=identifier)
        return data

    def upgradeConnectionLimit(self, identifier: int) -> bool:
        """Upgrades the connection limit on the Virtual IP Address and changes the billing item on your account to
reflect the change."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'upgradeConnectionLimit', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getApplicationDeliveryController(self, identifier: int) -> 'Network_Application_Delivery_Controller':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getApplicationDeliveryController', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller import Network_Application_Delivery_Controller
        return data

    def getApplicationDeliveryControllers(self, identifier: int) -> list['Network_Application_Delivery_Controller']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getApplicationDeliveryControllers', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller import Network_Application_Delivery_Controller
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getDedicatedBillingItem(self, identifier: int) -> 'Billing_Item_Network_LoadBalancer':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getDedicatedBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Network_LoadBalancer import Billing_Item_Network_LoadBalancer
        return data

    def getHighAvailabilityFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getHighAvailabilityFlag', id=identifier)
        return data

    def getIpAddress(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getIpAddress', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getLoadBalancerHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getLoadBalancerHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getManagedResourceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getManagedResourceFlag', id=identifier)
        return data

    def getSecureTransportCiphers(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportCipher']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getSecureTransportCiphers', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportCipher import Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportCipher
        return data

    def getSecureTransportProtocols(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportProtocol']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getSecureTransportProtocols', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportProtocol import Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportProtocol
        return data

    def getSecurityCertificate(self, identifier: int) -> 'Security_Certificate':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getSecurityCertificate', id=identifier)
        from SoftLayer.sltypes.Security_Certificate import Security_Certificate
        return data

    def getSecurityCertificateEntry(self, identifier: int) -> 'Security_Certificate_Entry':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getSecurityCertificateEntry', id=identifier)
        from SoftLayer.sltypes.Security_Certificate_Entry import Security_Certificate_Entry
        return data

    def getVirtualServers(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_VirtualServer']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', 'getVirtualServers', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_VirtualServer import Network_Application_Delivery_Controller_LoadBalancer_VirtualServer
        return data
