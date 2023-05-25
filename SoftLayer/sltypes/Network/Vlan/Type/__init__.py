from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Vlan_Type(Entity):
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Vlan_Type'

    def getObject(self, identifier: int) -> 'Network_Vlan_Type':
        """Retrieve a SoftLayer_Network_Vlan_Type record."""
        data = self.client.call('SoftLayer_Network_Vlan_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Vlan_Type import Network_Vlan_Type
        return data
