# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Gateway(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Gateway'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def bypassAllVlans(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'bypassAllVlans',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Gateway(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getCapacity(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getCapacity',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getMemberGatewayImagesMatch(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getMemberGatewayImagesMatch',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Gateway(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
    def getRollbackSupport(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getRollbackSupport',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Price(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def isRollbackAllowed(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isRollbackAllowed',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def rebuildHACluster(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'rebuildHACluster',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def rebuildvSRXHACluster(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'rebuildvSRXHACluster',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def refreshGatewayLicense(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'refreshGatewayLicense',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def unbypassAllVlans(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'unbypassAllVlans',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Member(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Firewall(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_IpAddress(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_IpAddress(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_IpAddress(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Vlan(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Status(data)


