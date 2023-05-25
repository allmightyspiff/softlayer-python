from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Layout_Container(Entity):
    """The SoftLayer_Layout_Container contains definitions for default page layouts"""
    id_: int
    keyname: str
    layoutContainerTypeId: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Layout_Container'

    def getAllObjects(self) -> list['Layout_Container']:
        """Returns customizable layout containers"""
        data = self.client.call('SoftLayer_Layout_Container', 'getAllObjects')
        from SoftLayer.sltypes.Layout_Container import Layout_Container
        return data

    def getObject(self, identifier: int) -> 'Layout_Container':
        """Retrieve a SoftLayer_Layout_Container record."""
        data = self.client.call('SoftLayer_Layout_Container', 'getObject', id=identifier)
        from SoftLayer.sltypes.Layout_Container import Layout_Container
        return data

    def getLayoutContainerType(self, identifier: int) -> 'Layout_Container_Type':
        """"""
        data = self.client.call('SoftLayer_Layout_Container', 'getLayoutContainerType', id=identifier)
        from SoftLayer.sltypes.Layout_Container_Type import Layout_Container_Type
        return data

    def getLayoutItems(self, identifier: int) -> list['Layout_Item']:
        """"""
        data = self.client.call('SoftLayer_Layout_Container', 'getLayoutItems', id=identifier)
        from SoftLayer.sltypes.Layout_Item import Layout_Item
        return data
