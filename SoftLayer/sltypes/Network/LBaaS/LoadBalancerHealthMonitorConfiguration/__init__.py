from SoftLayer.sltypes.Entity import Entity

class Network_LBaaS_LoadBalancerHealthMonitorConfiguration(Entity):
    """SoftLayer_Network_LBaaS_LoadBalancerHealthMonitorConfiguration specifies the check method to be used for
health monitoring backend members."""
    backendPort: int
    backendProtocol: str
    healthMonitorUuid: str
    interval: int
    maxRetries: int
    timeout: int
    urlPath: str
