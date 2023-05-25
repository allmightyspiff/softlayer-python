from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Network_PerformanceStorage(Container_Product_Order):
    """This is the base data type for Performance storage order containers. If you wish to place an order you must
not use this class and instead use the appropriate child container for the type of storage you would like to
order: [[SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs]] for File and
[[SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi]] for Block storage."""
