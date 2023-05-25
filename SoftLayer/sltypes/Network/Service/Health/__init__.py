from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Service_Health(Entity):
    """Many general services that SoftLayer provides are tracked on the customer portal with a quick status message.
These status message provide users with a quick reference to the health of a service, whether it's up or
down. These services include SoftLayer's Internet backbone connections, VPN entry points, and router
networks. The SoftLayer_Network_Service_Health data type provides the relationship between these services and
their health status."""
    createDate: datetime
    locationId: int
    modifyDate: datetime
    statusId: int
