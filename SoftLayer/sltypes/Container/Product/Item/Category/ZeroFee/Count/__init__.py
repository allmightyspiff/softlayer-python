from SoftLayer.sltypes.Entity import Entity

class Container_Product_Item_Category_ZeroFee_Count(Entity):
    """The SoftLayer_Container_Product_Item_Category_ZeroFee_Count data type represents a count of zero fee
billing/invoice items."""
    categoryCode: str
    categoryId: int
    categoryName: str
    count: int
