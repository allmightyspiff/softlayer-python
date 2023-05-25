from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Package_Type(Entity):
    """The [[SoftLayer_Product_Package_Type]] object indicates the type for a service offering (package). The type
can be used to filter packages. For example, if you are looking for the package representing virtual servers,
you can filter on the type's key name of '''VIRTUAL_SERVER_INSTANCE'''. For bare metal servers by core or
CPU, filter on '''BARE_METAL_CORE''' or '''BARE_METAL_CPU''', respectively."""
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Package_Type'

    def getAllObjects(self) -> list['Product_Package_Type']:
        """Get all the package types."""
        data = self.client.call('SoftLayer_Product_Package_Type', 'getAllObjects')
        from SoftLayer.sltypes.Product_Package_Type import Product_Package_Type
        return data

    def getObject(self, identifier: int) -> 'Product_Package_Type':
        """Retrieve a SoftLayer_Product_Package_Type record."""
        data = self.client.call('SoftLayer_Product_Package_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.Product_Package_Type import Product_Package_Type
        return data

    def getPackages(self, identifier: int) -> list['Product_Package']:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Type', 'getPackages', id=identifier)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data
