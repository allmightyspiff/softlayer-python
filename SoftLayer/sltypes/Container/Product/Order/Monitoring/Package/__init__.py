from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Monitoring_Package(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place a Monitoring Package order with SoftLayer. This class is no longer
available."""
    serverType: str
