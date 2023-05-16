# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Resource_Group(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Resource_Group'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Resource_Group
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Resource_Group':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Resource.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getAncestorGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group]':
        data = self.client.call(
            self.service,
            'getAncestorGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group_Attribute]':
        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group.Attribute import Attribute
        return SL_Attribute(data)

# This file was automatically generated with tools/generateTypes.py
    def getHardwareMembers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group_Member]':
        data = self.client.call(
            self.service,
            'getHardwareMembers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group.Member import Member
        return SL_Member(data)

# This file was automatically generated with tools/generateTypes.py
    def getMembers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group_Member]':
        data = self.client.call(
            self.service,
            'getMembers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group.Member import Member
        return SL_Member(data)

# This file was automatically generated with tools/generateTypes.py
    def getRootResourceGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Resource_Group':
        data = self.client.call(
            self.service,
            'getRootResourceGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Resource.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getSubnetMembers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group_Member]':
        data = self.client.call(
            self.service,
            'getSubnetMembers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group.Member import Member
        return SL_Member(data)

# This file was automatically generated with tools/generateTypes.py
    def getTemplate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Resource_Group_Template':
        data = self.client.call(
            self.service,
            'getTemplate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Resource.Group.Template import Template
        return SL_Template(data)

# This file was automatically generated with tools/generateTypes.py
    def getVlanMembers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group_Member]':
        data = self.client.call(
            self.service,
            'getVlanMembers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group.Member import Member
        return SL_Member(data)


