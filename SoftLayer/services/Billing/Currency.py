# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Currency(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Currency'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Billing_Currency]':
        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency import Currency
        return SL_Currency(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency import Currency
        return SL_Currency(data)

# This file was automatically generated with tools/generateTypes.py
    def getPrice(
        self,
        price: float,
        formatOptions: SoftLayer_Container_Billing_Currency_Format
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPrice',
            price,
            formatOptions
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCurrentExchangeRate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency_ExchangeRate':
        data = self.client.call(
            self.service,
            'getCurrentExchangeRate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency.ExchangeRate import ExchangeRate
        return SL_ExchangeRate(data)


