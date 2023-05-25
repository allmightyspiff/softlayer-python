from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_SecurityGroup_Rule(Entity):
    """The SoftLayer_Network_SecurityGroup_Rule data type contains general information for a single rule that
belongs to a [[SoftLayer_Network_SecurityGroup|security group]]. By default, all traffic (both inbound and\u2028
outbound) to a virtual server instance is blocked. Security group rules are permissive, and define the
allowed incoming (ingress) and outgoing (egress) traffic to both the public and private interfaces of a\u2028
virtual server instance. The order of rules within a security group does not matter and priority always falls
to the least restrictive rule."""
    createDate: datetime
    direction: str
    ethertype: str
    id_: int
    modifyDate: datetime
    portRangeMax: int
    portRangeMin: int
    protocol: str
    remoteGroupId: int
    remoteIp: str
    securityGroupId: int
