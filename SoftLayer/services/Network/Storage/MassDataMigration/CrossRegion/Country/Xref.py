# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref]':
        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.MassDataMigration.CrossRegion.Country.Xref import Xref
        return SL_Xref(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.MassDataMigration.CrossRegion.Country.Xref import Xref
        return SL_Xref(data)

# This file was automatically generated with tools/generateTypes.py
    def getValidCountriesForRegion(
        self,
        locationGroupName: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage_MassDataMigration_CrossRegion_Country_Xref]':
        data = self.client.call(
            self.service,
            'getValidCountriesForRegion',
            locationGroupName,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.MassDataMigration.CrossRegion.Country.Xref import Xref
        return SL_Xref(data)

# This file was automatically generated with tools/generateTypes.py
    def getCountry(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Locale_Country':
        data = self.client.call(
            self.service,
            'getCountry',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Locale.Country import Country
        return SL_Country(data)

# This file was automatically generated with tools/generateTypes.py
    def getLocationGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Group':
        data = self.client.call(
            self.service,
            'getLocationGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Group import Group
        return SL_Group(data)


