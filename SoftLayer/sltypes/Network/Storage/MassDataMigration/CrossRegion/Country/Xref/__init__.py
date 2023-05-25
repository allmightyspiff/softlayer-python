from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_MassDataMigration_CrossRegion_Country_Xref(Entity):
    countryId: int
    id_: int
    locationGroupId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref'

    def getAllObjects(self) -> list['Network_Storage_MassDataMigration_CrossRegion_Country_Xref']:
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref', 'getAllObjects')
        from SoftLayer.sltypes.Network_Storage_MassDataMigration_CrossRegion_Country_Xref import Network_Storage_MassDataMigration_CrossRegion_Country_Xref
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_MassDataMigration_CrossRegion_Country_Xref':
        """Retrieve a SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref record."""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Storage_MassDataMigration_CrossRegion_Country_Xref import Network_Storage_MassDataMigration_CrossRegion_Country_Xref
        return data

    def getValidCountriesForRegion(self, locationGroupName: str) -> list['Network_Storage_MassDataMigration_CrossRegion_Country_Xref']:
        """return countries assigned to the region having pricing info set."""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref', 'getValidCountriesForRegion', locationGroupName)
        from SoftLayer.sltypes.Network_Storage_MassDataMigration_CrossRegion_Country_Xref import Network_Storage_MassDataMigration_CrossRegion_Country_Xref
        return data

    def getCountry(self, identifier: int) -> 'Locale_Country':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref', 'getCountry', id=identifier)
        from SoftLayer.sltypes.Locale_Country import Locale_Country
        return data

    def getLocationGroup(self, identifier: int) -> 'Location_Group':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref', 'getLocationGroup', id=identifier)
        from SoftLayer.sltypes.Location_Group import Location_Group
        return data
