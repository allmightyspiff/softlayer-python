# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Currency_ExchangeRate(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Currency_ExchangeRate'
        self.client = client

    def getAllCurrencyExchangeRates(
        self,
        stringDate: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Billing_Currency_ExchangeRate]':

        data = self.client.call(
            self.service,
            'getAllCurrencyExchangeRates',
            stringDate,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Currency.ExchangeRate import ExchangeRate
        return ExchangeRate(data)


    def getCurrencies(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Billing_Currency]':

        data = self.client.call(
            self.service,
            'getCurrencies',
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Currency import Currency
        return Currency(data)


    def getExchangeRate(
        self,
        to: str,
        from: str,
        effectiveDate: dateTime,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Currency_ExchangeRate':

        data = self.client.call(
            self.service,
            'getExchangeRate',
            to,
            from,
            effectiveDate,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Currency.ExchangeRate import ExchangeRate
        return ExchangeRate(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency_ExchangeRate':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency.ExchangeRate import ExchangeRate
        return ExchangeRate(data)


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


    def getFundingCurrency(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency':

        data = self.client.call(
            self.service,
            'getFundingCurrency',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency import Currency
        return Currency(data)


    def getLocalCurrency(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency':

        data = self.client.call(
            self.service,
            'getLocalCurrency',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency import Currency
        return Currency(data)


