from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class McAfee_Epolicy_Orchestrator_Version36_Hips_Version7_BlockedApplicationEvent(Entity):
    """The McAfee_Epolicy_Orchestrator_Version36_Hips_Version7_BlockedApplicationEvent data type contains a single
blocked application event. The details of the event are the time the event occurred, the process that
generated the event and a brief description of the application that was blocked."""
    applicationDescription: str
    incidentTime: datetime
    processName: str
