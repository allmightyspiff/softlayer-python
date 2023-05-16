# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Tag(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Tag'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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
        return SL_Tag(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Tag(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Tag':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Tag import Tag
        return SL_Tag(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Tag(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Tag(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':
        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':
        data = self.client.call(
            self.service,
            'getReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return SL_Reference(data)


