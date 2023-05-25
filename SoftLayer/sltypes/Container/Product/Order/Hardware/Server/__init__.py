from SoftLayer.sltypes.Container.Product.Order.Property import Container_Product_Order_Property
from SoftLayer.sltypes.Container.Product.Order import Container_Product_Order
from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order

class Container_Product_Order_Hardware_Server(Container_Product_Order):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place an order with SoftLayer."""
    bootCategoryCode: str
    clusterIdentifier: str
    clusterOrderType: str
    clusterResourceId: int
    driveDestructionDisks: list[str]
    monitoringAgentConfigurationTemplateGroupId: int
    privateCloudServerRole: str
    requiredUpstreamDeviceId: int
    tags: list[Container_Product_Order_Property]
