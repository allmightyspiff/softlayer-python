from SoftLayer.sltypes.Entity import Entity

class Account_Link_OpenStack_ProjectCreationDetails(Entity):
    """OpenStack project creation details"""
    domainId: str
    projectId: str
    projectName: str
    userId: str
    userName: str
