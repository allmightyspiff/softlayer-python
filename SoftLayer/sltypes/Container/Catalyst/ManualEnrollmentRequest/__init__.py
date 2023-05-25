from SoftLayer.sltypes.Entity import Entity

class Container_Catalyst_ManualEnrollmentRequest(Entity):
    """Contains user information used to request a manual Catalyst enrollment."""
    customerEmail: str
    customerName: str
    startupName: str
    ventureAffiliationFlag: bool
    ventureFundName: str
