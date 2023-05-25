from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_NewCustomerSetup(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder when linking
a Bluemix account to a newly created SoftLayer account."""
    authorizationToken: str
    externalAccountId: str
    externalServiceProviderKey: str
