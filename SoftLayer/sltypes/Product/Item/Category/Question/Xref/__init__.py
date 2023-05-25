from SoftLayer.sltypes.Entity import Entity

class Product_Item_Category_Question_Xref(Entity):
    """The SoftLayer_Product_Item_Category_Question_Xref data type represents a link between an item category and an
item category question.  It also contains a 'required' field that designates if the question is required to
be answered for the given item category."""
    id_: int
    itemCategoryId: int
    locationId: int
    questionId: int
    required: bool
