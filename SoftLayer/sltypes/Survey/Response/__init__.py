from SoftLayer.sltypes.Entity import Entity

class Survey_Response(Entity):
    """The SoftLayer_Survey_Response data type contains general information relating to a single SoftLayer survey
response."""
    otherAnswer: str
    surveyAnswerId: int
