from SoftLayer.sltypes.Network.Storage import Network_Storage
from SoftLayer.sltypes.Container.Product.Order.Network.Storage.AsAService import Container_Product_Order_Network_Storage_AsAService
from SoftLayer.sltypes.Container_Product_Order_Network_Storage_AsAService import Container_Product_Order_Network_Storage_AsAService

class Container_Product_Order_Network_Storage_AsAService_Upgrade(Container_Product_Order_Network_Storage_AsAService):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place an upgrade order for Storage as a Service."""
    volume: Network_Storage
