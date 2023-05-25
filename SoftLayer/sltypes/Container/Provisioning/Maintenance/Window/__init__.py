from datetime import datetime
from SoftLayer.sltypes.Product.Item.Category import Product_Item_Category
from SoftLayer.sltypes.Provisioning.Maintenance.Classification import Provisioning_Maintenance_Classification
from SoftLayer.sltypes.Entity import Entity

class Container_Provisioning_Maintenance_Window(Entity):
    """This is the datatype that needs to be populated and sent to
SoftLayer_Provisioning_Maintenance_Window::addCustomerUpgradeWindow. This datatype has everything required to
place an order with SoftLayer."""
    classificationIds: list[Provisioning_Maintenance_Classification]
    itemCategoryIds: list[Product_Item_Category]
    maintenanceWindowId: int
    ticketId: int
    windowMaintenanceDate: datetime
