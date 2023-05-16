# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Configuration_Mapping(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Configuration_Mapping'
        self.client = client

    def createDomainMapping(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping]':

        data = self.client.call(
            self.service,
            'createDomainMapping',
            input
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping import Mapping
        return Mapping(data)


    def deleteDomainMapping(
        self,
        uniqueId: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping]':

        data = self.client.call(
            self.service,
            'deleteDomainMapping',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping import Mapping
        return Mapping(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Mapping':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Mapping import Mapping
        return Mapping(data)


    def listDomainMappingByUniqueId(
        self,
        uniqueId: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping]':

        data = self.client.call(
            self.service,
            'listDomainMappingByUniqueId',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping import Mapping
        return Mapping(data)


    def listDomainMappings(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping]':

        data = self.client.call(
            self.service,
            'listDomainMappings',
            
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping import Mapping
        return Mapping(data)


    def retryHttpsActionRequest(
        self,
        uniqueId: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping]':

        data = self.client.call(
            self.service,
            'retryHttpsActionRequest',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping import Mapping
        return Mapping(data)


    def startDomainMapping(
        self,
        uniqueId: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping]':

        data = self.client.call(
            self.service,
            'startDomainMapping',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping import Mapping
        return Mapping(data)


    def stopDomainMapping(
        self,
        uniqueId: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping]':

        data = self.client.call(
            self.service,
            'stopDomainMapping',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping import Mapping
        return Mapping(data)


    def updateDomainMapping(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping]':

        data = self.client.call(
            self.service,
            'updateDomainMapping',
            input
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping import Mapping
        return Mapping(data)


    def verifyCname(
        self,
        cname: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'verifyCname',
            cname
        )
        
        return data


    def verifyDomainMapping(
        self,
        uniqueId: int
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping]':

        data = self.client.call(
            self.service,
            'verifyDomainMapping',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping import Mapping
        return Mapping(data)


