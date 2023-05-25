from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event(Entity):
    """The McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event data type represents a single anti-virus event. It
contains details about the event such as the date the event occurred, the virus that is detected and the
action that is taken."""
    eventLocalDateTime: datetime
    filename: str
    virusName: str
    virusType: str
