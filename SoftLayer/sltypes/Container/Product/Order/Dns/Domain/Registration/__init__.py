from SoftLayer.sltypes.Container.Dns.Domain.Registration.List import Container_Dns_Domain_Registration_List
from SoftLayer.sltypes.Container.Dns.Domain.Registration.Contact import Container_Dns_Domain_Registration_Contact
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Dns_Domain_Registration(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. The
SoftLayer_Container_Product_Order_Dns_Domain_Registration datatype contains everything required to place a
domain registration order with SoftLayer."""
    administrativeContact: Container_Dns_Domain_Registration_Contact
    billingContact: Container_Dns_Domain_Registration_Contact
    domainRegistrationList: list[Container_Dns_Domain_Registration_List]
    ownerContact: Container_Dns_Domain_Registration_Contact
    registrationType: str
    technicalContact: Container_Dns_Domain_Registration_Contact
