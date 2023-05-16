# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Order(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Order'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def checkItemAvailability(
        self,
        itemPrices: SoftLayer_Product_Item_Price,
        accountId: int,
        availabilityTypeKeyNames: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'checkItemAvailability',
            itemPrices,
            accountId,
            availabilityTypeKeyNames
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def checkItemAvailabilityForImageTemplate(
        self,
        imageTemplateId: int,
        accountId: int,
        packageId: int,
        availabilityTypeKeyNames: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'checkItemAvailabilityForImageTemplate',
            imageTemplateId,
            accountId,
            packageId,
            availabilityTypeKeyNames
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def checkItemConflicts(
        self,
        itemPrices: SoftLayer_Product_Item_Price
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'checkItemConflicts',
            itemPrices
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getExternalPaymentAuthorizationReceipt(
        self,
        token: str,
        payerId: str
    ) -> 'SoftLayer_Container_Product_Order_Receipt':
        data = self.client.call(
            self.service,
            'getExternalPaymentAuthorizationReceipt',
            token,
            payerId
        )
        from SoftLayer.datatypes.Container.Product.Order.Receipt import Receipt
        return SL_Receipt(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworks(
        self,
        locationId: int,
        packageId: int,
        accountId: int
    ) -> 'list[SoftLayer_Container_Product_Order_Network]':
        data = self.client.call(
            self.service,
            'getNetworks',
            locationId,
            packageId,
            accountId
        )
        from SoftLayer.datatypes.Container.Product.Order.Network import Network
        return SL_Network(data)

# This file was automatically generated with tools/generateTypes.py
    def getResellerOrder(
        self,
        orderContainer: SoftLayer_Container_Product_Order
    ) -> 'SoftLayer_Container_Product_Order':
        data = self.client.call(
            self.service,
            'getResellerOrder',
            orderContainer
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return SL_Order(data)

# This file was automatically generated with tools/generateTypes.py
    def getTaxCalculationResult(
        self,
        orderHash: str
    ) -> 'SoftLayer_Container_Tax_Cache':
        data = self.client.call(
            self.service,
            'getTaxCalculationResult',
            orderHash
        )
        from SoftLayer.datatypes.Container.Tax.Cache import Cache
        return SL_Cache(data)

# This file was automatically generated with tools/generateTypes.py
    def getVlans(
        self,
        locationId: int,
        packageId: int,
        selectedItems: str,
        vlanIds: int,
        subnetIds: int,
        accountId: int,
        orderContainer: SoftLayer_Container_Product_Order,
        hardwareFirewallOrderedFlag: boolean
    ) -> 'SoftLayer_Container_Product_Order_Network_Vlans':
        data = self.client.call(
            self.service,
            'getVlans',
            locationId,
            packageId,
            selectedItems,
            vlanIds,
            subnetIds,
            accountId,
            orderContainer,
            hardwareFirewallOrderedFlag
        )
        from SoftLayer.datatypes.Container.Product.Order.Network.Vlans import Vlans
        return SL_Vlans(data)

# This file was automatically generated with tools/generateTypes.py
    def placeOrder(
        self,
        orderData: SoftLayer_Container_Product_Order,
        saveAsQuote: boolean
    ) -> 'SoftLayer_Container_Product_Order_Receipt':
        data = self.client.call(
            self.service,
            'placeOrder',
            orderData,
            saveAsQuote
        )
        from SoftLayer.datatypes.Container.Product.Order.Receipt import Receipt
        return SL_Receipt(data)

# This file was automatically generated with tools/generateTypes.py
    def placeQuote(
        self,
        orderData: SoftLayer_Container_Product_Order
    ) -> 'SoftLayer_Container_Product_Order_Receipt':
        data = self.client.call(
            self.service,
            'placeQuote',
            orderData
        )
        from SoftLayer.datatypes.Container.Product.Order.Receipt import Receipt
        return SL_Receipt(data)

# This file was automatically generated with tools/generateTypes.py
    def processExternalPaymentAuthorization(
        self,
        token: str,
        payerId: str
    ) -> 'SoftLayer_Container_Product_Order':
        data = self.client.call(
            self.service,
            'processExternalPaymentAuthorization',
            token,
            payerId
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return SL_Order(data)

# This file was automatically generated with tools/generateTypes.py
    def requiredItems(
        self,
        itemPrices: SoftLayer_Product_Item_Price
    ) -> 'list[SoftLayer_Product_Item]':
        data = self.client.call(
            self.service,
            'requiredItems',
            itemPrices
        )
        from SoftLayer.datatypes.Product.Item import Item
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
    def verifyOrder(
        self,
        orderData: SoftLayer_Container_Product_Order
    ) -> 'SoftLayer_Container_Product_Order':
        data = self.client.call(
            self.service,
            'verifyOrder',
            orderData
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return SL_Order(data)


