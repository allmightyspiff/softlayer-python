from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Network_Storage_Hub_ObjectStorage_Provision(Entity):
    """SoftLayer_Container_Network_Storage_Hub_ObjectStorage_Provision provides description of a provision"""
    accountId: int
    provision: str
    provisionCreateDate: datetime
    provisionModifyDate: datetime
    provisionTime: int
