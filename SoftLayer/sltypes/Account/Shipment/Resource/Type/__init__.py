from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Shipment_Resource_Type(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Shipment_Resource_Type'

    def getObject(self, identifier: int) -> 'Account_Shipment_Resource_Type':
        """Retrieve a SoftLayer_Account_Shipment_Resource_Type record."""
        data = self.client.call('SoftLayer_Account_Shipment_Resource_Type', 'getObject', id=identifier)
        return data
