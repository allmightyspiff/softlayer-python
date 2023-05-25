from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Logging_Syslog(Entity):
    """The Syslog class holds a single line from the Networking Firewall "Syslog" record, for firewall detected and
blocked attempts on a server."""
    createDate: datetime
    destinationIpAddress: str
    destinationPort: int
    eventType: str
    message: str
    protocol: str
    sourceIpAddress: str
    sourcePort: int
    totalEvents: int
