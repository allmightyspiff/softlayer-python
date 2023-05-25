from SoftLayer.sltypes.Entity import Entity

class Network_LBaaS_MemberHealth(Entity):
    """SoftLayer_Network_LBaaS_MemberHealth is a collection member metrics retrieved from a LBaaS VSI instance. The
available metrics are: <ul> <li>Name of the member</li> <li>Status of the member up or down</li> <li>Uuid of
the member</li> </ul>"""
    status: str
    uuid: str
