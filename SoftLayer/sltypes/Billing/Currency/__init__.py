from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Currency(Entity):
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Currency'

    def getAllObjects(self) -> list['Billing_Currency']:
        data = self.client.call('SoftLayer_Billing_Currency', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Billing_Currency':
        """Retrieve a SoftLayer_Billing_Currency record."""
        data = self.client.call('SoftLayer_Billing_Currency', 'getObject', id=identifier)
        return data

    def getPrice(self, identifier: int, price: float, formatOptions: 'Container_Billing_Currency_Format') -> str:
        data = self.client.call('SoftLayer_Billing_Currency', 'getPrice', price, formatOptions, id=identifier)
        return data

    def getCurrentExchangeRate(self, identifier: int) -> 'Billing_Currency_ExchangeRate':
        """"""
        data = self.client.call('SoftLayer_Billing_Currency', 'getCurrentExchangeRate', id=identifier)
        from SoftLayer.sltypes.Billing_Currency_ExchangeRate import Billing_Currency_ExchangeRate
        return data
