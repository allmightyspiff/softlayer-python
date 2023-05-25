from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Dns_Domain_Reseller(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. The
SoftLayer_Container_Product_Order_Dns_Domain_Reseller datatype contains everything required to place a domain
reseller credit order with SoftLayer."""
    creditAmount: float
