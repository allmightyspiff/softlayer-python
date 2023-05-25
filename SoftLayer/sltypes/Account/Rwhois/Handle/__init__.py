from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Account_Rwhois_Handle(Entity):
    """Provides a means of tracking handle identifiers at the various regional internet registries (RIRs). These
objects are used by the [[SoftLayer_Network_Subnet_Registration
(type)|SoftLayer_Network_Subnet_Registration]] objects to identify a customer or organization when a subnet
is registered."""
    accountId: int
    createDate: datetime
    handle: str
    id_: int
    modifyDate: datetime
