from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Gateway_VersionUpgrade(Entity):
    fromVersion: str
    id_: int
    osReloadRequired: int
    toVersion: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Gateway_VersionUpgrade'

    def getAllByUpgradePkgUrlId(self, upgradePkgUrlId: int) -> list['Network_Gateway_VersionUpgrade']:
        data = self.client.call('SoftLayer_Network_Gateway_VersionUpgrade', 'getAllByUpgradePkgUrlId', upgradePkgUrlId)
        return data

    def getAllUpgradesByGatewayId(self, gatewayId: int) -> list['Network_Gateway_VersionUpgrade']:
        data = self.client.call('SoftLayer_Network_Gateway_VersionUpgrade', 'getAllUpgradesByGatewayId', gatewayId)
        return data

    def getGwOrdersAllowedLicenses(self, accountId: int, manufacturer: str) -> str:
        data = self.client.call('SoftLayer_Network_Gateway_VersionUpgrade', 'getGwOrdersAllowedLicenses', accountId, manufacturer)
        return data

    def getGwOrdersAllowedOS(self, accountId: int, manufacturer: str) -> list['Product_Package_Item_Prices']:
        data = self.client.call('SoftLayer_Network_Gateway_VersionUpgrade', 'getGwOrdersAllowedOS', accountId, manufacturer)
        from SoftLayer.sltypes.Product_Package_Item_Prices import Product_Package_Item_Prices
        return data

    def getObject(self, identifier: int) -> 'Network_Gateway_VersionUpgrade':
        """Retrieve a SoftLayer_Network_Gateway_VersionUpgrade record."""
        data = self.client.call('SoftLayer_Network_Gateway_VersionUpgrade', 'getObject', id=identifier)
        return data

    def getVsrxOrdersAllowedOS(self, accountId: int, validate: bool) -> list['Product_Package_Item_Prices']:
        data = self.client.call('SoftLayer_Network_Gateway_VersionUpgrade', 'getVsrxOrdersAllowedOS', accountId, validate)
        from SoftLayer.sltypes.Product_Package_Item_Prices import Product_Package_Item_Prices
        return data

    def validateVersionChange(self, identifier: int, gatewayId: int, versionUpgradeId: int) -> bool:
        data = self.client.call('SoftLayer_Network_Gateway_VersionUpgrade', 'validateVersionChange', gatewayId, versionUpgradeId, id=identifier)
        return data
