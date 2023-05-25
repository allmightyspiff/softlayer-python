from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Layout_Item(Entity):
    """The SoftLayer_Layout_Item contains definitions for default layout items"""
    id_: int
    keyname: str
    layoutItemTypeId: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Layout_Item'

    def getObject(self, identifier: int) -> 'Layout_Item':
        """Retrieve a SoftLayer_Layout_Item record."""
        data = self.client.call('SoftLayer_Layout_Item', 'getObject', id=identifier)
        return data

    def getLayoutItemPreferences(self, identifier: int) -> list['Layout_Preference']:
        """"""
        data = self.client.call('SoftLayer_Layout_Item', 'getLayoutItemPreferences', id=identifier)
        from SoftLayer.sltypes.Layout_Preference import Layout_Preference
        return data

    def getLayoutItemType(self, identifier: int) -> 'Layout_Item_Type':
        """"""
        data = self.client.call('SoftLayer_Layout_Item', 'getLayoutItemType', id=identifier)
        from SoftLayer.sltypes.Layout_Item_Type import Layout_Item_Type
        return data
