from SoftLayer.sltypes.Entity import Entity

class Virtual_Network_SecurityGroup_NetworkComponentBinding(Entity):
    """The SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding data type contains general information
for a single binding. A binding associates a [[SoftLayer_Virtual_Guest_Network_Component]] with a
[[SoftLayer_Network_SecurityGroup]]."""
    id_: int
    networkComponentId: int
    securityGroupId: int
