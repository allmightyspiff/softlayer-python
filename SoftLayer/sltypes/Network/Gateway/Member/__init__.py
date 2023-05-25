from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Gateway_Member(Entity):
    gatewaySoftwareId: int
    hardwareId: int
    id_: int
    networkGatewayId: int
    priority: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Gateway_Member'

    def createObject(self, templateObject: 'Network_Gateway_Member') -> 'Network_Gateway_Member':
        """Add a member to a gateway"""
        data = self.client.call('SoftLayer_Network_Gateway_Member', 'createObject', templateObject)
        return data

    def createObjects(self, templateObjects: 'Network_Gateway_Member') -> list['Network_Gateway_Member']:
        """Add a member to a gateway"""
        data = self.client.call('SoftLayer_Network_Gateway_Member', 'createObjects', templateObjects)
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Gateway_Member') -> bool:
        """Edit Gateway Nmemnber"""
        data = self.client.call('SoftLayer_Network_Gateway_Member', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Gateway_Member':
        """Retrieve a SoftLayer_Network_Gateway_Member record."""
        data = self.client.call('SoftLayer_Network_Gateway_Member', 'getObject', id=identifier)
        return data

    def getAttributes(self, identifier: int) -> 'Network_Gateway_Member_Attribute':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway_Member', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Network_Gateway_Member_Attribute import Network_Gateway_Member_Attribute
        return data

    def getGatewaySoftwareDescription(self, identifier: int) -> 'Software_Description':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway_Member', 'getGatewaySoftwareDescription', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway_Member', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getLicenses(self, identifier: int) -> list['Network_Gateway_Member_Licenses']:
        """"""
        data = self.client.call('SoftLayer_Network_Gateway_Member', 'getLicenses', id=identifier)
        from SoftLayer.sltypes.Network_Gateway_Member_Licenses import Network_Gateway_Member_Licenses
        return data

    def getNetworkGateway(self, identifier: int) -> 'Network_Gateway':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway_Member', 'getNetworkGateway', id=identifier)
        from SoftLayer.sltypes.Network_Gateway import Network_Gateway
        return data

    def getPasswords(self, identifier: int) -> list['Network_Gateway_Member_Passwords']:
        """"""
        data = self.client.call('SoftLayer_Network_Gateway_Member', 'getPasswords', id=identifier)
        from SoftLayer.sltypes.Network_Gateway_Member_Passwords import Network_Gateway_Member_Passwords
        return data

    def getPublicIpAddress(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway_Member', 'getPublicIpAddress', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data
