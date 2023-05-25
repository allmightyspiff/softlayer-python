from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Billing_Order_Item_Category_Answer(Entity):
    """The SoftLayer_Billing_Order_Item_Category_Answer data type represents a single answer to an item category
question."""
    answer: str
    createDate: datetime
    questionId: int
