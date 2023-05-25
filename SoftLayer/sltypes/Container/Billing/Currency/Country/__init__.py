from SoftLayer.sltypes.Billing.Currency.Country import Billing_Currency_Country
from SoftLayer.sltypes.Locale.Country import Locale_Country
from SoftLayer.sltypes.Billing.Currency import Billing_Currency
from SoftLayer.sltypes.Entity import Entity

class Container_Billing_Currency_Country(Entity):
    availableCurrencies: list[Billing_Currency]
    country: Locale_Country
    currencyCountryLocales: list[Billing_Currency_Country]
