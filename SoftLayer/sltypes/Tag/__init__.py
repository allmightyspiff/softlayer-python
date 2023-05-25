from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Tag(Entity):
    """The SoftLayer_Tag data type is an optional type associated with hardware. The account ID that the tag is tied
to, and the tag itself are stored in this data type. There is also a flag to denote whether the tag is
internal or not."""
    accountId: int
    id_: int
    internal: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Tag'

    def autoComplete(self, tag: str) -> list['Tag']:
        """Autocomplete tag inputted by a user."""
        data = self.client.call('SoftLayer_Tag', 'autoComplete', tag)
        from SoftLayer.sltypes.Tag import Tag
        return data

    def deleteTag(self, tagName: str) -> bool:
        """delete tag for a given object."""
        data = self.client.call('SoftLayer_Tag', 'deleteTag', tagName)
        return data

    def getAllTagTypes(self) -> list['Tag_Type']:
        """Get all valid tag types."""
        data = self.client.call('SoftLayer_Tag', 'getAllTagTypes')
        from SoftLayer.sltypes.Tag_Type import Tag_Type
        return data

    def getAttachedTagsForCurrentUser(self) -> list['Tag']:
        """Get the tags attached to references."""
        data = self.client.call('SoftLayer_Tag', 'getAttachedTagsForCurrentUser')
        from SoftLayer.sltypes.Tag import Tag
        return data

    def getObject(self, identifier: int) -> 'Tag':
        """Retrieve a SoftLayer_Tag record."""
        data = self.client.call('SoftLayer_Tag', 'getObject', id=identifier)
        from SoftLayer.sltypes.Tag import Tag
        return data

    def getTagByTagName(self, tagList: str) -> list['Tag']:
        """Get the tag object based on what the user inputs."""
        data = self.client.call('SoftLayer_Tag', 'getTagByTagName', tagList)
        from SoftLayer.sltypes.Tag import Tag
        return data

    def getUnattachedTagsForCurrentUser(self) -> list['Tag']:
        """Get the tags not attached to references."""
        data = self.client.call('SoftLayer_Tag', 'getUnattachedTagsForCurrentUser')
        from SoftLayer.sltypes.Tag import Tag
        return data

    def setTags(self, tags: str, keyName: str, resourceTableId: int) -> bool:
        """Set the tags for a given object."""
        data = self.client.call('SoftLayer_Tag', 'setTags', tags, keyName, resourceTableId)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Tag', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Tag', 'getReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data
