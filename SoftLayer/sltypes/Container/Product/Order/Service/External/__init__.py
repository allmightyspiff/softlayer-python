from SoftLayer.sltypes.Service.External.Resource import Service_External_Resource
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Service_External(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder."""
    externalResources: list[Service_External_Resource]
