# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Gateway(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Gateway'
        self.client = client

    def bypassAllVlans(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'bypassAllVlans',
            id=identifier
        )
        
        return data


    def bypassVlans(
        self,
        vlans: 'SoftLayer_Network_Gateway_Vlan',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'bypassVlans',
            vlans,
            id=identifier
        )
        
        return data


    def changeGatewayVersion(
        self,
        versionId: int,
        rollbackVersion: bool,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'changeGatewayVersion',
            versionId,
            rollbackVersion,
            id=identifier
        )
        
        return data


    def checkAccountWhiteList(
        self,
        accountId: int,
        category: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'checkAccountWhiteList',
            accountId,
            category
        )
        
        return data


    def createObject(
        self,
        templateObject: 'SoftLayer_Network_Gateway',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Gateway':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Gateway import Gateway
        return Gateway(data)


    def editObject(
        self,
        templateObject: 'SoftLayer_Network_Gateway',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def forceRebuildCluster(
        self,
        osPriceId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'forceRebuildCluster',
            osPriceId,
            id=identifier
        )
        
        return data


    def forceRebuildvSRXCluster(
        self,
        osPriceId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'forceRebuildvSRXCluster',
            osPriceId,
            id=identifier
        )
        
        return data


    def getAllowedOsPriceIds(
        self,
        memberId: int,
        identifier: int
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getAllowedOsPriceIds',
            memberId,
            id=identifier
        )
        
        return data


    def getCapacity(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getCapacity',
            id=identifier
        )
        
        return data


    def getManufacturer(
        self,
        checkSameOs: bool,
        checkOsReloadMember: bool,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getManufacturer',
            checkSameOs,
            checkOsReloadMember,
            id=identifier
        )
        
        return data


    def getMemberGatewayImagesMatch(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getMemberGatewayImagesMatch',
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway import Gateway
        return Gateway(data)


    def getPossibleInsideVlans(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Vlan]':

        data = self.client.call(
            self.service,
            'getPossibleInsideVlans',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getRollbackSupport(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getRollbackSupport',
            id=identifier
        )
        
        return data


    def getUpgradeItemPrices(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getUpgradeItemPrices',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def isAccountWhiteListed(
        self,
        category: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isAccountWhiteListed',
            category,
            id=identifier
        )
        
        return data


    def isLicenseServerAllowed(
        self,
        licenseKeyName: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isLicenseServerAllowed',
            licenseKeyName,
            id=identifier
        )
        
        return data


    def isRollbackAllowed(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isRollbackAllowed',
            id=identifier
        )
        
        return data


    def rebuildHACluster(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'rebuildHACluster',
            id=identifier
        )
        
        return data


    def rebuildvSRXHACluster(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'rebuildvSRXHACluster',
            id=identifier
        )
        
        return data


    def refreshGatewayLicense(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'refreshGatewayLicense',
            id=identifier
        )
        
        return data


    def setGatewayPassword(
        self,
        password: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setGatewayPassword',
            password,
            id=identifier
        )
        
        return data


    def unbypassAllVlans(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'unbypassAllVlans',
            id=identifier
        )
        
        return data


    def unbypassVlans(
        self,
        vlans: 'SoftLayer_Network_Gateway_Vlan',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'unbypassVlans',
            vlans,
            id=identifier
        )
        
        return data


    def updateGatewayUserPassword(
        self,
        record: 'SoftLayer_Network_Gateway_Member_Passwords',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateGatewayUserPassword',
            record,
            id=identifier
        )
        
        return data


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getInsideVlans(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Gateway_Vlan]':

        data = self.client.call(
            self.service,
            'getInsideVlans',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Gateway.Vlan import Vlan
        return Vlan(data)


    def getMembers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Gateway_Member]':

        data = self.client.call(
            self.service,
            'getMembers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Gateway.Member import Member
        return Member(data)


    def getNetworkFirewall(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan_Firewall':

        data = self.client.call(
            self.service,
            'getNetworkFirewall',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan.Firewall import Firewall
        return Firewall(data)


    def getNetworkFirewallFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getNetworkFirewallFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPrivateIpAddress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getPrivateIpAddress',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getPrivateVlan(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan':

        data = self.client.call(
            self.service,
            'getPrivateVlan',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getPublicIpAddress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getPublicIpAddress',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getPublicIpv6Address(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getPublicIpv6Address',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getPublicVlan(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan':

        data = self.client.call(
            self.service,
            'getPublicVlan',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway.Status import Status
        return Status(data)


