# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Tunnel_Module_Context(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Tunnel_Module_Context'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def addCustomerSubnetToNetworkTunnel(
        self,
        subnetId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'addCustomerSubnetToNetworkTunnel',
            subnetId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def addPrivateSubnetToNetworkTunnel(
        self,
        subnetId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'addPrivateSubnetToNetworkTunnel',
            subnetId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def addServiceSubnetToNetworkTunnel(
        self,
        subnetId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'addServiceSubnetToNetworkTunnel',
            subnetId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def applyConfigurationsToDevice(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'applyConfigurationsToDevice',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def createAddressTranslation(
        self,
        translation: SoftLayer_Network_Tunnel_Module_Context_Address_Translation,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Tunnel_Module_Context_Address_Translation':
        data = self.client.call(
            self.service,
            'createAddressTranslation',
            translation,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Tunnel.Module.Context.Address.Translation import Translation
        return SL_Translation(data)

# This file was automatically generated with tools/generateTypes.py
    def createAddressTranslations(
        self,
        translations: SoftLayer_Network_Tunnel_Module_Context_Address_Translation,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Tunnel_Module_Context_Address_Translation]':
        data = self.client.call(
            self.service,
            'createAddressTranslations',
            translations,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Tunnel.Module.Context.Address.Translation import Translation
        return SL_Translation(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteAddressTranslation(
        self,
        translationId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteAddressTranslation',
            translationId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def downloadAddressTranslationConfigurations(
        self,
        
    ) -> 'SoftLayer_Container_Utility_File_Entity':
        data = self.client.call(
            self.service,
            'downloadAddressTranslationConfigurations',
            
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return SL_Entity(data)

# This file was automatically generated with tools/generateTypes.py
    def downloadParameterConfigurations(
        self,
        
    ) -> 'SoftLayer_Container_Utility_File_Entity':
        data = self.client.call(
            self.service,
            'downloadParameterConfigurations',
            
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return SL_Entity(data)

# This file was automatically generated with tools/generateTypes.py
    def editAddressTranslation(
        self,
        translation: SoftLayer_Network_Tunnel_Module_Context_Address_Translation,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Tunnel_Module_Context_Address_Translation':
        data = self.client.call(
            self.service,
            'editAddressTranslation',
            translation,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Tunnel.Module.Context.Address.Translation import Translation
        return SL_Translation(data)

# This file was automatically generated with tools/generateTypes.py
    def editAddressTranslations(
        self,
        translations: SoftLayer_Network_Tunnel_Module_Context_Address_Translation,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Tunnel_Module_Context_Address_Translation]':
        data = self.client.call(
            self.service,
            'editAddressTranslations',
            translations,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Tunnel.Module.Context.Address.Translation import Translation
        return SL_Translation(data)

# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Network_Tunnel_Module_Context
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAddressTranslationConfigurations(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getAddressTranslationConfigurations',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAuthenticationDefault(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getAuthenticationDefault',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAuthenticationOptions(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getAuthenticationOptions',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDiffieHellmanGroupDefault(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getDiffieHellmanGroupDefault',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDiffieHellmanGroupOptions(
        self,
        
    ) -> 'list[int]':
        data = self.client.call(
            self.service,
            'getDiffieHellmanGroupOptions',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getEncryptionDefault(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getEncryptionDefault',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getEncryptionOptions(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getEncryptionOptions',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getKeylifeLimits(
        self,
        
    ) -> 'list[int]':
        data = self.client.call(
            self.service,
            'getKeylifeLimits',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Tunnel_Module_Context':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Tunnel.Module.Context import Context
        return SL_Context(data)

# This file was automatically generated with tools/generateTypes.py
    def getParameterConfigurationsForCustomerView(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getParameterConfigurationsForCustomerView',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPhaseOneKeylifeDefault(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPhaseOneKeylifeDefault',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPhaseTwoKeylifeDefault(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPhaseTwoKeylifeDefault',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeCustomerSubnetFromNetworkTunnel(
        self,
        subnetId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeCustomerSubnetFromNetworkTunnel',
            subnetId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removePrivateSubnetFromNetworkTunnel(
        self,
        subnetId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removePrivateSubnetFromNetworkTunnel',
            subnetId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeServiceSubnetFromNetworkTunnel(
        self,
        subnetId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeServiceSubnetFromNetworkTunnel',
            subnetId
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
    def getActiveTransaction(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':
        data = self.client.call(
            self.service,
            'getActiveTransaction',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return SL_Transaction(data)

# This file was automatically generated with tools/generateTypes.py
    def getAddressTranslations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Tunnel_Module_Context_Address_Translation]':
        data = self.client.call(
            self.service,
            'getAddressTranslations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Tunnel.Module.Context.Address.Translation import Translation
        return SL_Translation(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllAvailableServiceSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':
        data = self.client.call(
            self.service,
            'getAllAvailableServiceSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return SL_Subnet(data)

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
    def getCustomerSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Customer_Subnet]':
        data = self.client.call(
            self.service,
            'getCustomerSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Customer.Subnet import Subnet
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
    def getDatacenter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':
        data = self.client.call(
            self.service,
            'getDatacenter',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getInternalSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':
        data = self.client.call(
            self.service,
            'getInternalSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
    def getServiceSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':
        data = self.client.call(
            self.service,
            'getServiceSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
    def getStaticRouteSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':
        data = self.client.call(
            self.service,
            'getStaticRouteSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return SL_Subnet(data)

# This file was automatically generated with tools/generateTypes.py
    def getTransactionHistory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Provisioning_Version1_Transaction]':
        data = self.client.call(
            self.service,
            'getTransactionHistory',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return SL_Transaction(data)


