from SoftLayer.sltypes.Container.Product.Order.Network.Message.Delivery import Container_Product_Order_Network_Message_Delivery
from SoftLayer.sltypes.Container_Product_Order_Network_Message_Delivery import Container_Product_Order_Network_Message_Delivery

class Container_Product_Order_Network_Message_Delivery_Upgrade(Container_Product_Order_Network_Message_Delivery):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place an upgrade order for network message delivery."""
    messageDeliveryId: int
