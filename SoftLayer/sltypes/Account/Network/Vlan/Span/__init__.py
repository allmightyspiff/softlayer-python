from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Account_Network_Vlan_Span(Entity):
    """The SoftLayer_Account_Network_Vlan_Span data type exposes the setting which controls the automatic spanning
of private VLANs attached to a given customers account."""
    enabledFlag: bool
    id_: int
    lastAppliedDate: datetime
    lastVerifiedDate: datetime
    modifyDate: datetime
