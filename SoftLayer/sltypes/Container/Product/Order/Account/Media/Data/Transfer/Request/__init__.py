from SoftLayer.sltypes.Account.Media.Data.Transfer.Request import Account_Media_Data_Transfer_Request
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Account_Media_Data_Transfer_Request(Container_Product_Order):
    """This datatype is to be used for data transfer requests."""
    request: Account_Media_Data_Transfer_Request
