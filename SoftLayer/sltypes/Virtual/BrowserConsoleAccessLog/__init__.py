from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Virtual_BrowserConsoleAccessLog(Entity):
    """The SoftLayer_Virtual_BrowserConsoleAccessLog data type presents the data for events associated with
accessing a VSIs console via the browser interface."""
    createDate: datetime
    eventType: str
    id_: int
    message: str
    modifyDate: datetime
    sourceIp: str
    sourcePort: int
    userId: int
    userType: str
    username: str
