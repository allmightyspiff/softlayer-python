# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Gateway_VersionUpgrade(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Gateway_VersionUpgrade'
        self.client = client

    def getAllByUpgradePkgUrlId(
        self,
        upgradePkgUrlId: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Gateway_VersionUpgrade]':

        data = self.client.call(
            self.service,
            'getAllByUpgradePkgUrlId',
            upgradePkgUrlId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Gateway.VersionUpgrade import VersionUpgrade
        return VersionUpgrade(data)


    def getAllUpgradesByGatewayId(
        self,
        gatewayId: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Gateway_VersionUpgrade]':

        data = self.client.call(
            self.service,
            'getAllUpgradesByGatewayId',
            gatewayId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Gateway.VersionUpgrade import VersionUpgrade
        return VersionUpgrade(data)


    def getGwOrdersAllowedLicenses(
        self,
        accountId: int,
        manufacturer: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getGwOrdersAllowedLicenses',
            accountId,
            manufacturer
        )
        
        return data


    def getGwOrdersAllowedOS(
        self,
        accountId: int,
        manufacturer: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Package_Item_Prices]':

        data = self.client.call(
            self.service,
            'getGwOrdersAllowedOS',
            accountId,
            manufacturer,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Package.Item.Prices import Prices
        return Prices(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway_VersionUpgrade':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway.VersionUpgrade import VersionUpgrade
        return VersionUpgrade(data)


    def getVsrxOrdersAllowedOS(
        self,
        accountId: int,
        validate: boolean,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Package_Item_Prices]':

        data = self.client.call(
            self.service,
            'getVsrxOrdersAllowedOS',
            accountId,
            validate,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Package.Item.Prices import Prices
        return Prices(data)


    def validateVersionChange(
        self,
        gatewayId: int,
        versionUpgradeId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'validateVersionChange',
            gatewayId,
            versionUpgradeId
        )
        
        return data


