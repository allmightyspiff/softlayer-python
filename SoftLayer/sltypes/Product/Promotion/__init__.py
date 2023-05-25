from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Promotion(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Promotion'

    def findByPromoCode(self, code: str) -> 'Container_Product_Promotion':
        data = self.client.call('SoftLayer_Product_Promotion', 'findByPromoCode', code)
        from SoftLayer.sltypes.Container_Product_Promotion import Container_Product_Promotion
        return data

    def getObject(self, identifier: int) -> 'Product_Promotion':
        """Retrieve a SoftLayer_Product_Promotion record."""
        data = self.client.call('SoftLayer_Product_Promotion', 'getObject', id=identifier)
        return data
