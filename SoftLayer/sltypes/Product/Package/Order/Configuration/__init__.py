from SoftLayer.sltypes.Entity import Entity

class Product_Package_Order_Configuration(Entity):
    """This datatype describes the item categories that are required for each package to be ordered. For instance,
for package 2, there will be many required categories. When submitting an order for a server, there must be
at most 1 price for each category whose "isRequired" is set. Examples of required categories: - server - ram
- bandwidth - disk0   There are others, but these are the main ones. For each required category, a
SoftLayer_Product_Item_Price must be chosen that is valid for the package."""
    bundledFlag: bool
    errorMessage: str
    id_: int
    isRequired: int
    itemCategoryId: int
    orderStepId: int
    packageId: int
    sort: int
    termFlag: bool
