# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Tunnel_Module_Context(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Tunnel_Module_Context'
        self.client = client

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


    def applyConfigurationsToDevice(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'applyConfigurationsToDevice',
            
        )
        
        return data


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
        return Translation(data)


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
        return Translation(data)


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


    def downloadAddressTranslationConfigurations(
        self,
        
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'downloadAddressTranslationConfigurations',
            
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def downloadParameterConfigurations(
        self,
        
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'downloadParameterConfigurations',
            
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


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
        return Translation(data)


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
        return Translation(data)


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


    def getAddressTranslationConfigurations(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAddressTranslationConfigurations',
            
        )
        
        return data


    def getAuthenticationDefault(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAuthenticationDefault',
            
        )
        
        return data


    def getAuthenticationOptions(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getAuthenticationOptions',
            
        )
        
        return data


    def getDiffieHellmanGroupDefault(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getDiffieHellmanGroupDefault',
            
        )
        
        return data


    def getDiffieHellmanGroupOptions(
        self,
        
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getDiffieHellmanGroupOptions',
            
        )
        
        return data


    def getEncryptionDefault(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getEncryptionDefault',
            
        )
        
        return data


    def getEncryptionOptions(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getEncryptionOptions',
            
        )
        
        return data


    def getKeylifeLimits(
        self,
        
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getKeylifeLimits',
            
        )
        
        return data


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
        return Context(data)


    def getParameterConfigurationsForCustomerView(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getParameterConfigurationsForCustomerView',
            
        )
        
        return data


    def getPhaseOneKeylifeDefault(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPhaseOneKeylifeDefault',
            
        )
        
        return data


    def getPhaseTwoKeylifeDefault(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPhaseTwoKeylifeDefault',
            
        )
        
        return data


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
        return Transaction(data)


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
        return Translation(data)


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
        return Subnet(data)


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
        return Item(data)


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
        return Subnet(data)


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
        return Location(data)


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
        return Subnet(data)


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
        return Subnet(data)


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
        return Subnet(data)


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
        return Transaction(data)


