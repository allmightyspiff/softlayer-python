from SoftLayer.sltypes.Entity import Entity

class Container_Product_Item_Category_Question_Answer(Entity):
    """The SoftLayer_Container_Product_Item_Category_Question_Answer data type represents an answer to an item
category question.  It contains the category, the question being answered, and the answer."""
    answer: str
    categoryCode: str
    categoryId: int
    questionId: int
