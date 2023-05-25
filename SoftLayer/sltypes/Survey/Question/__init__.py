from SoftLayer.sltypes.Entity import Entity

class Survey_Question(Entity):
    """The SoftLayer_Survey_Question data type contains general information relating to a single SoftLayer survey
question."""
    id_: int
    isRequired: int
    multiAnswer: int
    question: str
    questionOrder: int
    surveyId: int
