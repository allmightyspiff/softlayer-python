from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Package_Server_Option(Entity):
    """The [[SoftLayer_Product_Package_Server_Option]] data type contains various data points associated with
package servers that can be used in selection criteria."""
    catalogId: int
    description: str
    id_: int
    type_: str
    value: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Package_Server_Option'

    def getAllOptions(self) -> list['Product_Package_Server_Option']:
        """Get all the package server options"""
        data = self.client.call('SoftLayer_Product_Package_Server_Option', 'getAllOptions')
        from SoftLayer.sltypes.Product_Package_Server_Option import Product_Package_Server_Option
        return data

    def getObject(self, identifier: int) -> 'Product_Package_Server_Option':
        """Retrieve a SoftLayer_Product_Package_Server_Option record."""
        data = self.client.call('SoftLayer_Product_Package_Server_Option', 'getObject', id=identifier)
        from SoftLayer.sltypes.Product_Package_Server_Option import Product_Package_Server_Option
        return data

    def getOptions(self, type_: str) -> list['Product_Package_Server_Option']:
        """Get all the package server options of a particular type"""
        data = self.client.call('SoftLayer_Product_Package_Server_Option', 'getOptions', type)
        from SoftLayer.sltypes.Product_Package_Server_Option import Product_Package_Server_Option
        return data
