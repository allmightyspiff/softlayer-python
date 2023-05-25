from SoftLayer.sltypes.Container.Product.Order.Network.Protection.Firewall.Dedicated import Container_Product_Order_Network_Protection_Firewall_Dedicated
from SoftLayer.sltypes.Container_Product_Order_Network_Protection_Firewall_Dedicated import Container_Product_Order_Network_Protection_Firewall_Dedicated

class Container_Product_Order_Network_Protection_Firewall_Dedicated_Upgrade(Container_Product_Order_Network_Protection_Firewall_Dedicated):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place an order with SoftLayer."""
    firewallId: int
