from SoftLayer.sltypes.Container.Product.Order.Attribute.Address import Container_Product_Order_Attribute_Address
from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Attribute_Organization(Entity):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. The
SoftLayer_Container_Product_Order_Attribute_Organization datatype contains the organization information."""
    address: Container_Product_Order_Attribute_Address
    faxNumber: str
    organizationName: str
    phoneNumber: str
