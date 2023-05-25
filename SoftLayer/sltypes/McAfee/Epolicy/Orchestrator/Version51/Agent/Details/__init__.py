from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class McAfee_Epolicy_Orchestrator_Version51_Agent_Details(Entity):
    """The McAfee_Epolicy_Orchestrator_Version51_Agent_Details data type represents a virus scan agent and contains
details about its version."""
    agentVersion: str
    lastUpdate: datetime
