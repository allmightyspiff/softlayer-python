from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Network_Subnet(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place a subnet order with SoftLayer."""
    description: str
    endPointIpAddressId: int
    endPointVlanId: int
    id_: int
    routerHostname: str
