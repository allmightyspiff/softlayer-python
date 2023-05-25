from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Virtual_ReservedCapacity(Container_Product_Order):
    """This is the default container type for Reserved Capacity orders."""
    backendRouterId: int
    name: str
