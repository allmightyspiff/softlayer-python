from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Monitoring_Alarm_History(Entity):
    """The SoftLayer_Container_Monitoring_Alarm_History data type contains information relating to SoftLayer
monitoring alarm history."""
    accountId: int
    agentId: int
    alarmId: str
    closedDate: datetime
    createDate: datetime
    message: str
    robotId: int
    severity: str
