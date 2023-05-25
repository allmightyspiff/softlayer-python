from SoftLayer.sltypes.Container.Product.Order.Attribute.Organization import Container_Product_Order_Attribute_Organization
from SoftLayer.sltypes.Container.Product.Order.Attribute.Contact import Container_Product_Order_Attribute_Contact
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Security_Certificate(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype contains everything required to place a secure certificate order with SoftLayer."""
    administrativeContact: Container_Product_Order_Attribute_Contact
    billingContact: Container_Product_Order_Attribute_Contact
    certificateSigningRequest: str
    orderApproverEmailAddress: str
    organizationInformation: Container_Product_Order_Attribute_Organization
    renewalFlag: bool
    serverCount: int
    serverType: str
    technicalContact: Container_Product_Order_Attribute_Contact
    validityMonths: int
