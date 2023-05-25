from SoftLayer.sltypes.Entity import Entity

class Survey_Answer(Entity):
    """The SoftLayer_Survey_Answer data type contains general information relating to a single SoftLayer survey
answer."""
    answer: str
    answerOrder: int
    id_: int
    surveyQuestionId: int
