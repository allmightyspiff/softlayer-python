# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Locale_Country(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Locale_Country'
        self.client = client

    def getAllVatCountryCodesAndVatIdRegexes(
        self,
        
    ) -> 'list[SoftLayer_Container_Collection_Locale_VatCountryCodeAndFormat]':

        data = self.client.call(
            self.service,
            'getAllVatCountryCodesAndVatIdRegexes',
            
        )
        from SoftLayer.datatypes.Container.Collection.Locale.VatCountryCodeAndFormat import VatCountryCodeAndFormat
        return VatCountryCodeAndFormat(data)


    def getAvailableCountries(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Locale_Country]':

        data = self.client.call(
            self.service,
            'getAvailableCountries',
            mask=objectMask
        )
        from SoftLayer.datatypes.Locale.Country import Country
        return Country(data)


    def getCountries(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Locale_Country]':

        data = self.client.call(
            self.service,
            'getCountries',
            mask=objectMask
        )
        from SoftLayer.datatypes.Locale.Country import Country
        return Country(data)


    def getCountriesAndStates(
        self,
        usFirstFlag: boolean
    ) -> 'list[SoftLayer_Container_Collection_Locale_CountryCode]':

        data = self.client.call(
            self.service,
            'getCountriesAndStates',
            usFirstFlag
        )
        from SoftLayer.datatypes.Container.Collection.Locale.CountryCode import CountryCode
        return CountryCode(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Locale_Country':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Locale.Country import Country
        return Country(data)


    def getPostalCodeRequiredCountryCodes(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getPostalCodeRequiredCountryCodes',
            
        )
        
        return data


    def getVatCountries(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getVatCountries',
            
        )
        
        return data


    def getVatRequiredCountryCodes(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getVatRequiredCountryCodes',
            
        )
        
        return data


    def isEuropeanUnionCountry(
        self,
        iso2CountryCode: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isEuropeanUnionCountry',
            iso2CountryCode
        )
        
        return data


    def getStates(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Locale_StateProvince]':

        data = self.client.call(
            self.service,
            'getStates',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Locale.StateProvince import StateProvince
        return StateProvince(data)


