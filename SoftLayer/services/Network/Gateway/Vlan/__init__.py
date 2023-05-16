# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Gateway_Vlan(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Gateway_Vlan'
        self.client = client

    def bypass(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'bypass',
            id=identifier
        )
        
        return data


    def createObject(
        self,
        templateObject: 'SoftLayer_Network_Gateway_Vlan',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Gateway_Vlan':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Gateway.Vlan import Vlan
        return Vlan(data)


    def createObjects(
        self,
        templateObjects: 'SoftLayer_Network_Gateway_Vlan',
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Gateway_Vlan]':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Gateway.Vlan import Vlan
        return Vlan(data)


    def deleteObject(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'deleteObject',
            id=identifier
        )
        
        return data


    def deleteObjects(
        self,
        templateObjects: 'SoftLayer_Network_Gateway_Vlan'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObjects',
            templateObjects
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway_Vlan':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway.Vlan import Vlan
        return Vlan(data)


    def unbypass(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'unbypass',
            id=identifier
        )
        
        return data


    def getNetworkGateway(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Gateway':

        data = self.client.call(
            self.service,
            'getNetworkGateway',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Gateway import Gateway
        return Gateway(data)


    def getNetworkVlan(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan':

        data = self.client.call(
            self.service,
            'getNetworkVlan',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


