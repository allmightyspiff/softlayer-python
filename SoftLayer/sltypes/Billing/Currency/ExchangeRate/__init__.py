from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Currency_ExchangeRate(Entity):
    effectiveDate: datetime
    expirationDate: datetime
    id_: int
    rate: float

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Currency_ExchangeRate'

    def getAllCurrencyExchangeRates(self, identifier: int, stringDate: str) -> list['Billing_Currency_ExchangeRate']:
        data = self.client.call('SoftLayer_Billing_Currency_ExchangeRate', 'getAllCurrencyExchangeRates', stringDate, id=identifier)
        from SoftLayer.sltypes.Billing_Currency_ExchangeRate import Billing_Currency_ExchangeRate
        return data

    def getCurrencies(self) -> list['Billing_Currency']:
        data = self.client.call('SoftLayer_Billing_Currency_ExchangeRate', 'getCurrencies')
        from SoftLayer.sltypes.Billing_Currency import Billing_Currency
        return data

    def getExchangeRate(self, to: str, from_: str, effectiveDate: datetime) -> 'Billing_Currency_ExchangeRate':
        data = self.client.call('SoftLayer_Billing_Currency_ExchangeRate', 'getExchangeRate', to, from, effectiveDate)
        from SoftLayer.sltypes.Billing_Currency_ExchangeRate import Billing_Currency_ExchangeRate
        return data

    def getObject(self, identifier: int) -> 'Billing_Currency_ExchangeRate':
        """Retrieve a SoftLayer_Billing_Currency_ExchangeRate record."""
        data = self.client.call('SoftLayer_Billing_Currency_ExchangeRate', 'getObject', id=identifier)
        from SoftLayer.sltypes.Billing_Currency_ExchangeRate import Billing_Currency_ExchangeRate
        return data

    def getPrice(self, identifier: int, price: float, formatOptions: 'Container_Billing_Currency_Format') -> str:
        data = self.client.call('SoftLayer_Billing_Currency_ExchangeRate', 'getPrice', price, formatOptions, id=identifier)
        return data

    def getFundingCurrency(self, identifier: int) -> 'Billing_Currency':
        """"""
        data = self.client.call('SoftLayer_Billing_Currency_ExchangeRate', 'getFundingCurrency', id=identifier)
        from SoftLayer.sltypes.Billing_Currency import Billing_Currency
        return data

    def getLocalCurrency(self, identifier: int) -> 'Billing_Currency':
        """"""
        data = self.client.call('SoftLayer_Billing_Currency_ExchangeRate', 'getLocalCurrency', id=identifier)
        from SoftLayer.sltypes.Billing_Currency import Billing_Currency
        return data
