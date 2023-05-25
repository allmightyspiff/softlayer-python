from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Network_Application_Delivery_Controller(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place an application delivery controller order with SoftLayer."""
    applicationDeliveryControllerId: int
