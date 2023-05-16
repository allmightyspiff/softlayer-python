# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Currency_Country(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Currency_Country'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getCountriesWithListOfEligibleCurrencies(
        self,
        
    ) -> 'list[SoftLayer_Container_Billing_Currency_Country]':
        data = self.client.call(
            self.service,
            'getCountriesWithListOfEligibleCurrencies',
            
        )
        from SoftLayer.datatypes.Container.Billing.Currency.Country import Country
        return SL_Country(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency_Country':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency.Country import Country
        return SL_Country(data)


