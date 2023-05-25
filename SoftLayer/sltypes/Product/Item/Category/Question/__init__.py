from SoftLayer.sltypes.Entity import Entity

class Product_Item_Category_Question(Entity):
    """The SoftLayer_Product_Item_Category_Question data type represents a single question to be answered by an end
user.  The question may or may not be required which can be located by looking at the 'required' property on
the item category references.  The answerValueExpression property is a regular expression that is used to
validate the answer to the question.  The description and valueExample properties can be used to get an idea
of the type of answer that should be provided."""
    answerValueExpression: str
    description: str
    fieldTypeId: int
    id_: int
    keyName: str
    question: str
    valueExample: str
