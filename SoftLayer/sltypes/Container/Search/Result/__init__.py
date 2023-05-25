from SoftLayer.sltypes.Entity import Entity

class Container_Search_Result(Entity):
    """The SoftLayer_Container_Search_Result data type represents a result row from an execution of Search service."""
    matchedTerms: list[str]
    relevanceScore: float
    resource: Entity
    resourceType: str
