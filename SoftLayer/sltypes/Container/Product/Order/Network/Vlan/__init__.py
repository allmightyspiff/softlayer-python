from SoftLayer.sltypes.Hardware import Hardware
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Network_Vlan(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place a network vlan order with SoftLayer."""
    description: str
    hostnameDatacenter: str
    hostnameRouter: str
    id_: int
    name: str
    router: Hardware
    routerId: int
    subnets: list[Container_Product_Order]
    vlanNumber: int
