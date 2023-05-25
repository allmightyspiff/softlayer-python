from SoftLayer.sltypes.Entity import Entity

class Container_User_Customer_OpenIdConnect_MigrationState(Entity):
    daysToGracePeriodEnd: int
    emailAlreadyUsedForInvitationToAccount: bool
    emailAlreadyUsedForLinkToAccount: bool
    existingInvitationOpenIdConnectName: str
    isAccountOpenIdConnectAuthenticated: bool
