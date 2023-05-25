from SoftLayer.sltypes.Entity import Entity

class Container_Software_Component_HostIps_Policy(Entity):
    """The SoftLayer_Container_Software_Component_HostIps_Policy container holds the title and value of a current
host ips policy."""
    policy: str
    policyTitle: str
