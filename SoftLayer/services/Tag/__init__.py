# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Tag(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Tag'
        self.client = client

    def autoComplete(
        self,
        tag: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Tag]':

        data = self.client.call(
            self.service,
            'autoComplete',
            tag,
            mask=objectMask
        )
        from SoftLayer.datatypes.Tag import Tag
        return Tag(data)


    def deleteTag(
        self,
        tagName: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteTag',
            tagName
        )
        
        return data


    def getAllTagTypes(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Tag_Type]':

        data = self.client.call(
            self.service,
            'getAllTagTypes',
            mask=objectMask
        )
        from SoftLayer.datatypes.Tag.Type import Type
        return Type(data)


    def getAttachedTagsForCurrentUser(
        self,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag]':

        data = self.client.call(
            self.service,
            'getAttachedTagsForCurrentUser',
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag import Tag
        return Tag(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Tag':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Tag import Tag
        return Tag(data)


    def getTagByTagName(
        self,
        tagList: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Tag]':

        data = self.client.call(
            self.service,
            'getTagByTagName',
            tagList,
            mask=objectMask
        )
        from SoftLayer.datatypes.Tag import Tag
        return Tag(data)


    def getUnattachedTagsForCurrentUser(
        self,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag]':

        data = self.client.call(
            self.service,
            'getUnattachedTagsForCurrentUser',
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag import Tag
        return Tag(data)


    def setTags(
        self,
        tags: str,
        keyName: str,
        resourceTableId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setTags',
            tags,
            keyName,
            resourceTableId
        )
        
        return data


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getReferences(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':

        data = self.client.call(
            self.service,
            'getReferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return Reference(data)


