from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Gateway_Member_Attribute(Entity):
    id_: int
    isUpgraded: int
    lastvSRXVersion: str
    licenseExpirationDate: datetime
    licenseKey: str
    memberId: int
    networkModel: str
    password: str
    upgradedDate: datetime
    username: str
    vSRXVersion: str
    warningCode: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Gateway_Member_Attribute'

    def getObject(self, identifier: int) -> 'Network_Gateway_Member_Attribute':
        """Retrieve a SoftLayer_Network_Gateway_Member_Attribute record."""
        data = self.client.call('SoftLayer_Network_Gateway_Member_Attribute', 'getObject', id=identifier)
        return data

    def getGatewayMember(self, identifier: int) -> 'Network_Gateway_Member':
        """"""
        data = self.client.call('SoftLayer_Network_Gateway_Member_Attribute', 'getGatewayMember', id=identifier)
        from SoftLayer.sltypes.Network_Gateway_Member import Network_Gateway_Member
        return data
