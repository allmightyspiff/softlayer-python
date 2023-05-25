from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Monitor_Version1_Query_Result(Entity):
    """The monitoring result object is used to show the status of the actions taken by the monitoring system.   In
general, only the responseStatus variable is needed, as it holds the information on the status of the
service."""
    finishTime: datetime
    responseStatus: int
    responseTime: float
