from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Tunnel_Module_Context(Entity):
    """The SoftLayer_Network_Tunnel_Module_Context data type contains general information relating to a single
SoftLayer network tunnel.  The SoftLayer_Network_Tunnel_Module_Context is useful to gather information such
as related customer subnets (remote) and internal subnets (local) associated with the network tunnel as well
as other information needed to manage the network tunnel.  Account and billing information related to the
network tunnel can also be retrieved."""
    accountId: int
    advancedConfigurationFlag: int
    createDate: datetime
    customerPeerIpAddress: str
    friendlyName: str
    id_: int
    internalPeerIpAddress: str
    modifyDate: datetime
    name: str
    phaseOneAuthentication: str
    phaseOneDiffieHellmanGroup: int
    phaseOneEncryption: str
    phaseOneKeylife: int
    phaseTwoAuthentication: str
    phaseTwoDiffieHellmanGroup: int
    phaseTwoEncryption: str
    phaseTwoKeylife: int
    phaseTwoPerfectForwardSecrecy: int
    presharedKey: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Tunnel_Module_Context'

    def addCustomerSubnetToNetworkTunnel(self, identifier: int, subnetId: int) -> bool:
        """Associate a remote subnet to a network tunnel"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'addCustomerSubnetToNetworkTunnel', subnetId, id=identifier)
        return data

    def addPrivateSubnetToNetworkTunnel(self, identifier: int, subnetId: int) -> bool:
        """Associate a private subnet to a network tunnel."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'addPrivateSubnetToNetworkTunnel', subnetId, id=identifier)
        return data

    def addServiceSubnetToNetworkTunnel(self, identifier: int, subnetId: int) -> bool:
        """Associate a service subnet to a network tunnel."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'addServiceSubnetToNetworkTunnel', subnetId, id=identifier)
        return data

    def applyConfigurationsToDevice(self, identifier: int) -> bool:
        """Apply current configuration settings to the network device"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'applyConfigurationsToDevice', id=identifier)
        return data

    def createAddressTranslation(self, identifier: int, translation: 'Network_Tunnel_Module_Context_Address_Translation') -> 'Network_Tunnel_Module_Context_Address_Translation':
        """Create an address translation for a network tunnel"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'createAddressTranslation', translation, id=identifier)
        from SoftLayer.sltypes.Network_Tunnel_Module_Context_Address_Translation import Network_Tunnel_Module_Context_Address_Translation
        return data

    def createAddressTranslations(self, identifier: int, translations: 'Network_Tunnel_Module_Context_Address_Translation') -> list['Network_Tunnel_Module_Context_Address_Translation']:
        """Create address translations for a network tunnel"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'createAddressTranslations', translations, id=identifier)
        from SoftLayer.sltypes.Network_Tunnel_Module_Context_Address_Translation import Network_Tunnel_Module_Context_Address_Translation
        return data

    def deleteAddressTranslation(self, identifier: int, translationId: int) -> bool:
        """Delete an address translation from a network tunnel"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'deleteAddressTranslation', translationId, id=identifier)
        return data

    def downloadAddressTranslationConfigurations(self, identifier: int) -> 'Container_Utility_File_Entity':
        """Returns IPSec VPN tunnel address translation configurations in a text file."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'downloadAddressTranslationConfigurations', id=identifier)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def downloadParameterConfigurations(self, identifier: int) -> 'Container_Utility_File_Entity':
        """Returns IPSec VPN tunnel configurations in a text file."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'downloadParameterConfigurations', id=identifier)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def editAddressTranslation(self, identifier: int, translation: 'Network_Tunnel_Module_Context_Address_Translation') -> 'Network_Tunnel_Module_Context_Address_Translation':
        """Edit an address translation for a network tunnel"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'editAddressTranslation', translation, id=identifier)
        from SoftLayer.sltypes.Network_Tunnel_Module_Context_Address_Translation import Network_Tunnel_Module_Context_Address_Translation
        return data

    def editAddressTranslations(self, identifier: int, translations: 'Network_Tunnel_Module_Context_Address_Translation') -> list['Network_Tunnel_Module_Context_Address_Translation']:
        """Edit address translations for a network tunnel"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'editAddressTranslations', translations, id=identifier)
        from SoftLayer.sltypes.Network_Tunnel_Module_Context_Address_Translation import Network_Tunnel_Module_Context_Address_Translation
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Tunnel_Module_Context') -> bool:
        """Edit various settings for a network tunnel."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'editObject', templateObject, id=identifier)
        return data

    def getAddressTranslationConfigurations(self, identifier: int) -> str:
        """Build and returns IPsec VPN  tunnel address translation configurations"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getAddressTranslationConfigurations', id=identifier)
        return data

    def getAuthenticationDefault(self) -> str:
        """Returns the authentication default."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getAuthenticationDefault')
        return data

    def getAuthenticationOptions(self) -> list[str]:
        """Returns the authentication options."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getAuthenticationOptions')
        return data

    def getDiffieHellmanGroupDefault(self) -> int:
        """Returns the diffie hellman group default."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getDiffieHellmanGroupDefault')
        return data

    def getDiffieHellmanGroupOptions(self) -> list[int]:
        """Returns the diffie-hellman group options."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getDiffieHellmanGroupOptions')
        return data

    def getEncryptionDefault(self) -> str:
        """Returns the encryption default."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getEncryptionDefault')
        return data

    def getEncryptionOptions(self) -> list[str]:
        """Returns the encryption options."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getEncryptionOptions')
        return data

    def getKeylifeLimits(self) -> list[int]:
        """Returns the keylife min and max limits."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getKeylifeLimits')
        return data

    def getObject(self, identifier: int) -> 'Network_Tunnel_Module_Context':
        """Retrieve a SoftLayer_Network_Tunnel_Module_Context record."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getObject', id=identifier)
        return data

    def getParameterConfigurationsForCustomerView(self, identifier: int) -> str:
        """Build and returns IPsec VPN tunnel configurations"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getParameterConfigurationsForCustomerView', id=identifier)
        return data

    def getPhaseOneKeylifeDefault(self) -> str:
        """Returns the phase one keylife default."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getPhaseOneKeylifeDefault')
        return data

    def getPhaseTwoKeylifeDefault(self) -> str:
        """Returns phase two keylife default."""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getPhaseTwoKeylifeDefault')
        return data

    def removeCustomerSubnetFromNetworkTunnel(self, identifier: int, subnetId: int) -> bool:
        """Disassociate a customer (remote) subnet from a network tunnel"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'removeCustomerSubnetFromNetworkTunnel', subnetId, id=identifier)
        return data

    def removePrivateSubnetFromNetworkTunnel(self, identifier: int, subnetId: int) -> bool:
        """Disassociate a private subnet from a network tunnel"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'removePrivateSubnetFromNetworkTunnel', subnetId, id=identifier)
        return data

    def removeServiceSubnetFromNetworkTunnel(self, identifier: int, subnetId: int) -> bool:
        """Disassociate service subnet from a network tunnel"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'removeServiceSubnetFromNetworkTunnel', subnetId, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getActiveTransaction(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getActiveTransaction', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getAddressTranslations(self, identifier: int) -> list['Network_Tunnel_Module_Context_Address_Translation']:
        """"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getAddressTranslations', id=identifier)
        from SoftLayer.sltypes.Network_Tunnel_Module_Context_Address_Translation import Network_Tunnel_Module_Context_Address_Translation
        return data

    def getAllAvailableServiceSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getAllAvailableServiceSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getCustomerSubnets(self, identifier: int) -> list['Network_Customer_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getCustomerSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Customer_Subnet import Network_Customer_Subnet
        return data

    def getDatacenter(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getInternalSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getInternalSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getServiceSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getServiceSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getStaticRouteSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getStaticRouteSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getTransactionHistory(self, identifier: int) -> list['Provisioning_Version1_Transaction']:
        """"""
        data = self.client.call('SoftLayer_Network_Tunnel_Module_Context', 'getTransactionHistory', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data
