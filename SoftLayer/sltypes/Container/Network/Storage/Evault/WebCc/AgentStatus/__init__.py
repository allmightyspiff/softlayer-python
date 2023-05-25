from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Network_Storage_Evault_WebCc_AgentStatus(Entity):
    """The SoftLayer_Container_Network_Storage_Evault_WebCc_AgentStatus will contain the timestamp of the last
backup performed by the EVault agent.  The agent status will also be returned."""
    lastBackup: datetime
    status: str
