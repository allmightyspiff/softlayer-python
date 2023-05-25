from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Attribute_Address(Entity):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. The
SoftLayer_Container_Product_Order_Attribute_Address datatype contains the address information."""
    addressLine1: str
    addressLine2: str
    city: str
    countryCode: str
    nonUsState: str
    postalCode: str
    state: str
