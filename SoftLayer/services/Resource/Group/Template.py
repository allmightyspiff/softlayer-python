# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Resource_Group_Template(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Resource_Group_Template'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group_Template]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group.Template import Template
        return Template(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Resource_Group_Template':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Resource.Group.Template import Template
        return Template(data)


    def getChildren(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group_Template]':

        data = self.client.call(
            self.service,
            'getChildren',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group.Template import Template
        return Template(data)


    def getMembers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Resource_Group_Template_Member]':

        data = self.client.call(
            self.service,
            'getMembers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Resource.Group.Template.Member import Member
        return Member(data)


