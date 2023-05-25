from SoftLayer.sltypes.Entity import Entity

class Container_User_Customer_External_Binding(Entity):
    """Container classed used to hold external authentication information"""
    authenticationToken: str
    openIdConnectAccessToken: str
    openIdConnectAccountId: int
    openIdConnectProvider: str
    password: str
    securityQuestionAnswer: str
    securityQuestionId: int
    username: str
    vendor: str
