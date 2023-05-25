from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Auxiliary_Shipping_Courier_Type(Entity):
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Auxiliary_Shipping_Courier_Type'

    def getObject(self, identifier: int) -> 'Auxiliary_Shipping_Courier_Type':
        """Retrieve a SoftLayer_Auxiliary_Shipping_Courier_Type record."""
        data = self.client.call('SoftLayer_Auxiliary_Shipping_Courier_Type', 'getObject', id=identifier)
        return data

    def getTypeByKeyName(self, keyName: str) -> 'Auxiliary_Shipping_Courier_Type':
        data = self.client.call('SoftLayer_Auxiliary_Shipping_Courier_Type', 'getTypeByKeyName', keyName)
        return data

    def getCourier(self, identifier: int) -> list['Auxiliary_Shipping_Courier']:
        """"""
        data = self.client.call('SoftLayer_Auxiliary_Shipping_Courier_Type', 'getCourier', id=identifier)
        from SoftLayer.sltypes.Auxiliary_Shipping_Courier import Auxiliary_Shipping_Courier
        return data
