from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Media_Transcode_Job_History(Entity):
    createDate: datetime
    publicNotes: str
    transcodeJobId: int
