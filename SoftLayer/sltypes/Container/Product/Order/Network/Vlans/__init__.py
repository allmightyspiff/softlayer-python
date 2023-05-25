from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Network_Vlans(Entity):
    """This class contains the collections of public and private VLANs that are available during the ordering
process."""
    privateVlans: list[Container_Product_Order]
    publicVlans: list[Container_Product_Order]
