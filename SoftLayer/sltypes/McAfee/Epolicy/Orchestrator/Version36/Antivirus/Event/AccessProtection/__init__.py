from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event_AccessProtection(Entity):
    """The McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event_AccessProtection data type represents an access
protection event. It contains details about the event such as when it occurs, the process that caused it, and
the rule that triggered the event."""
    eventLocalDateTime: datetime
    filename: str
    processName: str
    ruleName: str
    source: str
