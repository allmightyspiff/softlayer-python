from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Locale_Country(Entity):
    isEuropeanUnionFlag: int
    isoCodeAlphaThree: str
    longName: str
    postalCodeFormat: str
    postalCodeRequiredFlag: int
    shortName: str
    vatIdRegex: str
    vatIdRequiredFlag: bool

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Locale_Country'

    def getAllVatCountryCodesAndVatIdRegexes(self) -> list['Container_Collection_Locale_VatCountryCodeAndFormat']:
        data = self.client.call('SoftLayer_Locale_Country', 'getAllVatCountryCodesAndVatIdRegexes')
        from SoftLayer.sltypes.Container_Collection_Locale_VatCountryCodeAndFormat import Container_Collection_Locale_VatCountryCodeAndFormat
        return data

    def getAvailableCountries(self) -> list['Locale_Country']:
        data = self.client.call('SoftLayer_Locale_Country', 'getAvailableCountries')
        from SoftLayer.sltypes.Locale_Country import Locale_Country
        return data

    def getCountries(self) -> list['Locale_Country']:
        data = self.client.call('SoftLayer_Locale_Country', 'getCountries')
        from SoftLayer.sltypes.Locale_Country import Locale_Country
        return data

    def getCountriesAndStates(self, usFirstFlag: bool) -> list['Container_Collection_Locale_CountryCode']:
        data = self.client.call('SoftLayer_Locale_Country', 'getCountriesAndStates', usFirstFlag)
        from SoftLayer.sltypes.Container_Collection_Locale_CountryCode import Container_Collection_Locale_CountryCode
        return data

    def getObject(self, identifier: int) -> 'Locale_Country':
        """Retrieve a SoftLayer_Locale_Country record."""
        data = self.client.call('SoftLayer_Locale_Country', 'getObject', id=identifier)
        from SoftLayer.sltypes.Locale_Country import Locale_Country
        return data

    def getPostalCodeRequiredCountryCodes(self) -> list[str]:
        data = self.client.call('SoftLayer_Locale_Country', 'getPostalCodeRequiredCountryCodes')
        return data

    def getVatCountries(self) -> list[str]:
        data = self.client.call('SoftLayer_Locale_Country', 'getVatCountries')
        return data

    def getVatRequiredCountryCodes(self) -> list[str]:
        data = self.client.call('SoftLayer_Locale_Country', 'getVatRequiredCountryCodes')
        return data

    def isEuropeanUnionCountry(self, iso2CountryCode: str) -> bool:
        data = self.client.call('SoftLayer_Locale_Country', 'isEuropeanUnionCountry', iso2CountryCode)
        return data

    def getStates(self, identifier: int) -> list['Locale_StateProvince']:
        """"""
        data = self.client.call('SoftLayer_Locale_Country', 'getStates', id=identifier)
        from SoftLayer.sltypes.Locale_StateProvince import Locale_StateProvince
        return data
