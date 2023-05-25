from SoftLayer.sltypes.Billing.Order.Quote import Billing_Order_Quote
from SoftLayer.sltypes.Billing_Order_Quote import Billing_Order_Quote
from SoftLayer import BaseClient

class Billing_Order_Cart(Billing_Order_Quote):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Order_Cart'

    def createCart(self, orderData: 'Container_Product_Order') -> int:
        """Create a new cart from the order data provided"""
        data = self.client.call('SoftLayer_Billing_Order_Cart', 'createCart', orderData)
        return data

    def deleteCart(self, identifier: int) -> bool:
        """Delete an existing cart"""
        data = self.client.call('SoftLayer_Billing_Order_Cart', 'deleteCart', id=identifier)
        return data

    def getCartByCartKey(self, cartKey: str) -> 'Billing_Order_Cart':
        """Retrieve a cart."""
        data = self.client.call('SoftLayer_Billing_Order_Cart', 'getCartByCartKey', cartKey)
        return data

    def getObject(self, identifier: int) -> 'Billing_Order_Cart':
        """Retrieve a SoftLayer_Billing_Order_Cart record."""
        data = self.client.call('SoftLayer_Billing_Order_Cart', 'getObject', id=identifier)
        return data

    def getPdf(self, identifier: int) -> str:
        """Retrieve a PDF copy of the cart."""
        data = self.client.call('SoftLayer_Billing_Order_Cart', 'getPdf', id=identifier)
        return data

    def getRecalculatedOrderContainer(self, identifier: int, orderData: 'Container_Product_Order', orderBeingPlacedFlag: bool) -> 'Container_Product_Order':
        """Retrieve order container from a saved cart"""
        data = self.client.call('SoftLayer_Billing_Order_Cart', 'getRecalculatedOrderContainer', orderData, orderBeingPlacedFlag, id=identifier)
        from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order
        return data

    def updateCart(self, identifier: int, orderData: 'Container_Product_Order') -> int:
        """Update an existing cart with the modified order data"""
        data = self.client.call('SoftLayer_Billing_Order_Cart', 'updateCart', orderData, id=identifier)
        return data
