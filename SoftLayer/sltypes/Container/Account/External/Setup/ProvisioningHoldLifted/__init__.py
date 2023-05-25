from SoftLayer.sltypes.Container.Account.External.Setup.ProvisioningHoldLifted.Attributes import Container_Account_External_Setup_ProvisioningHoldLifted_Attributes
from SoftLayer.sltypes.Entity import Entity

class Container_Account_External_Setup_ProvisioningHoldLifted(Entity):
    additionalAttributes: Container_Account_External_Setup_ProvisioningHoldLifted_Attributes
    code: str
    error: str
    state: str
