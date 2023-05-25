from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Item_Category_Group(Entity):
    """The SoftLayer_Product_Item_Category_Group data type contains general category group information."""
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Item_Category_Group'

    def getObject(self, identifier: int) -> 'Product_Item_Category_Group':
        """Retrieve a SoftLayer_Product_Item_Category_Group record."""
        data = self.client.call('SoftLayer_Product_Item_Category_Group', 'getObject', id=identifier)
        return data
