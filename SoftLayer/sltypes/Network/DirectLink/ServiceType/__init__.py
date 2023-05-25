from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_DirectLink_ServiceType(Entity):
    """The SoftLayer_Network_DirectLink_ServiceType presents a structure containing attributes of a Direct Link
Service Type."""
    id_: int
    type_: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_DirectLink_ServiceType'

    def getObject(self, identifier: int) -> 'Network_DirectLink_ServiceType':
        """Retrieve a SoftLayer_Network_DirectLink_ServiceType record."""
        data = self.client.call('SoftLayer_Network_DirectLink_ServiceType', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_DirectLink_ServiceType import Network_DirectLink_ServiceType
        return data
