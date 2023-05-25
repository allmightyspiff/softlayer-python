from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_LBaaS_Pool(Entity):
    """The SoftLayer_Network_LBaaS_Pool type presents a structure containing attributes of a load balancer pool such
as the protocol, protocol port and the load balancing algorithm used."""
    createDate: datetime
    loadBalancingAlgorithm: str
    modifyDate: datetime
    protocol: str
    protocolPort: int
    provisioningStatus: str
    uuid: str
