from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Subnet_Registration_Event_Type(Entity):
    """Subnet Registration Event Type objects describe the nature of a
[[SoftLayer_Network_Subnet_Registration_Event]]   The standard values for these objects are as follows: <ul>
<li><strong>REGISTRATION_CREATED</strong> - Indicates that the registration has been created</li>
<li><strong>REGISTRATION_UPDATED</strong> - Indicates that the registration has been updated</li>
<li><strong>REGISTRATION_CANCELLED</strong> - Indicates that the registration has been cancelled</li>
<li><strong>RIR_RESPONSE</strong> - Indicates that an action taken against the RIR has produced a response.
More details will be provided in the event message.</li> <li><strong>ERROR</strong> - Indicates that an error
has been encountered. More details will be provided in the event message.</li> <li><strong>NOTE</strong> - An
employee or other system has entered a note regarding the registration. The note content will be provided in
the event message.</li> </ul>"""
    createDate: datetime
    id_: int
    keyName: str
    modifyDate: datetime
    name: str
