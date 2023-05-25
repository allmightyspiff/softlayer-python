from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class McAfee_Epolicy_Orchestrator_Version45_Event(Entity):
    """The McAfee_Epolicy_Orchestrator_Version45_Event data type represents a single event. It contains details
about the event such as the date the event occurred, the virus or intrusion that is detected and the action
that is taken."""
    detectedUtc: datetime
    sourceIpv4: str
    sourceProcessName: str
    targetFilename: str
    threatActionTaken: str
    threatName: str
    threatSeverityLabel: str
    threatType: str
