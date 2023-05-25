from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Shipment_Status(Entity):
    createDate: datetime
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Shipment_Status'

    def getObject(self, identifier: int) -> 'Account_Shipment_Status':
        """Retrieve a SoftLayer_Account_Shipment_Status record."""
        data = self.client.call('SoftLayer_Account_Shipment_Status', 'getObject', id=identifier)
        return data
