from SoftLayer.sltypes.Entity import Entity

class Account_Link_OpenStack_LinkRequest(Entity):
    """Details required for OpenStack link request"""
    desiredPassword: str
    desiredProjectName: str
    desiredUsername: str
