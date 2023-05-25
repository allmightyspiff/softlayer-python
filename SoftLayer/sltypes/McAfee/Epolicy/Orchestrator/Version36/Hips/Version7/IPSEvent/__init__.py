from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class McAfee_Epolicy_Orchestrator_Version36_Hips_Version7_IPSEvent(Entity):
    """The McAfee_Epolicy_Orchestrator_Version36_Hips_Version7_IPSEvent data type represents a single IPS event.  It
contains details about the event such as the date the event occurred, the process that generated it, the
severity of the event, and the action taken."""
    incidentTime: datetime
    processName: str
    reactionText: str
    remoteIpAddress: str
    severityText: str
