from SoftLayer.sltypes.Network.LBaaS.MemberHealth import Network_LBaaS_MemberHealth
from SoftLayer.sltypes.Entity import Entity

class Network_LBaaS_PoolMembersHealth(Entity):
    """SoftLayer_Network_LBaaS_PoolMembersHealth provides statistics of members belonging to a particular pool."""
    membersHealth: list[Network_LBaaS_MemberHealth]
    poolUuid: str
