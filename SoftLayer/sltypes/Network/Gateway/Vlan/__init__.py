from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Gateway_Vlan(Entity):
    bypassFlag: bool
    id_: int
    networkGatewayId: int
    networkVlanId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Gateway_Vlan'

    def bypass(self, identifier: int) -> None:
        """Bypass VLAN"""
        data = self.client.call('SoftLayer_Network_Gateway_Vlan', 'bypass', id=identifier)
        return data

    def createObject(self, templateObject: 'Network_Gateway_Vlan') -> 'Network_Gateway_Vlan':
        """Attach a VLAN to a gateway"""
        data = self.client.call('SoftLayer_Network_Gateway_Vlan', 'createObject', templateObject)
        return data

    def createObjects(self, templateObjects: 'Network_Gateway_Vlan') -> list['Network_Gateway_Vlan']:
        """Attach a VLAN to a gateway"""
        data = self.client.call('SoftLayer_Network_Gateway_Vlan', 'createObjects', templateObjects)
        return data

    def deleteObject(self, identifier: int) -> None:
        """Detach VLAN"""
        data = self.client.call('SoftLayer_Network_Gateway_Vlan', 'deleteObject', id=identifier)
        return data

    def deleteObjects(self, templateObjects: 'Network_Gateway_Vlan') -> bool:
        """Attach a VLAN to a gateway"""
        data = self.client.call('SoftLayer_Network_Gateway_Vlan', 'deleteObjects', templateObjects)
        return data

    def getObject(self, identifier: int) -> 'Network_Gateway_Vlan':
        """Retrieve a SoftLayer_Network_Gateway_Vlan record."""
        data = self.client.call('SoftLayer_Network_Gateway_Vlan', 'getObject', id=identifier)
        return data

    def unbypass(self, identifier: int) -> None:
        """Unbypass VLAN"""
        data = self.client.call('SoftLayer_Network_Gateway_Vlan', 'unbypass', id=identifier)
        return data

    def getNetworkGateway(self, identifier: int) -> 'Network_Gateway':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway_Vlan', 'getNetworkGateway', id=identifier)
        from SoftLayer.sltypes.Network_Gateway import Network_Gateway
        return data

    def getNetworkVlan(self, identifier: int) -> 'Network_Vlan':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway_Vlan', 'getNetworkVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data
