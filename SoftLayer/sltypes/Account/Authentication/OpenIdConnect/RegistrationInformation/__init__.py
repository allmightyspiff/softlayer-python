from SoftLayer.sltypes.User.Customer import User_Customer
from SoftLayer.sltypes.Entity import Entity

class Account_Authentication_OpenIdConnect_RegistrationInformation(Entity):
    existingBlueIdFlag: bool
    federatedEmailDomainFlag: bool
    user: User_Customer
