from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_User_Customer_External_Binding(Container_Product_Order):
    """This container type is used for placing orders for external authentication, such as phone-based
authentication."""
    externalId: str
    userId: int
    vendorId: int
