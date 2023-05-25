from SoftLayer.sltypes.Entity import Entity

class Network_LBaaS_LoadBalancerProtocolConfiguration(Entity):
    """SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration specifies the protocol, port, maximum number of
allowed connections and session stickiness for load balancer's front- and backend."""
    backendPort: int
    backendProtocol: str
    clientTimeout: int
    frontendPort: int
    frontendProtocol: str
    listenerUuid: str
    loadBalancingMethod: str
    maxConn: int
    serverTimeout: int
    sessionCookieName: str
    sessionType: str
    tlsCertificateId: int
