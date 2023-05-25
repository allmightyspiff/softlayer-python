from SoftLayer.sltypes.Entity import Entity

class Container_Policy_Acceptance(Entity):
    """Represents the acceptance status of a Policy."""
    acceptedFlag: bool
    policyName: str
    productPolicyAssignmentId: int
