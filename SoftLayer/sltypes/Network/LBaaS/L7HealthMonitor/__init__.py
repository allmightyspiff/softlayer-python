from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_LBaaS_L7HealthMonitor(Entity):
    """The SoftLayer_Network_LBaaS_L7HealthMonitor type presents a structure containing attributes of a health
monitor object associated with a L7 pool instance. Note that the relationship between backend (L7 pool) and
health monitor is 1-to-1, pools object associated with a health monitor must have the same pair of protocol
and port. Example: frontend FA: http, 80   - backend BA: http, 3456 - healthmonitor HM_http3456 frontend FB:
https, 443 - backend BB: http, 3456 - healthmonitor HM_http3456"""
    createDate: datetime
    interval: int
    maxRetries: int
    modifyDate: datetime
    monitorType: str
    provisioningStatus: str
    timeout: int
    urlPath: str
