# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Location_Group(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Location_Group'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Location_Group]':
        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Location.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Group':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getLocationGroupType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Group_Type':
        data = self.client.call(
            self.service,
            'getLocationGroupType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Group.Type import Type
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
    def getLocations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Location]':
        data = self.client.call(
            self.service,
            'getLocations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)


