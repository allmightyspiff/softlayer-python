from SoftLayer.sltypes.Network.Vlan import Network_Vlan
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Network_Protection_Firewall_Dedicated(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place a hardware (dedicated) firewall order with SoftLayer."""
    name: str
    routerId: int
    vlan: Network_Vlan
    vlanId: int
