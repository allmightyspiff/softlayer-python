from SoftLayer.sltypes.Network.LBaaS.MemberHealth import Network_LBaaS_MemberHealth
from SoftLayer.sltypes.Entity import Entity

class Network_LBaaS_L7PoolMembersHealth(Entity):
    """SoftLayer_Network_LBaaS_L7PoolMembersHealth provides statistics of members belonging to a particular L7 pool."""
    l7PoolUuid: str
    membersHealth: list[Network_LBaaS_MemberHealth]
