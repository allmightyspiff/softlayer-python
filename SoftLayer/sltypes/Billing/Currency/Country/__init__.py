from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Currency_Country(Entity):
    """The SoftLayer_Billing_Currency_Country data type maps what currencies are valid for specific countries. US
Dollars are valid from any country, but other currencies are only available to customers in certain
countries."""
    countryId: int
    currencyId: int
    id_: int
    locale: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Currency_Country'

    def getCountriesWithListOfEligibleCurrencies(self) -> list['Container_Billing_Currency_Country']:
        """Get map between countries and what currencies can be supported for customers in that country."""
        data = self.client.call('SoftLayer_Billing_Currency_Country', 'getCountriesWithListOfEligibleCurrencies')
        from SoftLayer.sltypes.Container_Billing_Currency_Country import Container_Billing_Currency_Country
        return data

    def getObject(self, identifier: int) -> 'Billing_Currency_Country':
        """Retrieve a SoftLayer_Billing_Currency_Country record."""
        data = self.client.call('SoftLayer_Billing_Currency_Country', 'getObject', id=identifier)
        return data
