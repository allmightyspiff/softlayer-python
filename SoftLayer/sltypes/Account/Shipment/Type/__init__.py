from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Shipment_Type(Entity):
    createDate: datetime
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Shipment_Type'

    def getObject(self, identifier: int) -> 'Account_Shipment_Type':
        """Retrieve a SoftLayer_Account_Shipment_Type record."""
        data = self.client.call('SoftLayer_Account_Shipment_Type', 'getObject', id=identifier)
        return data
