from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Item_Policy_Assignment(Entity):
    """Represents the assignment of a policy to a product. The existence of a record means that the associated
product is subject to the terms defined in the document content of the policy."""
    id_: int
    productId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Item_Policy_Assignment'

    def acceptFromTicket(self, identifier: int, ticketId: int) -> bool:
        """Register acceptance of this assignment linking this record to a Ticket."""
        data = self.client.call('SoftLayer_Product_Item_Policy_Assignment', 'acceptFromTicket', ticketId, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Product_Item_Policy_Assignment':
        """Retrieve a SoftLayer_Product_Item_Policy_Assignment record."""
        data = self.client.call('SoftLayer_Product_Item_Policy_Assignment', 'getObject', id=identifier)
        from SoftLayer.sltypes.Product_Item_Policy_Assignment import Product_Item_Policy_Assignment
        return data

    def getPolicyDocumentContents(self, identifier: int) -> str:
        """Retrieve the binary content of the policy document."""
        data = self.client.call('SoftLayer_Product_Item_Policy_Assignment', 'getPolicyDocumentContents', id=identifier)
        return data

    def getPolicyName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Policy_Assignment', 'getPolicyName', id=identifier)
        return data

    def getProduct(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Product_Item_Policy_Assignment', 'getProduct', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data
