from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Storage_Credential(Entity):
    """The SoftLayer_Network_Storage_Credential data type will give you an overview of the usernames that are
currently attached to your storage device."""
    accountId: str
    createDate: datetime
    id_: int
    modifyDate: datetime
    nasCredentialTypeId: int
    password: str
    username: str
