from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Brand_Restriction_Location_CustomerCountry(Entity):
    """The [[SoftLayer_Brand_Restriction_Location_CustomerCountry]] data type defines the relationship between
brands, locations and countries associated with a user's account that are ineligible when ordering products.
For example, the India datacenter may not be available on the SoftLayer US brand for customers that live in
Great Britain."""
    brandId: int
    customerCountryCode: str
    locationId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Brand_Restriction_Location_CustomerCountry'

    def getAllObjects(self) -> list['Brand_Restriction_Location_CustomerCountry']:
        data = self.client.call('SoftLayer_Brand_Restriction_Location_CustomerCountry', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Brand_Restriction_Location_CustomerCountry':
        """Retrieve a SoftLayer_Brand_Restriction_Location_CustomerCountry record."""
        data = self.client.call('SoftLayer_Brand_Restriction_Location_CustomerCountry', 'getObject', id=identifier)
        return data

    def getBrand(self, identifier: int) -> 'Brand':
        """"""
        data = self.client.call('SoftLayer_Brand_Restriction_Location_CustomerCountry', 'getBrand', id=identifier)
        from SoftLayer.sltypes.Brand import Brand
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Brand_Restriction_Location_CustomerCountry', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data
