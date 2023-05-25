from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Gateway(Entity):
    accountId: int
    groupNumber: int
    id_: int
    name: str
    networkSpace: str
    osManufacturer: str
    privateIpAddressId: int
    privateVlanId: int
    publicIpAddressId: int
    publicIpv6AddressId: int
    publicVlanId: int
    statusId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Gateway'

    def bypassAllVlans(self, identifier: int) -> None:
        """Bypass All VLANs"""
        data = self.client.call('SoftLayer_Network_Gateway', 'bypassAllVlans', id=identifier)
        return data

    def bypassVlans(self, identifier: int, vlans: 'Network_Gateway_Vlan') -> None:
        """Bypass VLANs"""
        data = self.client.call('SoftLayer_Network_Gateway', 'bypassVlans', vlans, id=identifier)
        return data

    def changeGatewayVersion(self, identifier: int, versionId: int, rollbackVersion: bool) -> bool:
        """Change Juniper vSRX version on a Gateway"""
        data = self.client.call('SoftLayer_Network_Gateway', 'changeGatewayVersion', versionId, rollbackVersion, id=identifier)
        return data

    def checkAccountWhiteList(self, accountId: int, category: str) -> bool:
        data = self.client.call('SoftLayer_Network_Gateway', 'checkAccountWhiteList', accountId, category)
        return data

    def createObject(self, templateObject: 'Network_Gateway') -> 'Network_Gateway':
        """Create a new server gateway"""
        data = self.client.call('SoftLayer_Network_Gateway', 'createObject', templateObject)
        from SoftLayer.sltypes.Network_Gateway import Network_Gateway
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Gateway') -> bool:
        """Edit Gateway"""
        data = self.client.call('SoftLayer_Network_Gateway', 'editObject', templateObject, id=identifier)
        return data

    def forceRebuildCluster(self, identifier: int, osPriceId: int) -> bool:
        """Rebuild HA GAteway"""
        data = self.client.call('SoftLayer_Network_Gateway', 'forceRebuildCluster', osPriceId, id=identifier)
        return data

    def forceRebuildvSRXCluster(self, identifier: int, osPriceId: int) -> bool:
        """Rebuild HA GAteway"""
        data = self.client.call('SoftLayer_Network_Gateway', 'forceRebuildvSRXCluster', osPriceId, id=identifier)
        return data

    def getAllowedOsPriceIds(self, identifier: int, memberId: int) -> list[int]:
        data = self.client.call('SoftLayer_Network_Gateway', 'getAllowedOsPriceIds', memberId, id=identifier)
        return data

    def getCapacity(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Network_Gateway', 'getCapacity', id=identifier)
        return data

    def getManufacturer(self, identifier: int, checkSameOs: bool, checkOsReloadMember: bool) -> str:
        """manufacturer name"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getManufacturer', checkSameOs, checkOsReloadMember, id=identifier)
        return data

    def getMemberGatewayImagesMatch(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Gateway', 'getMemberGatewayImagesMatch', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Gateway':
        """Retrieve a SoftLayer_Network_Gateway record."""
        data = self.client.call('SoftLayer_Network_Gateway', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Gateway import Network_Gateway
        return data

    def getPossibleInsideVlans(self, identifier: int) -> list['Network_Vlan']:
        """Get Possible Inside VLANs"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getPossibleInsideVlans', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getRollbackSupport(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Network_Gateway', 'getRollbackSupport', id=identifier)
        return data

    def getUpgradeItemPrices(self, identifier: int) -> list['Product_Item_Price']:
        """Retrieve available upgrade prices"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getUpgradeItemPrices', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def isAccountWhiteListed(self, identifier: int, category: str) -> bool:
        data = self.client.call('SoftLayer_Network_Gateway', 'isAccountWhiteListed', category, id=identifier)
        return data

    def isLicenseServerAllowed(self, identifier: int, licenseKeyName: str) -> bool:
        data = self.client.call('SoftLayer_Network_Gateway', 'isLicenseServerAllowed', licenseKeyName, id=identifier)
        return data

    def isRollbackAllowed(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Gateway', 'isRollbackAllowed', id=identifier)
        return data

    def rebuildHACluster(self, identifier: int) -> bool:
        """Rebuild HA Gateway"""
        data = self.client.call('SoftLayer_Network_Gateway', 'rebuildHACluster', id=identifier)
        return data

    def rebuildvSRXHACluster(self, identifier: int) -> bool:
        """Rebuild Juniper vSRX HA Gateway"""
        data = self.client.call('SoftLayer_Network_Gateway', 'rebuildvSRXHACluster', id=identifier)
        return data

    def refreshGatewayLicense(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Gateway', 'refreshGatewayLicense', id=identifier)
        return data

    def setGatewayPassword(self, identifier: int, password: str) -> bool:
        data = self.client.call('SoftLayer_Network_Gateway', 'setGatewayPassword', password, id=identifier)
        return data

    def unbypassAllVlans(self, identifier: int) -> None:
        """Bypass All VLANs"""
        data = self.client.call('SoftLayer_Network_Gateway', 'unbypassAllVlans', id=identifier)
        return data

    def unbypassVlans(self, identifier: int, vlans: 'Network_Gateway_Vlan') -> None:
        """Bypass VLANs"""
        data = self.client.call('SoftLayer_Network_Gateway', 'unbypassVlans', vlans, id=identifier)
        return data

    def updateGatewayUserPassword(self, identifier: int, record: 'Network_Gateway_Member_Passwords') -> bool:
        data = self.client.call('SoftLayer_Network_Gateway', 'updateGatewayUserPassword', record, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getInsideVlans(self, identifier: int) -> list['Network_Gateway_Vlan']:
        """"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getInsideVlans', id=identifier)
        from SoftLayer.sltypes.Network_Gateway_Vlan import Network_Gateway_Vlan
        return data

    def getMembers(self, identifier: int) -> list['Network_Gateway_Member']:
        """"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getMembers', id=identifier)
        from SoftLayer.sltypes.Network_Gateway_Member import Network_Gateway_Member
        return data

    def getNetworkFirewall(self, identifier: int) -> 'Network_Vlan_Firewall':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getNetworkFirewall', id=identifier)
        from SoftLayer.sltypes.Network_Vlan_Firewall import Network_Vlan_Firewall
        return data

    def getNetworkFirewallFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getNetworkFirewallFlag', id=identifier)
        return data

    def getPrivateIpAddress(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getPrivateIpAddress', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getPrivateVlan(self, identifier: int) -> 'Network_Vlan':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getPrivateVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getPublicIpAddress(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getPublicIpAddress', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getPublicIpv6Address(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getPublicIpv6Address', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getPublicVlan(self, identifier: int) -> 'Network_Vlan':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getPublicVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getStatus(self, identifier: int) -> 'Network_Gateway_Status':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Network_Gateway_Status import Network_Gateway_Status
        return data
