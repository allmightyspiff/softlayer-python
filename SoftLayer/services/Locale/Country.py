# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Locale_Country(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Locale_Country'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAllVatCountryCodesAndVatIdRegexes(
        self,
        
    ) -> 'list[SoftLayer_Container_Collection_Locale_VatCountryCodeAndFormat]':
        data = self.client.call(
            self.service,
            'getAllVatCountryCodesAndVatIdRegexes',
            
        )
        from SoftLayer.datatypes.Container.Collection.Locale.VatCountryCodeAndFormat import VatCountryCodeAndFormat
        return SL_VatCountryCodeAndFormat(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Country(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Country(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_CountryCode(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Country(data)

# This file was automatically generated with tools/generateTypes.py
    def getPostalCodeRequiredCountryCodes(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getPostalCodeRequiredCountryCodes',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getVatCountries(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getVatCountries',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getVatRequiredCountryCodes(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getVatRequiredCountryCodes',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_StateProvince(data)


