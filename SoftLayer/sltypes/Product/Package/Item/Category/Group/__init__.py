from SoftLayer.sltypes.Entity import Entity

class Product_Package_Item_Category_Group(Entity):
    """This class is used to organize categories for a service offering. A service offering (usually) contains
multiple categories (e.g., server, os, disk0, ram). This class allows us to organize the prices into related
item category groups."""
    itemCategoryId: int
    packageId: int
    sort: int
    title: str
