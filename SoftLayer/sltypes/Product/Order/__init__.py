from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Order(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Order'

    def checkItemAvailability(self, itemPrices: 'Product_Item_Price', accountId: int, availabilityTypeKeyNames: str) -> bool:
        data = self.client.call('SoftLayer_Product_Order', 'checkItemAvailability', itemPrices, accountId, availabilityTypeKeyNames)
        return data

    def checkItemAvailabilityForImageTemplate(self, imageTemplateId: int, accountId: int, packageId: int, availabilityTypeKeyNames: str) -> bool:
        data = self.client.call('SoftLayer_Product_Order', 'checkItemAvailabilityForImageTemplate', imageTemplateId, accountId, packageId, availabilityTypeKeyNames)
        return data

    def checkItemConflicts(self, itemPrices: 'Product_Item_Price') -> bool:
        """Check order items for conflicts"""
        data = self.client.call('SoftLayer_Product_Order', 'checkItemConflicts', itemPrices)
        return data

    def getExternalPaymentAuthorizationReceipt(self, token: str, payerId: str) -> 'Container_Product_Order_Receipt':
        """Returns an order receipt for a completed external (PayPal) payment authorization."""
        data = self.client.call('SoftLayer_Product_Order', 'getExternalPaymentAuthorizationReceipt', token, payerId)
        from SoftLayer.sltypes.Container_Product_Order_Receipt import Container_Product_Order_Receipt
        return data

    def getNetworks(self, locationId: int, packageId: int, accountId: int) -> list['Container_Product_Order_Network']:
        """(DEPRECATED) Retrieve the networks that are available during ordering."""
        data = self.client.call('SoftLayer_Product_Order', 'getNetworks', locationId, packageId, accountId)
        from SoftLayer.sltypes.Container_Product_Order_Network import Container_Product_Order_Network
        return data

    def getResellerOrder(self, orderContainer: 'Container_Product_Order') -> 'Container_Product_Order':
        """Get External Reseller pricing where applicable"""
        data = self.client.call('SoftLayer_Product_Order', 'getResellerOrder', orderContainer)
        from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order
        return data

    def getTaxCalculationResult(self, orderHash: str) -> 'Container_Tax_Cache':
        """Get the results of a tax calculation."""
        data = self.client.call('SoftLayer_Product_Order', 'getTaxCalculationResult', orderHash)
        from SoftLayer.sltypes.Container_Tax_Cache import Container_Tax_Cache
        return data

    def getVlans(self, locationId: int, packageId: int, selectedItems: str, vlanIds: int, subnetIds: int, accountId: int, orderContainer: 'Container_Product_Order', hardwareFirewallOrderedFlag: bool) -> 'Container_Product_Order_Network_Vlans':
        """Get the VLANs that are available during ordering"""
        data = self.client.call('SoftLayer_Product_Order', 'getVlans', locationId, packageId, selectedItems, vlanIds, subnetIds, accountId, orderContainer, hardwareFirewallOrderedFlag)
        from SoftLayer.sltypes.Container_Product_Order_Network_Vlans import Container_Product_Order_Network_Vlans
        return data

    def placeOrder(self, orderData: 'Container_Product_Order', saveAsQuote: bool) -> 'Container_Product_Order_Receipt':
        """Place an order using the [[SoftLayer_Container_Product_Order]] data type."""
        data = self.client.call('SoftLayer_Product_Order', 'placeOrder', orderData, saveAsQuote)
        from SoftLayer.sltypes.Container_Product_Order_Receipt import Container_Product_Order_Receipt
        return data

    def placeQuote(self, orderData: 'Container_Product_Order') -> 'Container_Product_Order_Receipt':
        """Place a quote"""
        data = self.client.call('SoftLayer_Product_Order', 'placeQuote', orderData)
        from SoftLayer.sltypes.Container_Product_Order_Receipt import Container_Product_Order_Receipt
        return data

    def processExternalPaymentAuthorization(self, token: str, payerId: str) -> 'Container_Product_Order':
        """Process an external (PayPal) payment authorization."""
        data = self.client.call('SoftLayer_Product_Order', 'processExternalPaymentAuthorization', token, payerId)
        from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order
        return data

    def requiredItems(self, itemPrices: 'Product_Item_Price') -> list['Product_Item']:
        """Get list of items that are required with the item prices provided"""
        data = self.client.call('SoftLayer_Product_Order', 'requiredItems', itemPrices)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def verifyOrder(self, orderData: 'Container_Product_Order') -> 'Container_Product_Order':
        """Verify that an order may be successfully placed with the details provided."""
        data = self.client.call('SoftLayer_Product_Order', 'verifyOrder', orderData)
        from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order
        return data
