from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_RemoteManagement_Command_Request(Entity):
    """The SoftLayer_Hardware_Component_RemoteManagement_Command_Request contains details for remote management
commands issued to a server's remote management card.  Details for remote management commands such as
powerOn, powerOff, powerCycle, rebootDefault, rebootSoft, rebootHard can be retrieved.  Details such as the
user who issued the command, the id of the remote management card the command was issued, when the command
was issued may be retrieved."""
    createDate: datetime
    hardwareId: int
    modifyDate: datetime
    processed: bool
