# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Permission_Group_Type(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Permission_Group_Type'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Permission_Group_Type':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Permission.Group.Type import Type
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
    def getGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Group]':
        data = self.client.call(
            self.service,
            'getGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Group import Group
        return SL_Group(data)


