# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Gateway(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Gateway'
        self.client = client

    def bypassAllVlans(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'bypassAllVlans',
            
        )
        
        return data


    def bypassVlans(
        self,
        vlans: SoftLayer_Network_Gateway_Vlan
    ) -> 'void':

        data = self.client.call(
            self.service,
            'bypassVlans',
            vlans
        )
        
        return data


    def changeGatewayVersion(
        self,
        versionId: int,
        rollbackVersion: boolean
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'changeGatewayVersion',
            versionId,
            rollbackVersion
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
        templateObject: SoftLayer_Network_Gateway,
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
        templateObject: SoftLayer_Network_Gateway
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def forceRebuildCluster(
        self,
        osPriceId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'forceRebuildCluster',
            osPriceId
        )
        
        return data


    def forceRebuildvSRXCluster(
        self,
        osPriceId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'forceRebuildvSRXCluster',
            osPriceId
        )
        
        return data


    def getAllowedOsPriceIds(
        self,
        memberId: int
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getAllowedOsPriceIds',
            memberId
        )
        
        return data


    def getCapacity(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getCapacity',
            
        )
        
        return data


    def getManufacturer(
        self,
        checkSameOs: boolean,
        checkOsReloadMember: boolean
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getManufacturer',
            checkSameOs,
            checkOsReloadMember
        )
        
        return data


    def getMemberGatewayImagesMatch(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getMemberGatewayImagesMatch',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway import Gateway
        return Gateway(data)


    def getPossibleInsideVlans(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Vlan]':

        data = self.client.call(
            self.service,
            'getPossibleInsideVlans',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getRollbackSupport(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getRollbackSupport',
            
        )
        
        return data


    def getUpgradeItemPrices(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getUpgradeItemPrices',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def isAccountWhiteListed(
        self,
        category: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isAccountWhiteListed',
            category
        )
        
        return data


    def isLicenseServerAllowed(
        self,
        licenseKeyName: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isLicenseServerAllowed',
            licenseKeyName
        )
        
        return data


    def isRollbackAllowed(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isRollbackAllowed',
            
        )
        
        return data


    def rebuildHACluster(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'rebuildHACluster',
            
        )
        
        return data


    def rebuildvSRXHACluster(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'rebuildvSRXHACluster',
            
        )
        
        return data


    def refreshGatewayLicense(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'refreshGatewayLicense',
            
        )
        
        return data


    def setGatewayPassword(
        self,
        password: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setGatewayPassword',
            password
        )
        
        return data


    def unbypassAllVlans(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'unbypassAllVlans',
            
        )
        
        return data


    def unbypassVlans(
        self,
        vlans: SoftLayer_Network_Gateway_Vlan
    ) -> 'void':

        data = self.client.call(
            self.service,
            'unbypassVlans',
            vlans
        )
        
        return data


    def updateGatewayUserPassword(
        self,
        record: SoftLayer_Network_Gateway_Member_Passwords
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateGatewayUserPassword',
            record
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


    def getInsideVlans(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Gateway_Vlan]':

        data = self.client.call(
            self.service,
            'getInsideVlans',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Gateway.Vlan import Vlan
        return Vlan(data)


    def getMembers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Gateway_Member]':

        data = self.client.call(
            self.service,
            'getMembers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Gateway.Member import Member
        return Member(data)


    def getNetworkFirewall(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan_Firewall':

        data = self.client.call(
            self.service,
            'getNetworkFirewall',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan.Firewall import Firewall
        return Firewall(data)


    def getNetworkFirewallFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getNetworkFirewallFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPrivateIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getPrivateIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getPrivateVlan(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan':

        data = self.client.call(
            self.service,
            'getPrivateVlan',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getPublicIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getPublicIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getPublicIpv6Address(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getPublicIpv6Address',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getPublicVlan(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan':

        data = self.client.call(
            self.service,
            'getPublicVlan',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway.Status import Status
        return Status(data)


