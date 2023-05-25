from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Network import Network
from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Network(Entity):
    """(DEPRECATED) This type contains the structure of network-related objects that may be specified when ordering
services."""
    network: Network
    publicVlans: list[Container_Product_Order]
    subnets: list[Container_Product_Order]
