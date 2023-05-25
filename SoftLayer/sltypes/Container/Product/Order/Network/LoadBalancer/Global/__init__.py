from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Network_LoadBalancer_Global(Container_Product_Order):
    """The global load balancer service has been deprecated and is no longer available.   This is the datatype that
needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This datatype has everything required
to place a global load balancer order with SoftLayer."""
    domain: str
    hostname: str
